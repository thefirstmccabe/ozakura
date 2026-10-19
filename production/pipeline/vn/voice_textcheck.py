"""Check that each cut holds its line: compare the transcript characters inside every cut with the expected Japanese
(both read as hiragana with pykakasi, punctuation stripped). Report-only.

Usage: python3 voice_textcheck.py jobs.json cuts.json stt_words.json offsets.json [--min 0.8]
Prints one row per line below the threshold (expected vs heard) and a summary.
"""
import json, re, sys, difflib, argparse
import pykakasi
ap = argparse.ArgumentParser(); ap.add_argument("jobs"); ap.add_argument("cuts"); ap.add_argument("words"); ap.add_argument("offs")
ap.add_argument("--min", type=float, default=0.8); a = ap.parse_args()
_k = pykakasi.kakasi()
kana = lambda t: "".join(x["hira"] for x in _k.convert(t))
norm = lambda t: re.sub(r"[\s、。！？!?…「」『』・〜―ー\-\"'（）()]", "", kana(t))
jobs, cuts, words, offs = (json.load(open(p, encoding="utf-8")) for p in (a.jobs, a.cuts, a.words, a.offs))
chars = [w for w in words if w["type"] == "word"]
text = {i: t for j in jobs for i, t in zip(j["ids"], j["texts"])}
bad, n = [], 0
for lid, (take, s, e, _) in cuts.items():
    if lid not in text or str(take) not in offs: continue
    off = float(offs[str(take)]); n += 1
    heard = "".join(c["text"] for c in chars if off + s - 0.05 <= c["start"] < off + e + 0.05)
    r = difflib.SequenceMatcher(None, norm(text[lid]), norm(heard), autojunk=False).ratio()
    if r < a.min: bad.append((lid, round(r, 2), text[lid], heard))
for b in bad: print(f"  {b[0]} {b[1]}\n    expected: {b[2]}\n    heard:    {b[3]}")
print(f"{n} lines checked; {len(bad)} below {a.min}")
