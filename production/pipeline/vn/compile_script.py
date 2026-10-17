"""Compile an .ozs source script (see the header of production/pilot-v2/script/ch01.ozs) into the
engine's script.json commands, plus a voice job list.

Usage: python3 compile_script.py OUT_SCRIPT_JSON OUT_VOICE_JSON src1.ozs [src2.ozs ...]
"""
import json, re, sys

SPEAKERS = {"kohei": "Kōhei", "nanoha": "Nanoha", "natsuki": "Natsuki", "akane": "Akane", "rika": "Rika",
            "ryosuke": "Ryōsuke", "teacher": "Ōno-sensei", "kirishima": "Kirishima", "takatsuki": "Takatsuki",
            "manager": "Manager", "yuzu": "Yuzu", "emi": "Emi", "mio": "Mio", "past_natsuki": "???"}
FACES = {"smile", "neutral", "grin", "deadpan", "surprised", "flustered", "annoyed", "serious", "stillness", "sad"}
SAY = re.compile(r'^(\w+)(?:<(\w+)>)?(?:\((\w+)\))?:\s*(.+?)\s*(?:\|\|\s*(.*))?$')


def compile_files(paths):
    cmds, voice, errors = [], [], []
    outfit = {}          # who -> current outfit (school, home…)
    shown = {}           # who -> current sprite name
    counters = {}
    scene = None

    def line_id(prefix):
        counters[prefix] = counters.get(prefix, 0) + 1
        return f"{prefix}_{counters[prefix]:04d}"

    for path in paths:
        for n, raw in enumerate(open(path, encoding="utf-8"), 1):
            s = raw.rstrip("\n")
            if not s.strip() or s.lstrip().startswith("#"):
                continue
            where = f"{path}:{n}"
            if s.startswith("== "):
                scene, _, title = s[3:].partition("|")
                scene = scene.strip()
                cmds.append({"t": "scene", "id": scene, "title": title.strip()})
                continue
            prefix = "p" if scene == "prologue" else scene.split("_")[0]
            if s.startswith("> "):
                cmds.append({"t": "nar", "id": line_id(prefix), "text": s[2:].strip()})
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
            lid = line_id(prefix)
            c = {"t": "say", "id": lid, "who": who, "text": text}
            if face:
                c["face"] = face
            cmds.append(c)
            if ja and ja.strip() != "-":
                voice.append({"id": lid, "who": who, "ja": ja.strip(), "en": text, "scene": scene})
            elif not ja:
                errors.append(f"{where}: spoken line without Japanese (use '|| -' for unvoiced)")
    return cmds, voice, errors


if __name__ == "__main__":
    out_script, out_voice, srcs = sys.argv[1], sys.argv[2], sys.argv[3:]
    cmds, voice, errors = compile_files(srcs)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    json.dump({"speakers": SPEAKERS, "script": cmds}, open(out_script, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    json.dump(voice, open(out_voice, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n_say = sum(c["t"] == "say" for c in cmds); n_nar = sum(c["t"] == "nar" for c in cmds)
    words = sum(len(re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", c["text"]).split()) for c in cmds if c["t"] in ("say", "nar"))
    print(f"{len(cmds)} commands, {n_say} spoken + {n_nar} narration lines, ~{words} words, {len(voice)} voiced")
    print("sprites used:", sorted({c["spr"] for c in cmds if c["t"] == "show"}))
    print("bg/cg used:", sorted({c["name"] for c in cmds if c["t"] in ("bg", "cg") and c.get("name")}))
