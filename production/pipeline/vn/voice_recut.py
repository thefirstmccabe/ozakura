"""Final line cuts from a transcript with per-character timestamps (ElevenLabs STT on the joined takes).
Expected text is aligned to the transcript; between the last character of one line and the first of the
next, the cut goes in the longest silence. Lines the transcript missed keep the DP cut (voice_split.py),
clamped between their neighbours. Usage:
python3 voice_recut.py jobs.json dp_segments.json stt_words.json offsets.json TAKES_DIR out.json"""
import json, sys, re, difflib
import pykakasi
_k = pykakasi.kakasi()
kana = lambda t: "".join(x["hira"] for x in _k.convert(t))
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from voice_split import load, silences
jobs, dp, words, offs, takes, outp = (json.load(open(sys.argv[1])), json.load(open(sys.argv[2])), json.load(open(sys.argv[3])),
                                      json.load(open(sys.argv[4])), sys.argv[5], sys.argv[6])
norm = lambda t: re.sub(r"[\s、。！？!?…「」『』・〜―ー\-\"'（）()]", "", kana(t))
chars = [w for w in words if w["type"] == "word" and norm(w["text"])]
out = {}
for i, j in enumerate(jobs):
    off = float(offs[str(i)]); nxt = float(offs.get(str(i + 1), 1e9))
    x, sr = load(f"{takes}/take_{i:02d}.wav"); dur = len(x) / sr
    gaps, lead, tail = silences(x, sr, 0.08)
    st = [c for c in chars if off - 0.2 <= c["start"] < nxt - 1.0]
    # read the transcript as a whole (compound kanji readings), keeping which transcript character each kana came from
    raw = "".join(c["text"] for c in st); owner = [k for k, c in enumerate(st) for _ in c["text"]]
    s_text, s_idx, pos = "", [], 0
    for seg in _k.convert(raw):
        o = seg["orig"]; h = re.sub(r"[\s、。！？!?…「」『』・〜―ー\-\"'（）()]", "", seg["hira"])
        src = owner[pos:pos + len(o)] or [owner[min(pos, len(owner) - 1)]]
        for q, ch in enumerate(h):
            s_text += ch; s_idx.append(src[min(len(src) - 1, q * len(src) // max(1, len(h)))])
        pos += len(o)
    exp, bounds = "", []
    for t in j["texts"]:
        a = len(exp); exp += norm(t); bounds.append((a, len(exp)))
    sm = difflib.SequenceMatcher(None, exp, s_text, autojunk=False); m = {}
    for blk in sm.get_matching_blocks():
        for q in range(blk.size): m[blk.a + q] = blk.b + q
    spans = []
    for (a, b) in bounds:
        hits = [m[q] for q in range(a, b) if q in m]
        cov = len(hits) / max(1, b - a)
        if hits and cov >= 0.4:
            spans.append((st[s_idx[min(hits)]]["start"] - off, st[s_idx[max(hits)]]["start"] - off, st[s_idx[max(hits)]]["end"] - off))
        else:
            spans.append(None)
    n = len(j["ids"]); cuts = []          # cuts[k] = (end of line k, start of line k+1)
    for k in range(n - 1):
        A, B = spans[k], spans[k + 1]
        lo = A[1] + 0.05 if A else dp[j["ids"][k]][2] - 0.3
        hi = B[0] if B else dp[j["ids"][k + 1]][1] + 0.3
        cand = [g for g in gaps if g[1] > lo and g[0] < hi]
        if cand:
            g = max(cand, key=lambda g: min(g[1], hi) - max(g[0], lo))
            cuts.append((max(g[0], lo), min(g[1], hi)))
        else:
            mid = (lo + hi) / 2; cuts.append((mid, mid))
    for k, lid in enumerate(j["ids"]):
        s = lead if k == 0 else cuts[k - 1][1]
        e = tail if k == n - 1 else cuts[k][0]
        out[lid] = [i, max(0.0, s), min(dur, e), 1.0 if spans[k] else 0.0]
        if not spans[k]: print("  kept DP-bounded cut (no transcript match):", lid, j["texts"][k])
json.dump(out, open(outp, "w"))
# report changes vs DP
moved = [(l, dp[l][1:3], out[l][1:3]) for l in out if abs(dp[l][1] - out[l][1]) > 0.2 or abs(dp[l][2] - out[l][2]) > 0.2]
print(len(out), "lines;", len(moved), "moved more than 0.2 s from the first-pass cut")
for l, a, b in moved: print(f"  {l}: {a[0]:.2f}-{a[1]:.2f} -> {b[0]:.2f}-{b[1]:.2f}")
