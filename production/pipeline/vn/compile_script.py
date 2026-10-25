"""Compile an .ozs source script (see the header of production/pilot-v2/script/ch01.ozs) into the
engine's script.json commands, plus a voice job list.

Stable line IDs (style guide §9 step 2): every narration and spoken line carries its ID at the end of the line,
after two spaces, e.g. `> I get up.  #c1_0005` or `kohei(smile): "Morning." || おはよう。  #c1_0003`. The compiler
uses the written ID, so adding or removing lines never renumbers the others (voice cuts, saves and snapshot diffs
stay keyed to the same IDs). Lines without one get the next free number for their scene's prefix;
--write-ids writes those new IDs back into the source.

Translator's notes: if a `notes.txt` (`term | note` per line) sits next to the first source, the notes for terms the
script glosses as {term|gloss} go into the output as "notes" (lowercase term -> note); the engine underlines those
terms and opens the note on a tap.

Ch2 ops (Oct 24): `@wear kohei kendo|work|school` (the outfit Kōhei's face windows show, until changed),
`@phone me|chie text` (a text message, unvoiced), `@shake`, `@anim name` (a short animated
moment: the engine plays img/anim/name.mp4 once and holds the CG `name`), and manga inserts:
`@insert name` … `@panel description` … lines … `@insert end`. Lines inside an insert belong to the current panel:
they're lettered on the page art, go to the backlog, and spoken ones are voiced when the panel opens.

Usage: python3 compile_script.py OUT_SCRIPT_JSON OUT_VOICE_JSON src1.ozs [src2.ozs ...] [--write-ids]
"""
import json, os, re, sys

SPEAKERS = {"kohei": "Kōhei", "nanoha": "Nanoha", "natsuki": "Natsuki", "akane": "Akane", "rika": "Rika",
            "ryosuke": "Ryōsuke", "teacher": "Ōno-sensei", "kirishima": "Kirishima", "takatsuki": "Takatsuki",
            "manager": "Manager", "yuzu": "Yuzu", "emi": "Emi", "mio": "Mio", "past_natsuki": "???",
            "classmate": "Classmate"}
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
    insert = None        # the open @insert command while inside one
    hold_at = {}         # command index -> file:line of each @hold, for error messages
    kohei_wear = "school"  # Kōhei's face-window outfit (@wear)
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
            # inside a manga insert, lines go to the current panel instead of the command list
            sink = cmds
            if insert is not None and not s.startswith("@"):
                if not insert["panels"]:
                    errors.append(f"{where}: line inside @insert before the first @panel"); continue
                sink = insert["panels"][-1]["lines"]
            if s.startswith("> "):
                sink.append({"t": "nar", "id": line_id(prefix, written, (path, n)), "text": s[2:].strip()})
                continue
            if s.startswith("@"):
                parts = s[1:].split()
                op, args = parts[0], parts[1:]
                if insert is not None and op not in ("panel", "insert"):
                    errors.append(f"{where}: @{op} inside @insert (only @panel and lines; close it with @insert end)")
                    continue
                if op == "insert":
                    if args and args[0] == "end":
                        if insert is None:
                            errors.append(f"{where}: @insert end without @insert")
                        elif not insert["panels"]:
                            errors.append(f"{where}: @insert {insert['name']} has no panels")
                        insert = None
                    elif insert is not None:
                        errors.append(f"{where}: @insert inside @insert")
                    else:
                        insert = {"t": "insert", "id": args[0], "name": args[0], "panels": []}
                        cmds.append(insert)
                    continue
                if op == "panel":
                    if insert is None:
                        errors.append(f"{where}: @panel outside @insert")
                    else:
                        insert["panels"].append({"desc": s[len("@panel"):].strip(), "lines": []})
                    continue
                if op == "phone":
                    who, text = (args[0] if args else ""), s[len("@phone"):].strip()[len(args[0]) if args else 0:].strip()
                    if who not in ("me", "chie") or not text:
                        errors.append(f"{where}: @phone takes me|chie and a message")
                    else:
                        cmds.append({"t": "phone", "id": line_id(prefix, written, (path, n)), "who": who, "text": text})
                    continue
                if op == "wear":   # @wear kohei kendo|work|school: which outfit Kōhei's face windows show (Ch2 on)
                    if len(args) != 2 or args[0] != "kohei":
                        errors.append(f"{where}: @wear takes 'kohei' and an outfit")
                    else:
                        kohei_wear = args[1]
                    continue
                if op == "shake":
                    cmds.append({"t": "shake"}); continue
                if op == "anim":
                    cmds.append({"t": "anim", "name": args[0]}); continue
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
                elif op == "hold":     # @hold on / @hold off: taps don't skip waits or crossfades in between (the wordless cold open)
                    arg = (args[0] if args else "on").lower()
                    if arg not in ("on", "off") or len(args) > 1:
                        errors.append(f"{where}: @hold takes 'on' or 'off', got {' '.join(args)!r}")
                    else:
                        cmds.append({"t": "hold", "on": arg == "on"})
                        hold_at[len(cmds) - 1] = where
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
            if expr and sink is not cmds:
                errors.append(f"{where}: no sprite expressions inside an insert"); expr = None
            if expr:
                if who not in shown:
                    errors.append(f"{where}: {who}<{expr}> but {who} is not on stage")
                spr = f"{who}_{outfit.get(who, 'school')}_{expr}"
                shown[who] = spr
                cmds.append({"t": "show", "who": who, "spr": spr})
            if who == "kohei" and face not in FACES and sink is cmds:
                errors.append(f"{where}: Kōhei line needs a face from {sorted(FACES)}")
            if face and who != "kohei" and sink is cmds:
                if expr:
                    errors.append(f"{where}: use either <expr> (sprite) or (face) (face window), not both")
                if who in shown:
                    errors.append(f"{where}: {who}({face}) is a face-window line, but {who} is on stage")
                face = f"{outfit.get(who, 'school')}_{face}"   # crop of that sprite expression
            lid = line_id(prefix, written, (path, n))
            c = {"t": "say", "id": lid, "who": who, "text": text}
            if face and sink is cmds:
                c["face"] = face if (who != "kohei" or kohei_wear == "school") else f"{kohei_wear}_{face}"
            sink.append(c)
            if ja and ja.strip() != "-":
                voice.append({"id": lid, "who": who, "ja": ja.strip(), "en": text, "scene": scene})
            elif not ja:
                errors.append(f"{where}: spoken line without Japanese (use '|| -' for unvoiced)")
    if insert is not None:
        errors.append(f"@insert {insert['name']} is never closed (add @insert end)")
    # a hold that never closes would swallow every tap for the rest of a first playthrough
    held = cur_scene = None
    for k, c in enumerate(cmds):
        if c["t"] == "scene" and held:
            errors.append(f"{held[1]}: @hold on in scene {held[0]} is never closed (add @hold off before the next scene)"); held = None
        if c["t"] == "scene": cur_scene = c["id"]
        if c["t"] == "hold": held = (cur_scene, hold_at.get(k, "?")) if c["on"] else None
    if held:
        errors.append(f"{held[1]}: @hold on in scene {held[0]} is never closed")
    return cmds, voice, errors, new_ids


