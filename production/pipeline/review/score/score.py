"""Tally a scoring run: the matcher's JSON per build -> the baseline table.

Counts only ground-truth items with scored=true. A hit is strict; "hit or partial" is the lenient count. Findings that
match no author item are reported as unmatched (the false-alarm side; some are real problems he never mentioned).
Usage: python3 score.py RUN_DIR   (RUN_DIR/<build>/match.json for every build in builds.json)
Writes RUN_DIR/results.md and prints it.
"""
import json, os, sys
from collections import Counter, defaultdict

K = os.path.dirname(os.path.abspath(__file__))
run = sys.argv[1]
gt = json.load(open(os.path.join(K, "ground-truth.json")))
builds = [b["id"] for b in json.load(open(os.path.join(K, "builds.json")))["builds"]]
items = {i["id"]: i for i in gt["items"] if i["scored"]}
CHECKS = ["continuity", "diagnosis", "lint", "reader1", "reader2", "reader3", "onmodel", "build"]

verdict, by_check, findings, liked, missing = {}, defaultdict(dict), [], [], {}
for b in builds:
    p = os.path.join(run, b, "match.json")
    if not os.path.exists(p):
        missing[b] = "no match.json"; continue
    m = json.load(open(p))
    if m.get("missing_reports"): missing[b] = ", ".join(m["missing_reports"])
    findings += [dict(f, build=b) for f in m["findings"]]
    liked += [dict(l, build=b) for l in m.get("liked", [])]
    for it in m["items"]:
        if it["id"] not in items: continue
        verdict[it["id"]] = it["verdict"]
        for x in it.get("by", []):
            prev = by_check[it["id"]].get(x["check"])
            if prev != "hit": by_check[it["id"]][x["check"]] = x["verdict"]

def rate(ids):
    n = len(ids); h = sum(verdict.get(i) == "hit" for i in ids); hp = sum(verdict.get(i) in ("hit", "partial") for i in ids)
    return n, h, hp

def row(label, ids):
    n, h, hp = rate(ids)
    return f"| {label} | {n} | {h} ({100*h//n if n else 0}%) | {hp} ({100*hp//n if n else 0}%) |"

out = ["# Harness score against the author's punch lists", "",
       f"Run: `{os.path.basename(os.path.abspath(run))}`. Ground truth: {len(items)} scored items "
       f"({len(gt['items'])} in all). Strict = hit; lenient = hit or partial.", ""]
if missing: out += ["**Missing:** " + "; ".join(f"{b}: {v}" for b, v in missing.items()), ""]
hdr = ["| | Items | Caught (strict) | Caught (lenient) |", "|---|---|---|---|"]
out += ["## Overall", ""] + hdr + [row("All scored items", list(items))]
for c in ("text", "screen", "script"):
    out.append(row(f"Catchable from the {c}", [i for i in items if items[i]["catchable"] == c]))
out += ["", "## By build", ""] + hdr + [row(b, [i for i in items if items[i]["build"] == b]) for b in builds]
out += ["", "## By kind", ""] + hdr
for k, n in Counter(items[i]["kind"] for i in items).most_common():
    out.append(row(f"{k} ({gt['kinds'][k]})", [i for i in items if items[i]["kind"] == k]))
out += ["", "## By check", "", "Items each check raised (strict / lenient), and how many findings it made.", "",
        "| Check | Strict | Lenient | Findings | Matched an item |", "|---|---|---|---|---|"]
for c in CHECKS:
    s = sum(by_check[i].get(c) == "hit" for i in items); l = sum(by_check[i].get(c) in ("hit", "partial") for i in items)
    fs = [f for f in findings if f["check"] == c]; mt = sum(bool(f.get("matches")) for f in fs)
    out.append(f"| {c} | {s} | {l} | {len(fs)} | {mt} |")
tot = len(findings); mt = sum(bool(f.get("matches")) for f in findings)
out += ["", f"**Findings:** {tot} in all; {mt} matched an author item, {tot - mt} didn't "
        f"({100*(tot-mt)//tot if tot else 0}% unmatched).", ""]
out += ["## Item by item", "", "| Item | Build | Kind | Catchable | Verdict | Raised by |", "|---|---|---|---|---|---|"]
for i in items:
    r = ", ".join(f"{c} ({v})" for c, v in by_check[i].items()) or "—"
    out.append(f"| {i} {items[i]['item'][:70]} | {items[i]['build'][:2]} | {items[i]['kind']} | {items[i]['catchable']} | {verdict.get(i, 'not scored')} | {r} |")
fl = [l for l in liked if l.get("flagged")]
out += ["", f"**Liked items flagged as problems:** {len(fl)} of {len(liked)}" +
        ("".join(f"\n- {l['id']} ({l['build']}): " + "; ".join(f"{x['check']}: \"{x['quote'][:120]}\"" for x in l.get("by", [])) for l in fl))]
open(os.path.join(run, "results.md"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
