#!/usr/bin/env python3
"""Build the author's review page from a scene list.

    python3 production/scene-list/build_page.py story/scene-list.md out.html [--key pass1] [--tables]

The scene list is the source. This script reads it, checks its shape, writes a
single-file review page (one row per scene with Keep / Change / Cut and a note
field), and with --tables rewrites the tables between the two table markers in
the scene list itself.

Scene-list shape (see the top of story/scene-list.md):

    ## Part 1 — Spring (April–May)
    One paragraph.

    ### Ch 5 — Golden Week
    *When: late April · Whose: Natsuki · Closeness: strong · Cast: K, Na, Nt, T, A, Rika · Uncanny: Kōhei: the first eyes dream*
    **Changes:** One sentence.
    - **5.1 Title.** One line. *(Natsuki · CG · comic · P)*
      - *Your call:* The question in one line.

    ## Whole-story questions
    - **Q1.** The question. *(What I'd do: the recommendation.)*
"""
import json
import re
import sys
from pathlib import Path

FIVE = {"K": "Kōhei", "Na": "Nanoha", "Nt": "Natsuki", "T": "Takatsuki", "A": "Akane"}
SIDE = ["Rika", "Ryōsuke", "Kirishima", "Yuzu", "Chie", "Mio", "Emi", "Kazuo", "Genji", "Mom", "Fairy"]
SCREEN = ["CG", "insert", "gag", "still", "anim", "imagined"]
KNOWN_TAGS = set(SCREEN) | {"Nanoha", "Natsuki", "comic", "dread", "A+T", "family", "kendo", "uncanny", "Built", "D", "Map", "P"}
T_START, T_END = "<!-- tables:start -->", "<!-- tables:end -->"

PART = re.compile(r"^## (Part (\d+)) — (.+)$")
CHAP = re.compile(r"^### (Ch (\d+)|Epilogue) — (.+)$")
META = re.compile(r"^\*(When: .+)\*$")
CHANGES = re.compile(r"^\*\*Changes:\*\* (.+)$")
SCENE = re.compile(r"^- \*\*(\S+) (.+?)\.\*\* (.+?)(?: \*\(([^()]*)\)\*)?$")
CALL = re.compile(r"^\s+- \*Your call:\* (.+)$")
QUESTION = re.compile(r"^- \*\*(Q\d+)\.\*\* (.+?)(?: \*\(What I'd do: (.+)\)\*)?$")


def parse(text):
    data = {"parts": [], "questions": [], "side": SIDE}
    problems = []
    part = chap = scene = None
    section = "head"
    lines = text.split("\n")
    m = re.match(r"^# (.+)$", lines[0])
    data["title"] = m.group(1) if m else "Scene list"
    for n, raw in enumerate(lines[1:], start=2):
        line = raw.rstrip()
        if line.startswith(T_START):
            section = "tables"
            continue
        if line.startswith(T_END):
            section = "after"
            continue
        if section == "tables":
            continue
        if line.startswith("## "):
            m = PART.match(line)
            if m:
                part = {"id": "part" + m.group(2), "short": m.group(1), "title": line[3:], "paras": [], "chapters": []}
                data["parts"].append(part)
                chap = scene = None
                section = "part"
            elif line == "## Whole-story questions":
                section = "questions"
            else:
                section = "other"
            continue
        if section == "questions":
            m = QUESTION.match(line)
            if m:
                data["questions"].append({"id": m.group(1), "text": m.group(2), "rec": m.group(3) or ""})
            elif line.startswith("- "):
                problems.append(f"line {n}: question not in shape: {line[:60]}")
            continue
        if section != "part":
            continue
        m = CHAP.match(line)
        if m:
            label = m.group(1)
            cid = "ch" + m.group(2) if m.group(2) else "epilogue"
            chap = {"id": cid, "label": label, "title": m.group(3), "when": "", "whose": "", "closeness": "",
                    "cast": [], "uncanny": "", "changes": "", "scenes": [], "counts": {}}
            part["chapters"].append(chap)
            scene = None
            continue
        if chap is None:
            if line.strip():
                part["paras"].append(line.strip())
            continue
        m = META.match(line)
        if m:
            for bit in m.group(1).split(" · "):
                k, _, v = bit.partition(": ")
                k = k.strip().lower()
                if k == "when":
                    chap["when"] = v
                elif k == "whose":
                    chap["whose"] = v
                elif k == "closeness":
                    chap["closeness"] = v
                elif k == "uncanny":
                    chap["uncanny"] = v
                elif k == "cast":
                    for c in [x.strip() for x in v.split(",")]:
                        name = FIVE.get(c, c)
                        if name not in FIVE.values() and name not in SIDE:
                            problems.append(f"line {n}: unknown cast name {c!r}")
                        chap["cast"].append(name)
                else:
                    problems.append(f"line {n}: unknown chapter field {k!r}")
            continue
        m = CHANGES.match(line)
        if m:
            chap["changes"] = m.group(1)
            continue
        m = SCENE.match(line)
        if m:
            tags = [t.strip() for t in (m.group(4) or "").split("·") if t.strip()]
            for t in tags:
                base = "CG" if t.startswith("CG×") else t
                if base not in KNOWN_TAGS and not re.match(r"^SB\w+$", t):
                    problems.append(f"line {n}: unknown tag {t!r} on {m.group(1)}")
                if base in SCREEN:
                    k = int(t[3:]) if t.startswith("CG×") else 1
                    chap["counts"][base] = chap["counts"].get(base, 0) + k
            scene = {"id": m.group(1), "title": m.group(2), "line": m.group(3), "tags": tags, "call": ""}
            chap["scenes"].append(scene)
            continue
        m = CALL.match(raw)
        if m and scene is not None:
            scene["call"] = m.group(1)
            continue
        if line.startswith("- ") or line.startswith("  - "):
            problems.append(f"line {n}: list item not in shape: {line[:70]}")
    return data, problems


