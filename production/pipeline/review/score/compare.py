"""Compare two scoring runs item by item: how much does the score move when nothing changed?

Usage: python3 compare.py RUN_A RUN_B [--out FILE]
Each RUN is a folder with <build>/match.json. Prints strict and lenient counts for each run, the items whose verdict
differs, and the counts if either run's catch is taken (the ceiling for "run the check twice").
Use it on two runs of the same harness to measure noise, and on baseline vs candidate to judge a change: a gain no
bigger than the baseline's own run-to-run swing isn't a gain.
"""
import json, os, sys

K = os.path.dirname(os.path.abspath(__file__))
gt = json.load(open(os.path.join(K, "ground-truth.json")))
items = {i["id"]: i for i in gt["items"] if i["scored"]}
builds = [b["id"] for b in json.load(open(os.path.join(K, "builds.json")))["builds"]]
RANK = {"hit": 2, "partial": 1, "miss": 0}


def load(run):
    v = {}
    for b in builds:
        p = os.path.join(run, b, "match.json")
        if os.path.exists(p):
            for it in json.load(open(p))["items"]:
                if it["id"] in items:
                    v[it["id"]] = it["verdict"]
    return v


a, b = load(sys.argv[1]), load(sys.argv[2])
out = []
for name, v in (("A", a), ("B", b)):
    s = sum(v.get(i) == "hit" for i in items); l = sum(v.get(i) in ("hit", "partial") for i in items)
    out.append(f"Run {name}: strict {s}/{len(items)}, lenient {l}/{len(items)}")
either = {i: max(a.get(i, "miss"), b.get(i, "miss"), key=RANK.get) for i in items}
both = {i: min(a.get(i, "miss"), b.get(i, "miss"), key=RANK.get) for i in items}
out.append(f"Either run: strict {sum(v == 'hit' for v in either.values())}, lenient {sum(v != 'miss' for v in either.values())}")
out.append(f"Both runs: strict {sum(v == 'hit' for v in both.values())}, lenient {sum(v != 'miss' for v in both.values())}")
diff = [i for i in items if a.get(i, "miss") != b.get(i, "miss")]
out.append(f"Items whose verdict differs: {len(diff)} of {len(items)}")
out += ["", "| Item | Kind | A | B |", "|---|---|---|---|"]
out += [f"| {i} {items[i]['item'][:60]} | {items[i]['kind']} | {a.get(i, 'miss')} | {b.get(i, 'miss')} |" for i in diff]
text = "\n".join(out)
if "--out" in sys.argv:
    open(sys.argv[sys.argv.index("--out") + 1], "w").write(text + "\n")
print(text)
