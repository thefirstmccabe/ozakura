"""Carry existing voice cuts over to a recompiled script whose line IDs have shifted.

Line IDs are sequential, so adding or removing any line renumbers everything after it. With stable line IDs, a line keeps its take when its
ID, speaker and Japanese are unchanged. Otherwise this matches the new voice
line list against the old one by content (speaker + Japanese), in order (and then any line that only moved), keeps the cut of every unchanged line under
its new ID, and lists the lines that still need a take (new or changed Japanese).

Usage: python3 voice_remap.py OLD_LINES OLD_CUTS NEW_LINES OUT_CUTS
Prints the IDs that need takes; writes OUT_CUTS (new-ID cuts) and OUT_CUTS.idmap.json (old ID -> new ID).
"""
import json, sys
from difflib import SequenceMatcher

old, cuts, new = (json.load(open(p, encoding="utf-8")) for p in sys.argv[1:4])
key = lambda x: (x["who"], x["ja"])
idmap = {}
# with stable line IDs (style guide §9 step 2) the same ID with the same speaker + Japanese keeps its take as is
old_by_id = {x["id"]: x for x in old}
for x in new:
    o = old_by_id.get(x["id"])
    if o and key(o) == key(x):
        idmap[o["id"]] = x["id"]
# content matching for anything left (older scripts without written IDs, or lines whose ID changed)
rest_old = [x for x in old if x["id"] not in idmap]
taken = set(idmap.values()); rest_new = [x for x in new if x["id"] not in taken]
sm = SequenceMatcher(a=[key(x) for x in rest_old], b=[key(x) for x in rest_new], autojunk=False)
old, new_all, new = rest_old, new, rest_new
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        for k in range(i2 - i1):
            idmap[old[i1 + k]["id"]] = new[j1 + k]["id"]
# second pass: lines that moved (the diff sees a move as delete + insert) keep their take if the same
# speaker + Japanese occurs exactly once among the unmatched lines on each side
from collections import Counter
used_new = set(idmap.values())
left_old = [x for x in old if x["id"] not in idmap]
left_new = [x for x in new if x["id"] not in used_new]
co, cn = Counter(key(x) for x in left_old), Counter(key(x) for x in left_new)
for x in left_new:
    if cn[key(x)] == 1 and co[key(x)] == 1:
        o = next(y for y in left_old if key(y) == key(x))
        idmap[o["id"]] = x["id"]
out = {idmap[o]: cuts[o] for o in idmap if o in cuts}
new = new_all
need = [x for x in new if x["id"] not in out]
json.dump(out, open(sys.argv[4], "w", encoding="utf-8"), ensure_ascii=False)
json.dump(idmap, open(sys.argv[4] + ".idmap.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
dropped = [i for i in old_by_id if i not in idmap]
print(f"kept {len(out)} cuts; dropped {len(dropped)} old lines {dropped}; {len(need)} need takes:")
for x in need:
    print(f"  {x['id']} {x['who']}: {x['ja']}")