GLOSS = re.compile(r"\{([^|}]+)\|([^}]+)\}")


def read_notes(path):
    """Translator's notes (style guide §5): `term | note` per line, '#' comments. Keys are lowercase terms."""
    notes, errors = {}, []
    for n, raw in enumerate(open(path, encoding="utf-8"), 1):
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        term, sep, note = s.partition("|")
        term, note = term.strip(), note.strip()
        if not sep or not term or not note:
            errors.append(f"{path}:{n}: expected 'term | note'")
        elif "{" in note or "}" in note:
            errors.append(f"{path}:{n}: braces aren't allowed in a note")
        elif term.lower() in notes:
            errors.append(f"{path}:{n}: duplicate note for {term!r}")
        else:
            notes[term.lower()] = note
    return notes, errors


def notes_for(cmds, notes):
    """The notes the script's glossed terms use, in first-use order, and the notes nothing uses."""
    used = {}
    for c in cmds:
        for term, _ in GLOSS.findall(c.get("text", "")):
            k = term.strip().lower()
            if k in notes and k not in used:
                used[k] = notes[k]
    return used, sorted(set(notes) - set(used))


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
    # translator's notes: notes.txt next to the first source, if there is one
    notes_path = os.path.join(os.path.dirname(os.path.abspath(srcs[0])), "notes.txt")
    used_notes, unused_notes = {}, []
    if os.path.exists(notes_path):
        notes, note_errors = read_notes(notes_path)
        errors += note_errors
        used_notes, unused_notes = notes_for(cmds, notes)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    if new_ids:
        if "--write-ids" in sys.argv:
            write_ids(new_ids); print(f"wrote {len(new_ids)} new line IDs into the source")
        else:
            print(f"note: {len(new_ids)} lines have no written ID (run with --write-ids to fix them in the source)")
    out = {"speakers": SPEAKERS, "script": cmds}
    if used_notes:
        out["notes"] = used_notes
    json.dump(out, open(out_script, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    if used_notes or unused_notes:
        print(f"translator's notes: {len(used_notes)} used ({', '.join(used_notes)})"
              + (f"; not used by these sources: {', '.join(unused_notes)}" if unused_notes else ""))
    json.dump(voice, open(out_voice, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    flat = [c for c in cmds if c["t"] != "insert"] + [x for c in cmds if c["t"] == "insert" for p in c["panels"] for x in p["lines"]]
    n_say = sum(c["t"] == "say" for c in flat); n_nar = sum(c["t"] == "nar" for c in flat)
    words = sum(len(re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", c["text"]).split()) for c in flat if c["t"] in ("say", "nar", "phone"))
    print(f"{len(cmds)} commands, {n_say} spoken + {n_nar} narration lines, ~{words} words, {len(voice)} voiced")
    print("sprites used:", sorted({c["spr"] for c in cmds if c["t"] == "show"}))
    print("bg/cg used:", sorted({c["name"] for c in cmds if c["t"] in ("bg", "cg") and c.get("name")}))
