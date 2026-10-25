#!/usr/bin/env python3
"""Per-line text check for a joined-takes transcript without usable timings (style guide §9, step 5).

Wizper's segments can run 40 s, too coarse to cut by time, so this aligns the whole transcript, read as hiragana, against
the expected lines concatenated in take order, and scores each line on the stretch of transcript aligned to it.
Report-only; homophones (斬新/残心, 首相/主将) score as matches because both sides are compared as kana.

  voice_seqcheck.py JOBS.json WIZPER_RESULT.json [--min 0.8]
"""
import json, re, sys, difflib, argparse
import pykakasi
ap = argparse.ArgumentParser(); ap.add_argument("jobs"); ap.add_argument("stt"); ap.add_argument("--min", type=float, default=0.8)
a = ap.parse_args()
_k = pykakasi.kakasi()
kana = lambda t: "".join(x["hira"] for x in _k.convert(t))
norm = lambda t: re.sub(r"[\s、。！？!?…「」『』・〜―ー\-\"'（）()]", "", kana(t))
jobs = json.load(open(a.jobs, encoding="utf-8"))
stt = json.load(open(a.stt, encoding="utf-8")); stt = stt.get("result", stt)
heard = norm(stt["text"])
exp, spans = "", []
for j in jobs:
    t = norm("".join(j["texts"])); spans.append((len(exp), len(exp) + len(t))); exp += t
sm = difflib.SequenceMatcher(None, exp, heard, autojunk=False)
m = [None] * (len(exp) + 1)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    for i in range(i1, i2):
        m[i] = j1 + (i - i1) * (j2 - j1) // max(i2 - i1, 1) if tag != "delete" else j1
m[len(exp)] = len(heard)
bad = 0
for j, (s, e) in zip(jobs, spans):
    hs, he = m[s], m[e] if e < len(exp) else len(heard)
    h = heard[hs:he]; r = difflib.SequenceMatcher(None, exp[s:e], h, autojunk=False).ratio()
    if r < a.min:
        bad += 1; print(f"  {j['ids'][0]} {r:.2f}\n    expected: {''.join(j['texts'])}\n    heard:    {h}")
print(f"{len(jobs)} lines checked; {bad} below {a.min}")
