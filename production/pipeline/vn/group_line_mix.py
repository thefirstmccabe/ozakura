"""Mix a line the whole cast says together (speaker "all", tag "Everyone") from one take per voice.

Each input is a voice's take already packed the usual way (voice_pack.py: trimmed, pitched per §7, leveled), one file per
voice. Every take's onset (first point where its envelope passes -40 dBFS) is aligned to --onset seconds, shifted by that
voice's lead, scaled by its gain, then the sum is leveled to --level dBFS (speech RMS, like voice_pack), peak-limited to
-1 dBFS, faded (10 ms in, 60 ms out) and written as a 64 kbps, 24 kHz mono MP3 like the other voice files.

Ch3 c3_0415 "Itadakimasu!" (Nov 21) was made with:
  python3 group_line_mix.py OUT.mp3 mio=mio.mp3 natsuki=natsuki.mp3 emi=emi.mp3 nanoha=nanoha.mp3 akane=akane.mp3 \
      kohei=kohei.mp3 genji=genji.mp3 --gain mio=0,natsuki=2,emi=-2.5 --default-gain -3 --lead mio=0.09
  (Mio a hair early, Natsuki loudest; the others a little under). Pack the result into the chapter's clip with voice_patch.py.
  The shipped c3_0415 was mixed inline the same way and then trimmed tighter by hand (1.66 s); this script, written
  afterward from that recipe, matches its balance and level (about -21 dB) but leaves a longer tail (about 2.3 s), so
  check the tail by ear before shipping a new one. The seven takes are production/pilot-v2/voice/takes/take_435..441.
"""
import argparse, subprocess, sys
import numpy as np

SR = 24000


def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def onset(x, thresh_db=-40.0, win=240):
    env = np.sqrt(np.convolve(x * x, np.ones(win) / win, mode="same"))
    idx = np.nonzero(env > 10 ** (thresh_db / 20))[0]
    return int(idx[0]) if len(idx) else 0


def kv(s, cast=float):
    return {k: cast(v) for k, v in (p.split("=") for p in s.split(",") if p)} if s else {}


ap = argparse.ArgumentParser()
ap.add_argument("out"); ap.add_argument("takes", nargs="+", help="voice=path")
ap.add_argument("--onset", type=float, default=0.15); ap.add_argument("--level", type=float, default=-21.0)
ap.add_argument("--gain", default="", help="voice=dB,..."); ap.add_argument("--default-gain", type=float, default=0.0)
ap.add_argument("--lead", default="", help="voice=seconds early,...")
a = ap.parse_args()
gains, leads = kv(a.gain), kv(a.lead)
tracks = []
for t in a.takes:
    name, path = t.split("=", 1)
    x = load(path)
    start = int(round((a.onset - leads.get(name, 0.0)) * SR)) - onset(x)
    tracks.append((name, x * 10 ** (gains.get(name, a.default_gain) / 20), start))
lo = min(s for _, _, s in tracks)
if lo < 0:   # a take with a long lead-in: shift everything right
    tracks = [(n, x, s - lo) for n, x, s in tracks]
mix = np.zeros(max(s + len(x) for _, x, s in tracks), dtype=np.float64)
for _, x, s in tracks:
    mix[s:s + len(x)] += x
env = np.sqrt(np.convolve(mix * mix, np.ones(480) / 480, mode="same"))
speech = mix[env > 10 ** (-45 / 20)]
rms = np.sqrt(np.mean(speech ** 2)) if len(speech) else 1e-9
mix *= 10 ** (a.level / 20) / rms
ceil = 10 ** (-1 / 20)
mix = np.where(np.abs(mix) > ceil * 0.8, np.sign(mix) * (ceil * 0.8 + (ceil * 0.2) * np.tanh((np.abs(mix) - ceil * 0.8) / (ceil * 0.2))), mix)
env = np.sqrt(np.convolve(mix * mix, np.ones(480) / 480, mode="same"))
loud = np.nonzero(env > 10 ** (-45 / 20))[0]
if len(loud):   # trim the tail: 80 ms after the last voice ends
    mix = mix[:min(len(mix), loud[-1] + int(0.08 * SR))]
fi, fo = int(0.01 * SR), int(0.06 * SR)
mix[:fi] *= np.linspace(0, 1, fi); mix[-fo:] *= np.linspace(1, 0, fo)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-b:a", "64k", "-ar", str(SR), "-ac", "1", a.out],
               input=mix.astype(np.float32).tobytes(), check=True)
print(f"{a.out}: {len(mix) / SR:.2f} s, {len(tracks)} voices", file=sys.stderr)
