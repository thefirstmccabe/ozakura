#!/usr/bin/env python3
"""Splice re-voiced lines into a built voice folder without touching any other clip (Nov 1).

voice_pack.py rebuilds every clip from the archived takes. The archive is Opus, and the clips built from the original
WAV downloads (most of Ch2, Natsuki's Ch1 re-voice) don't come back byte-identical from a full rebuild, so a single
retake would quietly re-encode about two hundred lines. This takes the clips for the listed IDs from a fresh
voice_pack.py run (REBUILT) and writes them into the live packs (LIVE), keeping every other clip's bytes and order;
index.json offsets and ja.json are updated to match.

Usage: python3 voice_patch.py LIVE_VOICE_DIR REBUILT_VOICE_DIR id1 [id2 ...]
"""
import json, os, sys


def main():
    live, rebuilt, ids = sys.argv[1], sys.argv[2], set(sys.argv[3:])
    L = json.load(open(f"{live}/index.json")); R = json.load(open(f"{rebuilt}/index.json"))
    Lja = json.load(open(f"{live}/ja.json", encoding="utf-8")); Rja = json.load(open(f"{rebuilt}/ja.json", encoding="utf-8"))
    missing = [i for i in ids if i not in R]
    if missing:
        sys.exit(f"not in the rebuilt index: {missing}")

    def clip(index, root, i):
        p, o, n = index[i]
        with open(f"{root}/{p}", "rb") as f:
            f.seek(o); return f.read(n)

    packs = {}   # pack -> ordered ids, in the live order (new IDs go to the end of their rebuilt pack)
    for i, (p, o, _) in sorted(L.items(), key=lambda kv: (kv[1][0], kv[1][1])):
        packs.setdefault(p, []).append(i)
    for i in ids:
        if i not in L:
            packs.setdefault(R[i][0], []).append(i)
    touched = {R[i][0] for i in ids} | {L[i][0] for i in ids if i in L}
    for p in touched:
        data, off, new_index = bytearray(), 0, {}
        for i in packs[p]:
            b = clip(R, rebuilt, i) if i in ids else clip(L, live, i)
            new_index[i] = [p, off, len(b)]; data += b; off += len(b)
        open(f"{live}/{p}", "wb").write(data)
        L.update(new_index)
        print(f"{p}: {len(packs[p])} clips, {sum(1 for i in packs[p] if i in ids)} replaced")
    for i in ids:
        Lja[i] = Rja[i]
    json.dump(L, open(f"{live}/index.json", "w"), ensure_ascii=False)
    json.dump(Lja, open(f"{live}/ja.json", "w"), ensure_ascii=False)


if __name__ == "__main__":
    main()
