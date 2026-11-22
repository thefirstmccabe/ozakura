"""Fill today's reviewer prompts (production/pipeline/review/*.md) for each scored build, so a scoring run uses the
current harness exactly as written, pointed at the build and the docs as they were at that commit.

One file per agent: PROMPTS_DIR/<build>/<check>.md. Launch one fresh agent per file with:
  "Your instructions are in <file>. Read it and follow it exactly."
Checks: continuity, diagnosis, reader1-3, onmodel, build (the Japanese pass is left out: the author can't read
Japanese, so none of his items can test it; rewrite and overcorrection don't flag problems).

The only change to the standard prompts is where output goes: each agent writes its full report to a file and
replies with one line, so a run of 28 agents doesn't flood the scoring thread.

Usage: python3 make_prompts.py SCRATCH_DIR   (after setup.sh SCRATCH_DIR)
"""
import json, os, re, sys

K = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.dirname(K)
S = os.path.abspath(sys.argv[1])
OUT = os.path.join(S, "prompts")
RUNS = os.path.join(S, "runs")

ENVELOPE = """**Scoring run: read this first.** You are running one standard check from this project's review harness on an
older build of the Ōzakura visual novel, as if the build were about to be handed to the author. Work only with the
files named below. ROOT is `{root}`, a checkout of the project as it was when this build was made; paths below are
relative to ROOT unless they are absolute. Do not open anything under `/home/claude/ozakura`, do not run git, and do
not look for other review reports, punch lists, logs or later versions of anything. Don't edit any file in ROOT.

**Output:** write your full report to `{out}` (create the folder if needed). When you're done, reply with one line
only: "done", plus how many problems you reported.

---

"""


def standard(name):
    return open(os.path.join(REVIEW, name), encoding="utf-8").read()


def cold_reader_parts():
    t = standard("cold-reader.md")
    personas = re.search(r"\*\*Personas:\*\* \(1\) (.*?); \(2\) (.*?); \(3\) (.*?)\n", t)
    p = [personas.group(1).strip(), personas.group(2).strip().strip('"'), personas.group(3).strip().strip('"')]
    p[0] = "You are a casual reader." if p[0].startswith("a casual") else p[0]
    p[1] = "You are " + p[1].rstrip(".") + "." if not p[1].lower().startswith("you") else p[1]
    p[2] = "You are " + p[2].rstrip(".") + "." if not p[2].lower().startswith("you") else p[2]
    quote = "\n".join(l[2:] if l.startswith("> ") else l[1:] for l in t.split("\n") if l.startswith(">"))
    return p, quote


