"""Compile an .ozs source script (see the header of production/pilot-v2/script/ch01.ozs) into the
engine's script.json commands, plus a voice job list.

Stable line IDs (style guide §9 step 2): every narration and spoken line carries its ID at the end of the line,
after two spaces, e.g. `> I get up.  #c1_0005` or `kohei(smile): "Morning." || おはよう。  #c1_0003`. The compiler
uses the written ID, so adding or removing lines never renumbers the others (voice cuts, saves and snapshot diffs
stay keyed to the same IDs). Lines without one get the next free number for their scene's prefix;
--write-ids writes those new IDs back into the source.

Usage: python3 compile_script.py OUT_SCRIPT_JSON OUT_VOICE_JSON src1.ozs [src2.ozs ...] [--write-ids]
"""
import json, re, sys

SPEAKERS = {"kohei": "Kōhei", "nanoha": "Nanoha", "natsuki": "Natsuki", "akane": "Akane", "rika": "Rika",
            "ryosuke": "Ryōsuke", "teacher": "Ōno-sensei", "kirishima": "Kirishima", "takatsuki": "Takatsuki",
            "manager": "Manager", "yuzu": "Yuzu", "emi": "Emi", "mio": "Mio", "past_natsuki": "???"}
FACES = {"smile", "neutral", "grin", "deadpan", "surprised", "flustered", "annoyed", "serious", "stillness", "sad"}
ID_TAG = re.compile(r'\s+#((?:p|c\d+)_\d{4,})\s*$')


def split_id(s):
    """'> text  #c1_0042' -> ('> text', 'c1_0042'); lines without an ID tag come back unchanged with None."""
    m = ID_TAG.search(s)
    return (s[:m.start()], m.group(1)) if m else (s, None)


SAY = re.compile(r'^(\w+)(?:<(\w+)>)?(?:\((\w+)\))?:\s*(.+?)\s*(?:\|\|\s*(.*))?$')


