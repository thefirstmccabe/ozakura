"""Cut voiced lines out of the batched takes, apply the cast's post-processing and pack them per scene.

  pitch: style guide §7 ("+2" = asetrate x1.1225 then atempo 0.8909; "+4" = 1.2599 / 0.7937)
  past_natsuki: a soft echo, so the dream voice sits apart from the present day
  every line: 50 ms pad in, 120 ms out, short fades, leveled per line to the same speech RMS (-21 dBFS), peaks limited

Output: OUT/voice/<scene>.mp3 packs (lines concatenated as standalone mp3s), OUT/voice/index.json {id:[pack,offset,len]},
OUT/voice/ja.json {id: Japanese line}.
Usage: python3 voice_pack.py lines.json jobs.json segments.json TAKES_DIR OUT_DIR
"""
import json, subprocess, sys, os, tempfile, wave
import numpy as np


def speech_rms_db(path, a, b):
    w = wave.open(path); sr = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float) / 32768
    x = x[int(a * sr):int(b * sr)]
    fr = int(sr * 0.02); n = max(1, len(x) // fr)
    e = np.sqrt(np.mean(x[:n * fr].reshape(n, fr) ** 2, axis=1) + 1e-12)
    v = e[e > max(e.max() * 0.1, 1e-4)]
    return 20 * np.log10(np.sqrt(np.mean(v ** 2)))

PITCH = {"nanoha": 2, "akane": 2, "rika": 4, "yuzu": 2, "mio": 4}
RATE = {2: (1.1225, 0.8909), 4: (1.2599, 0.7937)}

lines, jobs, segs, takes, out = (json.load(open(sys.argv[1])), json.load(open(sys.argv[2])),
                                 json.load(open(sys.argv[3])), sys.argv[4], sys.argv[5])
os.makedirs(f"{out}/voice", exist_ok=True)
tmp = tempfile.mkdtemp()
by_scene, ja = {}, {}
for x in lines:
    if x["id"] not in segs:
        print("missing", x["id"]); continue
    take, a, b, _ = segs[x["id"]]
    a = max(0.0, a - 0.05); b = b + 0.12
    f = [f"atrim={a:.3f}:{b:.3f}", "asetpts=PTS-STARTPTS"]
    if x["who"] in PITCH:
        r, t = RATE[PITCH[x["who"]]]
        f += [f"asetrate=24000*{r}", "aresample=24000", f"atempo={t}"]
    if x["who"] == "past_natsuki":
        f += ["aecho=0.85:0.6:70|140:0.22|0.12"]
    d = b - a
    gain = max(-12, min(12, -21 - speech_rms_db(f"{takes}/take_{take:02d}.wav", a, b)))
    f += [f"volume={gain:.2f}dB", "alimiter=limit=0.89:attack=2:release=40", "afade=t=in:d=0.02", f"afade=t=out:st={max(0, d - 0.06):.3f}:d=0.06", "aresample=24000"]
    mp3 = f"{tmp}/{x['id']}.mp3"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{takes}/take_{take:02d}.wav", "-af", ",".join(f),
                    "-ac", "1", "-ar", "24000", "-c:a", "libmp3lame", "-b:a", "64k", "-id3v2_version", "0", mp3], check=True)
    by_scene.setdefault(x["scene"], []).append(x["id"])
    ja[x["id"]] = x["ja"]
index = {}
for scene, ids in by_scene.items():
    pack = f"{scene}.mp3"; off = 0
    with open(f"{out}/voice/{pack}", "wb") as fo:
        for i in ids:
            data = open(f"{tmp}/{i}.mp3", "rb").read()
            fo.write(data); index[i] = [pack, off, len(data)]; off += len(data)
json.dump(index, open(f"{out}/voice/index.json", "w"), ensure_ascii=False)
json.dump(ja, open(f"{out}/voice/ja.json", "w"), ensure_ascii=False)
print(len(index), "lines in", len(by_scene), "packs")
