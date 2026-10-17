"""Carry existing voice cuts over to a recompiled script whose line IDs have shifted.

Line IDs are sequential, so adding or removing any line renumbers everything after it. This matches the new voice
line list against the old one by content (speaker + Japanese), in order, keeps the cut of every unchanged line under
its new ID, and lists the lines that still need a take (new or changed Japanese).

Usage: python3 voice_remap.py OLD_LINES OLD_CUTS NEW_LINES OUT_CUTS
Prints the IDs that need takes; writes OUT_CUTS (new-ID cuts) and OUT_CUTS.idmap.json (old ID -> new ID).
"""
import json, sys
from difflib import SequenceMatcher

old, cuts, new = (json.load(open(p, encoding="utf-8")) for p in sys.argv[1:4])
key = lambda x: (x["who"], x["ja"])
sm = SequenceMatcher(a=[key(x) for x in old], b=[key(x) for x in new], autojunk=False)
idmap = {}
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        for k in range(i2 - i1):
            idmap[old[i1 + k]["id"]] = new[j1 + k]["id"]
out = {idmap[o]: cuts[o] for o in idmap if o in cuts}
need = [x for x in new if x["id"] not in out]
json.dump(out, open(sys.argv[4], "w", encoding="utf-8"), ensure_ascii=False)
json.dump(idmap, open(sys.argv[4] + ".idmap.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
dropped = [x["id"] for x in old if x["id"] not in idmap]
print(f"kept {len(out)} cuts; dropped {len(dropped)} old lines {dropped}; {len(need)} need takes:")
for x in need:
    print(f"  {x['id']} {x['who']}: {x['ja']}")
