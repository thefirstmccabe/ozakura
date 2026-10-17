"""Lint .ozs chapter scripts against the speech sheets and the address sheet (style guide §3b–§3c, §9 step 3).

It flags things for a human or reviewer to look at; it doesn't rewrite anything. Checks:
  1. Tics: deadpan "very" in spoken English (more than 3 per chapter), and narration's "says it like", "the way you",
     "Something about" (more than 1 each per chapter).
  2. Japanese first-person pronouns per speaker (§3c), e.g. Takatsuki is 僕, Ryōsuke and Kōhei are 俺, Mio uses her name.
  3. きみ/君 from anyone but Natsuki (it's hers, for Kōhei); Kōhei's お前 right after a Natsuki line (he never says
     omae to her).
  4. Name timing (--chapter N): before Ch24 Kōhei doesn't say "Nanoha"/なのは aloud; before Ch30 he doesn't say
     "Natsuki" aloud and his narration calls her "Mizuno" (interludes are exempt; "Mizuno Natsuki" is fine).
  5. Retired forms: "Nano" as a name (なの is also a sentence ending; "Nano-chan" from Rika is fine).

Usage: python3 script_lint.py --chapter N src1.ozs [src2.ozs ...]
Exit code 1 if anything is flagged.
"""
import argparse, re, sys

SAY = re.compile(r'^(\w+)(?:<(\w+)>)?(?:\((\w+)\))?:\s*"(.*?)"\s*(?:\|\|\s*(.*))?$')
PRONOUNS = ["わたくし", "あたし", "わたし", "おれ", "ぼく", "わし", "俺", "僕", "私"]  # not うち: it hides inside こうちゃん etc.
ALLOWED_I = {
    "kohei": {"俺", "おれ"}, "nanoha": {"私", "わたし"}, "natsuki": {"私", "わたし"}, "akane": {"私", "わたし"},
    "rika": {"あたし"}, "ryosuke": {"俺", "おれ"}, "takatsuki": {"僕", "ぼく"}, "kirishima": {"俺", "おれ"},
    "emi": {"私", "わたし"}, "kazuo": {"俺", "おれ", "私"}, "genji": {"わし"}, "teacher": {"私"},
    "yuzu": {"私", "わたし"}, "mio": set(), "past_natsuki": {"私", "わたし", "わたくし"}, "fairy": {"わたし", "私"},
}
NOT_PRONOUN = re.compile(r"私立|私服|私物|私鉄|私語")  # 私 inside ordinary words


def first_person(ja):
    ja = NOT_PRONOUN.sub("", ja)
    ja = re.sub(r"「[^」]*」", "", ja)  # quoting someone else (Nanoha doing Kōhei's face: 「誰かが俺と…」)
    found = []
    for p in PRONOUNS:
        if p in ja:
            found.append(p); ja = ja.replace(p, "")
    return found


def lint(paths, chapter):
    flags = []
    very, says_like, way_you, something_about = [], [], [], []
    prev_speaker = None
    interlude = False
    for path in paths:
        for n, raw in enumerate(open(path, encoding="utf-8"), 1):
            s = raw.rstrip("\n")
            if not s.strip() or s.lstrip().startswith("#"):
                continue
            where = f"{path.split('/')[-1]}:{n}"
            if s.startswith("@mode"):
                interlude = "interlude" in s
                continue
            if s.startswith("=="):
                prev_speaker = None
                continue
            if s.startswith(">"):
                t = s[1:]
                if re.search(r"\bsays it like\b", t, re.I): says_like.append(where)
                if re.search(r"\bthe way you\b", t, re.I): way_you.append(where)
                if re.search(r"\bsomething about\b", t, re.I): something_about.append(where)
                if chapter < 30 and not interlude and re.search(r"(?<!Mizuno )\bNatsuki\b", t):
                    flags.append((where, "Kōhei's narration says \"Natsuki\" before Ch30 (§3c: \"Mizuno\")"))
                continue
            m = SAY.match(s)
            if not m:
                continue
            who, en, ja = m.group(1), m.group(4), (m.group(5) or "")
            if re.search(r"\bvery\b", en, re.I): very.append(f"{where} ({who})")
            if ja and ja != "-":
                if who in ALLOWED_I:
                    for p in first_person(ja):
                        if p not in ALLOWED_I[who]:
                            flags.append((where, f"{who} uses {p} (§3c: {'her own name' if who == 'mio' else '/'.join(sorted(ALLOWED_I[who])) or '—'})"))
                if re.search(r"きみ|君(?!た)", ja) and who != "natsuki":
                    flags.append((where, f"{who} says きみ/君 (§3c: Natsuki's, for Kōhei only)"))
                if who == "kohei" and "お前" in ja and prev_speaker == "natsuki":
                    flags.append((where, "Kōhei says お前 right after Natsuki speaks (§3c: never omae to her). Check who it's addressed to"))
                if who == "kohei" and chapter < 24 and "なのは" in ja:
                    flags.append((where, "Kōhei says なのは aloud before Ch24 (§3c: omae / no name / Chibi)"))
            if who == "kohei" and chapter < 24 and re.search(r"\bNanoha\b", en):
                flags.append((where, "Kōhei says \"Nanoha\" aloud before Ch24 (§3c)"))
            if who == "kohei" and chapter < 30 and re.search(r"\bNatsuki\b", en):
                flags.append((where, "Kōhei says \"Natsuki\" aloud before Ch30 (§3c: \"Mizuno\")"))
            if re.search(r"\bNano\b(?!-cha)", en):
                flags.append((where, "\"Nano\" as a name (retired; §3c)"))
            prev_speaker = who
    if len(very) > 3:
        flags.append(("chapter", f"\"very\" in spoken lines {len(very)} times (more than 3): " + ", ".join(very)))
    for name, hits in (("says it like", says_like), ("the way you", way_you), ("Something about", something_about)):
        if len(hits) > 1:
            flags.append(("chapter", f"narration \"{name}\" {len(hits)} times (more than 1): " + ", ".join(hits)))
    return flags


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", type=int, required=True, help="story chapter number, for the name-timing rules")
    ap.add_argument("src", nargs="+")
    a = ap.parse_args()
    fl = lint(a.src, a.chapter)
    for where, msg in fl:
        print(f"{where}: {msg}")
    print(f"{len(fl)} flag(s)")
    sys.exit(1 if fl else 0)
