"""Turn .ozs chapter scripts into the reader-visible text that cold readers get (style guide §9, step 3).

What a reader sees, and nothing more: narration, spoken English with speaker names as displayed (the compiler's
SPEAKERS table, so the dream voice shows as "???"), and [bracketed] staging for backgrounds, CGs, sprites, captions
and chapter cards. No expression tags, Japanese, line IDs or comments. CGs are named as neutral image files
(image_01.jpg, image_02.jpg, … in order of first appearance; Oct 18: a reader saw "cg_natsuki_intro_falter" in a folder
listing and knew a falter was coming), so the readers
can be handed JPG copies.

Translator's notes (notes.txt next to the first source): a reader in the game can tap a noted term, so the first
time a noted term appears, its note follows the line in brackets.

Split points: by default one part per scene. Pass --split scene_a,scene_b,... to start a new part at those scenes
(the Oct 17 Ch1 cold read split at prologue | c1_morning | c1_intro | c1_interlude).

Usage: python3 reader_view.py OUT_DIR src1.ozs [src2.ozs ...] [--split ids] [--cg-dir v2/img/bg]
       With --cg-dir, every CG the script shows is copied into OUT_DIR as a JPG (1280 px long side).
"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compile_script import SPEAKERS, split_id, read_notes  # display names, kept in one place

SAY = re.compile(r'^(\w+)(?:<(\w+)>)?(?:\((\w+)\))?:\s*"(.*?)"\s*(?:\|\|.*)?$')
GLOSS = re.compile(r'\{([^|}]+)\|([^}]+)\}')


def bg_label(name):
    """bg_classroom_day -> 'classroom, day'. Good enough for staging notes; override in BG_LABELS if not."""
    if name == "black":
        return "black screen"
    if name in BG_LABELS:
        return BG_LABELS[name]
    words = name.removeprefix("bg_").split("_")
    times = {"day", "night", "evening", "morning", "dusk", "lit"}
    tail = [w for w in words if w in times]
    head = [w for w in words if w not in times]
    return " ".join(head).replace("kohei", "Kōhei's").replace("fujisawa", "the Fujisawa") + (", " + " ".join(tail) if tail else "")


BG_LABELS = {
    "bg_houses_night": "two houses side by side at night",
    "bg_houses_night_lit": "the two houses at night; an upstairs window across the gap lights up",
    "bg_river_morning": "riverside path under cherry trees, morning",
    "bg_school_entrance": "school entrance hall",
}


def convert(paths, split):
    parts, cur, cgs, alias = [], [], [], {}
    notes_path = os.path.join(os.path.dirname(os.path.abspath(paths[0])), "notes.txt")
    notes = read_notes(notes_path)[0] if os.path.exists(notes_path) else {}
    noted = set()
    for path in paths:
        for raw in open(path, encoding="utf-8"):
            s = split_id(raw.rstrip("\n"))[0]   # drop the stable line ID tag
            if not s.strip() or s.lstrip().startswith("#"):
                continue
            out = None
            if s.startswith("=="):
                sid = s[2:].split("|")[0].strip()
                if cur and (not split or sid in split):
                    parts.append(cur); cur = []
                continue
            if s.startswith(">"):
                out = s[1:].strip()
            elif s.startswith("@"):
                w = s.split(); c = w[0]
                if c == "@bg":
                    out = f"[Background: {bg_label(w[1])}]"
                elif c == "@cg":
                    if w[1] == "-":
                        out = "[Full-screen illustration ends]"
                    else:
                        alias.setdefault(w[1], f"image_{len(alias) + 1:02d}")
                        out = f"[Full-screen illustration shown: image file {alias[w[1]]}.jpg]"; cgs.append(w[1])
                elif c == "@show":
                    out = f"[{SPEAKERS.get(w[1], w[1].capitalize())} appears on screen]"
                elif c == "@card":
                    out = f"[Caption: {s[5:].strip()}]"
                elif c == "@chapter":
                    out = f"[Chapter title card: Chapter {s[8:].strip()}]"
                elif c == "@mode" and len(w) > 2:
                    out = f"[{' '.join(w[2:])}, told in third person]"
                elif c == "@anim":
                    alias.setdefault(w[1], f"image_{len(alias) + 1:02d}")
                    out = f"[A two-second animated moment plays, ending on a full-screen illustration: image file {alias[w[1]]}.jpg]"; cgs.append(w[1])
                elif c == "@phone":
                    who = "Natsuki" if w[1] == "me" else "Chie"
                    out = f'[Text message, {who}: "{s.split(None, 2)[2] if len(w) > 2 else ""}"]'
                elif c == "@insert":
                    out = ("[Manga insert ends; back to the visual novel]" if w[1:2] == ["end"] else
                           "[Manga insert begins: the next part is a full-color comic, shown one panel at a time; lines in it are lettered on the art]")
                elif c == "@panel":
                    out = f"[Manga panel: {s[len('@panel'):].strip()}]"
                elif c == "@flash":
                    out = "[White flash]"
                elif c == "@endchapter":
                    out = f"[End of Chapter {w[1] if len(w) > 1 else ''}]".replace(" ]", "]")
            else:
                m = SAY.match(s)
                if m:
                    out = f'{SPEAKERS.get(m.group(1), m.group(1).capitalize())}: "{m.group(4)}"'
                else:
                    print("unparsed:", s, file=sys.stderr)
            if out:
                cur.append(GLOSS.sub(r"\1 (\2)", out))
                for term, _ in GLOSS.findall(out):
                    k = term.strip().lower()
                    if k in notes and k not in noted:
                        noted.add(k); cur.append(f"[Translator's note, {term.strip()}: {notes[k]}]")
    if cur:
        parts.append(cur)
    return parts, cgs, alias


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("src", nargs="+")
    ap.add_argument("--split", default="")
    ap.add_argument("--cg-dir", default="")
    ap.add_argument("--planned", default="", help="JSON {cg name: description} for CGs not drawn yet (pre-art reads)")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    parts, cgs, alias = convert(a.src, set(filter(None, a.split.split(","))))
    planned = json.load(open(a.planned, encoding="utf-8")) if a.planned else {}
    def drawn(n):
        return a.cg_dir and any(os.path.exists(os.path.join(a.cg_dir, n + e)) for e in (".webp", ".png", ".jpg"))
    for n in dict.fromkeys(cgs):   # a CG that isn't drawn yet is described in words instead
        if not drawn(n) and n in planned:
            parts = [[l.replace(f"image file {alias[n]}.jpg", f"(not drawn yet; described) {planned[n]}") for l in p] for p in parts]
    for i, p in enumerate(parts, 1):
        open(os.path.join(a.out, f"part{i}.txt"), "w", encoding="utf-8").write("\n".join(p).strip() + "\n")
    if a.cg_dir:
        from PIL import Image
        for n in dict.fromkeys(cgs):
            src = next((os.path.join(a.cg_dir, n + e) for e in (".webp", ".png", ".jpg") if os.path.exists(os.path.join(a.cg_dir, n + e))), None)
            if src:
                im = Image.open(src).convert("RGB"); im.thumbnail((1280, 1280)); im.save(os.path.join(a.out, alias[n] + ".jpg"), quality=85)
            elif n not in planned:
                print("missing CG:", n, file=sys.stderr)
    # the key stays outside the readers' folder
    json.dump(alias, open(a.out.rstrip("/") + ".cg-key.json", "w"), indent=1)
    print(f"{len(parts)} parts, {len(set(cgs))} CGs -> {a.out} (key: {a.out.rstrip('/')}.cg-key.json)")