def check(data):
    problems, seen = [], set()
    for p in data["parts"]:
        if not p["paras"]:
            problems.append(f"{p['short']}: no paragraph")
        for c in p["chapters"]:
            for f in ("when", "whose", "changes"):
                if not c[f]:
                    problems.append(f"{c['label']}: no {f}")
            if not c["cast"]:
                problems.append(f"{c['label']}: no cast")
            if not c["scenes"]:
                problems.append(f"{c['label']}: no scenes")
            for s in c["scenes"]:
                if s["id"] in seen:
                    problems.append(f"duplicate scene ID {s['id']}")
                seen.add(s["id"])
                if not any(t in ("Built", "D", "Map", "P") or t.startswith("SB") for t in s["tags"]):
                    problems.append(f"{s['id']}: no source tag")
    return problems


def chapters(data):
    return [c for p in data["parts"] for c in p["chapters"]]


def md_tables(data):
    chs = chapters(data)
    out = []
    cols = list(FIVE.values()) + SIDE
    out.append("### Who is in each chapter")
    out.append("| Ch | " + " | ".join(cols) + " |")
    out.append("|---|" + "---|" * len(cols))
    for c in chs:
        out.append(f"| {c['label']} | " + " | ".join("●" if n in c["cast"] else "" for n in cols) + " |")
    out.append("")
    out.append("### The triangle, and the uncanny and dread beats")
    out.append("| Ch | Whose chapter | Natsuki and Kōhei | Uncanny or dread, and whose |")
    out.append("|---|---|---|---|")
    for c in chs:
        out.append(f"| {c['label']} | {c['whose']} | {c['closeness']} | {c['uncanny']} |")
    out.append("")
    out.append("### On screen: CGs, inserts and the rest")
    names = {"CG": "CGs", "insert": "Manga inserts", "gag": "Gag inserts", "still": "Living stills", "anim": "Animation attempts", "imagined": "Imagined scenes"}
    out.append("| Ch | " + " | ".join(names[k] for k in SCREEN) + " |")
    out.append("|---|" + "---|" * len(SCREEN))
    tot = {k: 0 for k in SCREEN}
    for c in chs:
        for k in SCREEN:
            tot[k] += c["counts"].get(k, 0)
        out.append(f"| {c['label']} | " + " | ".join(str(c["counts"].get(k, "") or "") for k in SCREEN) + " |")
    out.append("| **Total** | " + " | ".join(f"**{tot[k]}**" for k in SCREEN) + " |")
    out.append("")
    out.append("### Every scene that needs the author's call, in story order")
    calls = [(s["id"], s["call"]) for c in chs for s in c["scenes"] if s["call"]]
    if calls:
        out.append("| Scene | Question |")
        out.append("|---|---|")
        for i, q in calls:
            out.append(f"| {i} | {q} |")
    else:
        out.append("None.")
    return "\n".join(out)


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    src, dst = Path(argv[1]), Path(argv[2])
    key = argv[argv.index("--key") + 1] if "--key" in argv else "pass1"
    text = src.read_text(encoding="utf-8")
    data, problems = parse(text)
    problems += check(data)
    if "--tables" in argv:
        if T_START not in text or T_END not in text:
            problems.append("no table markers in the scene list")
        else:
            head, rest = text.split(T_START, 1)
            _, tail = rest.split(T_END, 1)
            text = head + T_START + "\n" + md_tables(data) + "\n" + T_END + tail
            src.write_text(text, encoding="utf-8")
    data["key"] = key
    data["short"] = "Ōzakura scenes"
    m = re.search(r"^\*\*Lede:\*\* (.+)$", text, re.M)
    data["lede"] = m.group(1) if m else ""
    template = (Path(__file__).parent / "page-template.html").read_text(encoding="utf-8")
    blob = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    html = template.replace("__TITLE__", data["title"].replace("&", "&amp;").replace("<", "&lt;")).replace("__DATA__", blob)
    dst.write_text(html, encoding="utf-8")
    chs = chapters(data)
    print(f"{len(data['parts'])} parts, {len(chs)} chapters, {sum(len(c['scenes']) for c in chs)} scenes, "
          f"{sum(1 for c in chs for s in c['scenes'] if s['call'])} calls, {len(data['questions'])} questions")
    for p in problems:
        print("PROBLEM:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