def compile_files(paths):
    cmds, voice, errors = [], [], []
    outfit = {}          # who -> current outfit (school, home…)
    shown = {}           # who -> current sprite name
    counters = {}
    scene = None
    used = set()
    new_ids = {}         # (path, line number) -> ID assigned to a line that had none
    for path in paths:   # explicit IDs first, so new ones never collide
        for raw in open(path, encoding="utf-8"):
            _, lid = split_id(raw.rstrip("\n"))
            if lid:
                pre, num = lid.rsplit("_", 1)
                counters[pre] = max(counters.get(pre, 0), int(num))

    def line_id(prefix, written, where_key):
        if written:
            if written in used:
                errors.append(f"{where_key[0]}:{where_key[1]}: duplicate line ID {written}")
            used.add(written)
            return written
        counters[prefix] = counters.get(prefix, 0) + 1
        lid = f"{prefix}_{counters[prefix]:04d}"
        used.add(lid); new_ids[where_key] = lid
        return lid

    for path in paths:
        for n, raw in enumerate(open(path, encoding="utf-8"), 1):
            s = raw.rstrip("\n")
            if not s.strip() or s.lstrip().startswith("#"):
                continue
            s, written = split_id(s)
            where = f"{path}:{n}"
            if s.startswith("== "):
                scene, _, title = s[3:].partition("|")
                scene = scene.strip()
                cmds.append({"t": "scene", "id": scene, "title": title.strip()})
                continue
            prefix = "p" if scene == "prologue" else scene.split("_")[0]
            if s.startswith("> "):
                cmds.append({"t": "nar", "id": line_id(prefix, written, (path, n)), "text": s[2:].strip()})
                continue
            if s.startswith("@"):
                parts = s[1:].split()
                op, args = parts[0], parts[1:]
                if op in ("bg", "cg"):
                    name = args[0]
                    if op == "cg" and name == "-":
                        cmds.append({"t": "cg", "name": None, "tr": args[1] if len(args) > 1 else "fade"})
                    else:
                        cmds.append({"t": op, "name": name, "tr": args[1] if len(args) > 1 else ("cut" if name == "black" and op == "bg" else "fade")})
                    if op == "bg":
                        shown.clear()
                elif op == "bgm":
                    cmds.append({"t": "bgm", "name": None if args[0] == "-" else args[0]})
                elif op == "sfx":
                    cmds.append({"t": "sfx", "name": args[0]})
                elif op == "wait":
                    cmds.append({"t": "wait", "s": float(args[0])})
                elif op == "flash":
                    cmds.append({"t": "bg", "name": "white", "tr": "flash"})
                elif op == "card":
                    cmds.append({"t": "card", "text": s[len("@card "):].strip()})
                elif op == "chapter":
                    num, _, title = s[len("@chapter "):].partition("|")
                    cmds.append({"t": "chapter", "n": int(num), "title": title.strip()})
                elif op == "endchapter":
                    cmds.append({"t": "endchapter", "n": int(args[0])})
                elif op == "mode":
                    cmds.append({"t": "mode", "mode": args[0], **({"label": " ".join(args[1:])} if len(args) > 1 else {})})
                elif op == "show":
                    who, spr = args[0], f"{args[0]}_{args[1]}"
                    outfit[who] = args[1].split("_")[0]
                    shown[who] = spr
                    cmds.append({"t": "show", "who": who, "spr": spr, **({"pos": args[2]} if len(args) > 2 else {})})
                elif op == "move":
                    who = args[0]
                    if who not in shown:
                        errors.append(f"{where}: @move {who} but not on stage")
                    else:
                        cmds.append({"t": "show", "who": who, "spr": shown[who], "pos": args[1]})
                elif op == "hide":
                    shown.pop(args[0], None)
                    cmds.append({"t": "hide", "who": args[0]})
                elif op == "hideall":
                    shown.clear()
                    cmds.append({"t": "hideall"})
                else:
                    errors.append(f"{where}: unknown op @{op}")
                continue
            m = SAY.match(s)
            if not m:
                errors.append(f"{where}: can't parse: {s}")
                continue
            who, expr, face, text, ja = m.groups()
            if who not in SPEAKERS:
                errors.append(f"{where}: unknown speaker {who}")
            if expr:
                if who not in shown:
                    errors.append(f"{where}: {who}<{expr}> but {who} is not on stage")
                spr = f"{who}_{outfit.get(who, 'school')}_{expr}"
                shown[who] = spr
                cmds.append({"t": "show", "who": who, "spr": spr})
            if who == "kohei" and face not in FACES:
                errors.append(f"{where}: Kōhei line needs a face from {sorted(FACES)}")
            if face and who != "kohei":
                if expr:
                    errors.append(f"{where}: use either <expr> (sprite) or (face) (face window), not both")
                if who in shown:
                    errors.append(f"{where}: {who}({face}) is a face-window line, but {who} is on stage")
                face = f"{outfit.get(who, 'school')}_{face}"   # crop of that sprite expression
            lid = line_id(prefix, written, (path, n))
            c = {"t": "say", "id": lid, "who": who, "text": text}
            if face:
                c["face"] = face
            cmds.append(c)
            if ja and ja.strip() != "-":
                voice.append({"id": lid, "who": who, "ja": ja.strip(), "en": text, "scene": scene})
            elif not ja:
                errors.append(f"{where}: spoken line without Japanese (use '|| -' for unvoiced)")
    return cmds, voice, errors, new_ids


def write_ids(new_ids):
    """Append newly assigned IDs to their source lines."""
    by_path = {}
    for (path, n), lid in new_ids.items():
        by_path.setdefault(path, {})[n] = lid
    for path, rows in by_path.items():
        lines = open(path, encoding="utf-8").read().split("\n")
        for n, lid in rows.items():
            lines[n - 1] = lines[n - 1].rstrip() + f"  #{lid}"
        open(path, "w", encoding="utf-8").write("\n".join(lines))


if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if x != "--write-ids"]
    out_script, out_voice, srcs = args[0], args[1], args[2:]
    cmds, voice, errors, new_ids = compile_files(srcs)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    if new_ids:
        if "--write-ids" in sys.argv:
            write_ids(new_ids); print(f"wrote {len(new_ids)} new line IDs into the source")
        else:
            print(f"note: {len(new_ids)} lines have no written ID (run with --write-ids to fix them in the source)")
    json.dump({"speakers": SPEAKERS, "script": cmds}, open(out_script, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    json.dump(voice, open(out_voice, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n_say = sum(c["t"] == "say" for c in cmds); n_nar = sum(c["t"] == "nar" for c in cmds)
    words = sum(len(re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", c["text"]).split()) for c in cmds if c["t"] in ("say", "nar"))
    print(f"{len(cmds)} commands, {n_say} spoken + {n_nar} narration lines, ~{words} words, {len(voice)} voiced")
    print("sprites used:", sorted({c["spr"] for c in cmds if c["t"] == "show"}))
    print("bg/cg used:", sorted({c["name"] for c in cmds if c["t"] in ("bg", "cg") and c.get("name")}))
