"""Check the level of every packed voice line (style guide §9, step 5).

voice_pack.py levels each line to the same speech RMS and limits peaks; this verifies the result in the shipped packs.
For every id in VOICE_DIR/index.json ({id: [pack, byte_offset, byte_len]}) it cuts the standalone mp3 out of its pack,
decodes it, and measures speech RMS (20 ms frames above 10% of the loudest, as voice_pack does) and true sample peak.

Flags: speech RMS more than 3 dB from the build's median; peak above -0.3 dBFS (clipping risk); a line under 0.25 s;
a line that's mostly silence.
Usage: python3 voice_levels.py v2/voice [--tol 3]
Exit code 1 if anything is flagged.
"""
import argparse, json, os, subprocess, sys, tempfile
import numpy as np


def decode(mp3_bytes):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        f.write(mp3_bytes); src = f.name
    try:
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-f", "s16le", "-ac", "1", "-ar", "24000", "-"],
                             capture_output=True, check=True).stdout
    finally:
        os.unlink(src)
    return np.frombuffer(raw, dtype=np.int16).astype(float) / 32768, 24000


def measure(x, sr):
    fr = int(sr * 0.02); n = max(1, len(x) // fr)
    e = np.sqrt(np.mean(x[:n * fr].reshape(n, fr) ** 2, axis=1) + 1e-12)
    loud = e > max(e.max() * 0.1, 1e-4)
    v = e[loud]
    rms = 20 * np.log10(np.sqrt(np.mean(v ** 2))) if len(v) else -99
    peak = 20 * np.log10(np.abs(x).max() + 1e-12)
    return rms, peak, len(x) / sr, loud.mean()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("voice_dir"); ap.add_argument("--tol", type=float, default=3.0)
    a = ap.parse_args()
    idx = json.load(open(os.path.join(a.voice_dir, "index.json")))
    packs, rows = {}, []
    for lid, (pack, off, ln) in idx.items():
        if pack not in packs:
            packs[pack] = open(os.path.join(a.voice_dir, pack), "rb").read()
        x, sr = decode(packs[pack][off:off + ln])
        rows.append((lid, *measure(x, sr)))
    med = float(np.median([r[1] for r in rows]))
    flags = []
    for lid, rms, peak, dur, voiced in rows:
        if abs(rms - med) > a.tol: flags.append(f"{lid}: speech RMS {rms:.1f} dB ({rms - med:+.1f} from median {med:.1f})")
        if peak > -0.3: flags.append(f"{lid}: peak {peak:.1f} dBFS (clipping risk)")
        if dur < 0.25: flags.append(f"{lid}: only {dur:.2f} s long")
        if voiced < 0.2: flags.append(f"{lid}: mostly silence ({voiced:.0%} voiced frames)")
    print(f"{len(rows)} lines; median speech RMS {med:.1f} dB; range {min(r[1] for r in rows):.1f} to {max(r[1] for r in rows):.1f}")
    for f in flags: print(f)
    print(f"{len(flags)} flag(s)")
    sys.exit(1 if flags else 0)
