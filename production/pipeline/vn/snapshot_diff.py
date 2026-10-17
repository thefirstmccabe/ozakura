"""Visual regression between two builds (style guide §9, steps 6–9).

Take shots of both builds with qa_play.py --every (one PNG per line, named NNN_<line id>.png, plus NNN_<scene>_start.png),
then compare them line by line. Line IDs renumber when lines are added or removed, so new IDs are matched to old ones
through the two script.json files by (speaker, text); scene starts match by scene name.

Output: OUT/report.txt (changed, new and removed frames) and OUT/changed_NN.jpg contact sheets (baseline left, new
right) so a reviewer looks only at what changed. Unchanged frames are skipped.
Notes: living stills (looping video under a CG) move between shots, so their frames usually show as changed; glance
and move on. Raise --threshold if a build has many.
Usage:
  python3 qa_play.py BASE_URL base_shots --every      # the last approved build
  python3 qa_play.py NEW_URL new_shots --every        # the build under review
  python3 snapshot_diff.py base_shots base_script.json new_shots new_script.json OUT [--threshold 0.2]
"""
import argparse, glob, json, os, re
from PIL import Image, ImageChops, ImageDraw, ImageStat

NAME = re.compile(r"^\d{3}_(.+)\.png$")


def frames(d):
    out = {}
    for p in sorted(glob.glob(os.path.join(d, "*.png"))):
        m = NAME.match(os.path.basename(p))
        if m:
            out.setdefault(m.group(1), p)     # first shot of a key wins (a line seen twice keeps its first frame)
    return out


def text_keys(script_path):
    s = json.load(open(script_path))
    cmds = s["script"] if isinstance(s, dict) else s
    by_id = {}
    for c in cmds:
        if c.get("id") and c.get("text") is not None:
            by_id[c["id"]] = (c.get("who", ""), c["text"])
    return by_id


def diff_score(a, b):
    """Percent of pixels that changed noticeably (grayscale difference above 12 of 255, at half size)."""
    A = Image.open(a).convert("L").resize((590, 410)); B = Image.open(b).convert("L").resize((590, 410))
    d = ImageChops.difference(A, B).point(lambda v: 255 if v > 12 else 0)
    return 100.0 * ImageStat.Stat(d).mean[0] / 255


def sheet(pairs, out, cols=1):
    W = 1180
    rows = []
    for title, a, b in pairs:
        A = Image.open(a).convert("RGB").resize((580, 403)) if a else Image.new("RGB", (580, 403), (60, 20, 30))
        B = Image.open(b).convert("RGB").resize((580, 403)) if b else Image.new("RGB", (580, 403), (60, 20, 30))
        r = Image.new("RGB", (W, 433), (16, 19, 31)); r.paste(A, (0, 30)); r.paste(B, (600, 30))
        ImageDraw.Draw(r).text((8, 8), title, fill=(243, 236, 223)); rows.append(r)
    im = Image.new("RGB", (W, 433 * len(rows)), (16, 19, 31))
    for i, r in enumerate(rows): im.paste(r, (0, i * 433))
    im.save(out, quality=82)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("base"); ap.add_argument("base_script"); ap.add_argument("new"); ap.add_argument("new_script"); ap.add_argument("out")
    ap.add_argument("--threshold", type=float, default=0.2, help="percent of pixels that must change for a frame to count as changed")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    bf, nf = frames(a.base), frames(a.new)
    bt, nt = text_keys(a.base_script), text_keys(a.new_script)
    old_by_text = {}
    for i, k in bt.items(): old_by_text.setdefault(k, []).append(i)
    changed, new, matched = [], [], set()
    for key, path in nf.items():
        old = key if key.endswith("_start") else None
        if old is None:
            cands = old_by_text.get(nt.get(key), [])
            old = cands[0] if len(cands) == 1 else (key if key in bf and bt.get(key) == nt.get(key) else None)
        if old and old in bf:
            matched.add(old)
            sc = diff_score(bf[old], path)
            if sc > a.threshold: changed.append((f"{key}  (was {old})  {sc:.2f}% of pixels changed", bf[old], path))
        else:
            new.append((f"{key}  NEW or reworded", None, path))
    removed = [k for k in bf if k not in matched]
    with open(os.path.join(a.out, "report.txt"), "w") as f:
        f.write(f"base {len(bf)} frames, new {len(nf)} frames\n{len(changed)} changed, {len(new)} new/reworded, {len(removed)} removed\n\n")
        for t, _, _ in changed + new: f.write(t + "\n")
        for k in removed: f.write(f"{k}  REMOVED (or reworded)\n")
    items = changed + new
    for i in range(0, len(items), 8):
        sheet(items[i:i + 8], os.path.join(a.out, f"changed_{i // 8 + 1:02d}.jpg"))
    print(open(os.path.join(a.out, "report.txt")).read().split("\n\n")[0])
