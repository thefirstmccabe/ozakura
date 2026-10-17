"""Check (and correct) line cuts against a transcription with per-character timestamps.
For each take, the expected lines are aligned to the transcript characters; each line's first and last
matched characters give its true span. A DP cut that disagrees by more than 0.25 s is replaced by the span
snapped outward to the surrounding silences. Prints a report; writes corrected segments.
Usage: python3 voice_check.py jobs.json segments.json stt_words.json offsets.json TAKES_DIR out_segments.json"""
import json, sys, re, difflib
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from voice_split import load, silences
jobs, segs, words, offs, takes, outp = (json.load(open(sys.argv[1])), json.load(open(sys.argv[2])), json.load(open(sys.argv[3])),
                                        json.load(open(sys.argv[4])), sys.argv[5], sys.argv[6])
norm = lambda t: re.sub(r"[\s、。！？!?…「」『』・〜―ー\-\"'（）()]", "", t)
chars = [w for w in words if w["type"] == "word"]
out, flagged = dict(segs), []
for i, j in enumerate(jobs):
    off = float(offs[str(i)]); x, sr = load(f"{takes}/take_{i:02d}.wav"); dur = len(x) / sr
    gaps, lead, tail = silences(x, sr, 0.12)
    st = [c for c in chars if off - 0.2 <= c["start"] <= off + dur + 0.2]
    s_text = "".join(norm(c["text"]) for c in st)
    s_idx = [k for k, c in enumerate(st) for _ in norm(c["text"])]
    exp, bounds = "", []
    for t in j["texts"]:
        a = len(exp); exp += norm(t); bounds.append((a, len(exp)))
    sm = difflib.SequenceMatcher(None, exp, s_text, autojunk=False)
    m = {}
    for blk in sm.get_matching_blocks():
        for q in range(blk.size): m[blk.a + q] = blk.b + q
    sim = sm.ratio()
    for lid, (a, b) in zip(j["ids"], bounds):
        hits = [m[q] for q in range(a, b) if q in m]
        cov = len(hits) / max(1, b - a)
        seg = segs[lid]
        if cov < 0.4:
            flagged.append((lid, f"low coverage {cov:.2f}", j["texts"][j["ids"].index(lid)])); continue
        t0 = st[s_idx[min(hits)]]["start"] - off; t1 = st[s_idx[max(hits)]]["end"] - off
        # snap outward to silence edges
        before = [g[1] for g in gaps if g[1] <= t0 + 0.05]; after = [g[0] for g in gaps if g[0] >= t1 - 0.05]
        s0 = max(before) if before else lead; s1 = min(after) if after else tail
        s0 = max(s0, t0 - 0.6); s1 = min(s1, t1 + 0.6)
        if abs(s0 - seg[1]) > 0.25 or abs(s1 - seg[2]) > 0.25:
            flagged.append((lid, f"cut moved {seg[1]:.2f}-{seg[2]:.2f} -> {s0:.2f}-{s1:.2f}", j["texts"][j["ids"].index(lid)]))
            out[lid] = [seg[0], s0, s1, seg[3]]
    print(f"{i:2d} {j['key']:26s} transcript match {sim:.2f}")
json.dump(out, open(outp, "w"))
print("\nflagged:"); [print(" ", *f) for f in flagged]
