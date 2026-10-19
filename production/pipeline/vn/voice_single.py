#!/usr/bin/env python3
"""Fold single-line retakes into a chapter's voice records (style guide §9, step 5).

For each retake: download the TTS WAV (or take a local file), save it as TAKES_DIR/take_NN.wav (24 kHz mono, the next free
take numbers), trim leading and trailing silence for the cut, and add a `retake.<id>` job. It also writes a joined MP3 of
the new takes with 1.5 s gaps, and the offsets, so one ElevenLabs transcript checks them all with voice_textcheck.py.

  voice_single.py JOBS.json CUTS.json TAKES_DIR OUT_PREFIX  <id>=<url-or-wav>::<japanese>::<note> ...

Writes JOBS.json and CUTS.json in place, OUT_PREFIX_joined.mp3, OUT_PREFIX_offs.json, OUT_PREFIX_jobs.json and
OUT_PREFIX_cuts.json (the new takes only, numbered from 0 for the transcript check).
"""
import json, os, subprocess, sys, tempfile, urllib.request, wave
import numpy as np

SR = 24000


def trim(x):
    f = int(SR * 0.01)
    e = np.sqrt(np.mean((x[:len(x) // f * f].astype(float).reshape(-1, f) / 32768) ** 2, axis=1))
    on = np.where(e > max(e.max() * 0.05, 1e-3))[0]
    return max(0.0, on[0] * 0.01 - 0.02), min(len(x) / SR, (on[-1] + 1) * 0.01 + 0.02)


def main():
    jobs_p, cuts_p, takes, out = sys.argv[1:5]
    jobs, cuts = json.load(open(jobs_p, encoding="utf-8")), json.load(open(cuts_p, encoding="utf-8"))
    sub_jobs, sub_cuts, offs, pieces, t = [], {}, {}, [], 0.0
    for k, arg in enumerate(sys.argv[5:]):
        lid, rest = arg.split("=", 1)
        src, ja, note = rest.split("::")
        n = len(jobs)
        dst = f"{takes}/take_{n:02d}.wav"
        if src.startswith("http"):
            tmp = tempfile.mktemp(suffix=".wav"); urllib.request.urlretrieve(src, tmp); src = tmp
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", src, "-ar", str(SR), "-ac", "1", "-c:a", "pcm_s16le", dst], check=True)
        w = wave.open(dst); x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)
        a, b = trim(x)
        job = {"key": f"retake.{lid}", "ids": [lid], "texts": [ja], "note": note}
        jobs.append(job); cuts[lid] = [n, a, b, 1.0]
        sub_jobs.append(job); sub_cuts[lid] = [k, a, b, 1.0]; offs[str(k)] = t
        pieces += [x, np.zeros(int(SR * 1.5), dtype=np.int16)]; t += len(x) / SR + 1.5
        print(f"take_{n:02d} {lid}: {a:.2f}-{b:.2f} s")
    json.dump(jobs, open(jobs_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(cuts, open(cuts_p, "w", encoding="utf-8"))
    json.dump(sub_jobs, open(out + "_jobs.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(sub_cuts, open(out + "_cuts.json", "w")); json.dump(offs, open(out + "_offs.json", "w"))
    wav = out + "_joined.wav"
    o = wave.open(wav, "wb"); o.setnchannels(1); o.setsampwidth(2); o.setframerate(SR); o.writeframes(np.concatenate(pieces).tobytes()); o.close()
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", wav, "-c:a", "libmp3lame", "-b:a", "96k", out + "_joined.mp3"], check=True)
    print("joined:", out + "_joined.mp3", os.path.getsize(out + "_joined.mp3"), "bytes")


if __name__ == "__main__":
    main()