def main():
    builds = json.load(open(os.path.join(K, "builds.json")))["builds"]
    os.makedirs(os.path.join(S, "tools"), exist_ok=True)
    import shutil; shutil.copy(os.path.join(os.path.dirname(REVIEW), "vn", "voice_levels.py"), os.path.join(S, "tools"))
    personas, reader_prompt = cold_reader_parts()
    for b in builds:
        bid, ch = b["id"], b["chapter"]
        root = os.path.join(S, bid)
        speech_root = os.path.join(S, b.get("speech_sheets_from") or bid)
        sg = "story/style-guide.md" if speech_root == root else os.path.join(speech_root, "story/style-guide.md")
        script = f"production/pilot-v2/script/ch{ch:02d}.ozs"
        earlier = [f"production/pilot-v2/script/{s}" for s in b["scripts"][:-1]]
        os.makedirs(os.path.join(OUT, bid), exist_ok=True)
        outdir = os.path.join(RUNS, bid)

        def write(check, body):
            env = ENVELOPE.format(root=root, out=os.path.join(outdir, check + ".md"))
            open(os.path.join(OUT, bid, check + ".md"), "w", encoding="utf-8").write(env + body)

        # Continuity
        t = standard("continuity.md").replace("{CHAPTER}", f"Ch{ch}") \
            .replace("`{EARLIER_SCRIPTS}`", ", ".join(f"`{e}`" for e in earlier) if earlier else "(none: this is the first chapter)") \
            .replace("`{DRAFT}`", f"`{script}`")
        if sg != "story/style-guide.md":
            t += f"\n\n(This build's own style guide has no §3b–§3c yet; read them from `{sg}`.)"
        t += "\n\nThe reader-knowledge target and the scene list are in `production/pilot-v2/scene-outline.md`."
        write("continuity", t)

        # Dialogue diagnosis (whole chapter, as in §9 step 3c)
        brief = f"`{os.path.join(S, 'briefs', bid + '.md')}`" if b.get("brief") else \
            f"the Ch{ch} scenes in `production/pilot-v2/scene-outline.md` (this build had no separate brief)"
        t = standard("dialogue-diagnosis.md").replace("`{BRIEF}`", brief).replace("`{DRAFT}`", f"`{script}` (the whole chapter)") \
            .replace("`{LINT}`", f"`{os.path.join(S, 'lint', bid + '.txt')}`")
        if sg != "story/style-guide.md":
            t = t.replace("`story/style-guide.md` §3b (speech sheets) and §3c (address)", f"`{sg}` §3b (speech sheets) and §3c (address)")
        write("diagnosis", t)

        # Cold readers
        for n in (1, 2, 3):
            rd = os.path.join(S, "readers", bid, f"r{n}")
            t = reader_prompt.replace("{READER_DIR}", rd).replace("{N}", str(n)).replace("{PERSONA}", personas[n - 1])
            t = re.sub(r"\{CHECKPOINT_QUESTIONS[^}]*\}", "what, if anything, the dream has to do with the present-day story", t)
            t = t.replace("Return all checkpoints exactly as you wrote them, then the final answers.",
                          f"Write the final answers into the same notes file, under a heading \"# Final answers\".")
            env = ENVELOPE.format(root=rd, out=os.path.join(rd, f"notes-reader{n}.md"))
            env = env.replace("ROOT is", "Your folder is").replace(
                "a checkout of the project as it was when this build was made; paths below are\nrelative to ROOT unless they are absolute.",
                "and it holds everything you may read.").replace(" Don't edit any file in ROOT.", "")
            open(os.path.join(OUT, bid, f"reader{n}.md"), "w", encoding="utf-8").write(env + t)

        # On-model check, every image the chapter shows
        t = standard("on-model-image.md").replace(
            "Check one generated image (a CG, background, sprite or manga panel) before it goes into the build.",
            f"Check every full-screen illustration (CG), animated moment and manga insert page that Ch{ch} shows, one by one, before the build goes to the author.") \
            .replace("`{IMAGE}`", f"each image named by the `@cg`, `@anim` and `@insert`/`@panel` lines in `{script}` (files under `v2/img/`)") \
            .replace("`{REFS}`", "the references the style guide names for each character (under `production/refs/`, `production/design/` and the sprites in `v2/img/ch/`) and the location plates (`v2/img/bg/`)") \
            .replace("`{LAYOUT}`", "layout sketch, if `production/pilot-v2/art/` has one") \
            .replace("`{SCRIPT_EXCERPT}`", f"in `{script}` around each image")
        t = t.replace("the deliverable's `art/prompts.md`", "`production/pilot-v2/art/prompts.md`")
        t += "\n\nReport one section per image, then a summary of every failure."
        write("onmodel", t)

        # Build review, whole chapter before handover
        port = b["port"]
        t = standard("build-review.md").replace(
            "{SCOPE: the whole chapter before handover, OR one fix round, with the diff `{DIFF}` (`git diff BASE..HEAD`) and the visual-regression output `{SNAPSHOT_DIR}` (report.txt and changed_*.jpg)}",
            f"the whole of Ch{ch} before handover (there is no diff or snapshot regression for this run; skip those steps)") \
            .replace("`{SCRIPT}`", f"`{script}`") \
            .replace("`{QA_REPORT}`", f"(make it yourself: serve the build with `python3 -m http.server {port} --directory {root}/v2` in the background, then run `python3 {root}/production/pipeline/vn/qa_play.py http://localhost:{port}/ {outdir}/qa --every` at the default iPad size; read its report)")
        t += f"\n\nThe build is `{root}/v2/`. Use port {port} only. Voice levels: `python3 {os.path.join(S, 'tools', 'voice_levels.py')}` on `{root}/v2/voice/` if it runs; if it doesn't, say so. Put screenshots under `{outdir}/shots/`."
        write("build", t)
    print("prompts in", OUT)


if __name__ == "__main__":
    main()
