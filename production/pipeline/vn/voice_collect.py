#!/usr/bin/env python3
"""Collect a chapter of single-line TTS takes into voice records (style guide §9, step 5).

voice_single_jobs.py writes one job per line; after the takes come back, this downloads each WAV, saves it as
TAKES_DIR/take_NN.wav (24 kHz mono) numbered from FIRST (after the earlier chapters' takes, so one takes folder and one
merged cuts file serve voice_pack.py), trims leading and trailing silence for the cut, and writes:

  OUT_PREFIX-jobs.json   the jobs, each with its take number
  OUT_PREFIX-cuts.json   {line id: [take, start, end, 1.0]}
  OUT_PREFIX-take-urls.json
  OUT_PREFIX_joined.mp3 + OUT_PREFIX_offs.json   all takes joined with 1.5 s gaps, for one transcript (voice_textcheck.py)

  voice_collect.py SPEC_JOBS.json URLS.json TAKES_DIR FIRST OUT_PREFIX [JOINED_PREFIX]

URLS.json maps the job's position in SPEC_JOBS.json ("0", "1", ...) to its WAV URL.
"""
import json, os, subprocess, sys, tempfile, urllib.request, wave
import numpy as np
from voice_single import trim, SR


def main():
    spec_p, urls_p, takes, first, out = sys.argv[1:6]
    joined = sys.argv[6] if len(sys.argv) > 6 else out
    spec, urls, first = json.load(open(spec_p, encoding="utf-8")), json.load(open(urls_p)), int(first)
    os.makedirs(takes, exist_ok=True)
    jobs, cuts, offs, pieces, t, used = [], {}, {}, [], 0.0, {}
    for k, job in enumerate(spec):
        n = first + k
        dst = f"{takes}/take_{n:02d}.wav"
        src = urls[str(k)]
        tmp = tempfile.mktemp(suffix=".wav"); urllib.request.urlretrieve(src, tmp)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", tmp, "-ar", str(SR), "-ac", "1", "-c:a", "pcm_s16le", dst], check=True)
        os.remove(tmp)
        w = wave.open(dst); x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)
        a, b = trim(x)
        jobs.append({"key": job["key"], "ids": job["ids"], "texts": job["texts"], "take": n,
                     "voice": job["input"]["voice"], "style_instructions": job["input"]["style_instructions"]})
        cuts[job["ids"][0]] = [n, round(a, 3), round(b, 3), 1.0]
        used[str(n)] = src
        offs[str(k)] = round(t, 3)
        pieces += [x, np.zeros(int(SR * 1.5), dtype=np.int16)]; t += len(x) / SR + 1.5
    json.dump(jobs, open(out + "-jobs.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(cuts, open(out + "-cuts.json", "w"))
    json.dump(used, open(out + "-take-urls.json", "w"), indent=1)
    json.dump(offs, open(joined + "_offs.json", "w"))
    wav = joined + "_joined.wav"
    o = wave.open(wav, "wb"); o.setnchannels(1); o.setsampwidth(2); o.setframerate(SR); o.writeframes(np.concatenate(pieces).tobytes()); o.close()
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", wav, "-c:a", "libmp3lame", "-b:a", "96k", joined + "_joined.mp3"], check=True)
    print(len(jobs), "takes", first, "to", first + len(jobs) - 1, "; joined", round(t / 60, 1), "min,",
          os.path.getsize(joined + "_joined.mp3"), "bytes")


if __name__ == "__main__":
    main()
