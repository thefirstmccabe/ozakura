# Cold readers (§9 step 3e)

Run **three** fresh agents with the same prompt and different personas. Build their material with `reader_view.py` (reader-visible text in parts, plus JPG copies of the CGs named `image_01.jpg`, `image_02.jpg`… so a folder listing gives nothing away; the key is written next to the folder, not in it). Give them only that folder. Never give them canon, the outline or the reader-knowledge target; compare their checkpoints against the target yourself afterward.

**Read from the start (Oct 18):** the three standing numbers are judged over windows of 3–4 chapters, so each round's fresh readers read from Ch1 through the chapter under test, in order, with checkpoints after every part. That's easy within the pilot; when the story outgrows a single read, decide how much earlier text to give them.

**Personas:** (1) a casual reader; (2) "a reader who mostly reads manga and plays a few visual novels a year, not a genre expert"; (3) "an experienced reader of romance visual novels and romcom manga (Clannad, Steins;Gate, Horimiya, Blue Box), quick to spot genre conventions."

**Prompt:**
> You are a first-time reader of an English-language visual novel (a Japanese-style school romance, translated-manga feel). You know NOTHING about the story beyond what you read here. Do not open, search or read any file except the ones listed below; do not look at any git repository, docs or other folders, even if you can find them. That would ruin the test.
>
> Folder: `{READER_DIR}`. The chapter is split into parts (`part1.txt`, `part2.txt`, …). Lines in [brackets] describe what is on screen. When a full-screen illustration is shown, open that .jpg with your Read tool and look at it as a reader would. Spoken lines are voiced in Japanese with English text; narration is unvoiced first person, except where marked as a third-person interlude. {PERSONA}
>
> Read the parts strictly in order. After each part, and before opening the next, write your checkpoint notes to `{READER_DIR}/notes-reader{N}.md`. Don't revise earlier checkpoints.
>
> At each checkpoint answer, always (canon §5, Oct 18): who do you think Kōhei ends up with, and how sure (0–100%)? Who do you want him to end up with, and how much? Who do you think the woman in the dream is, and how sure? Then: {CHECKPOINT_QUESTIONS — derived from the chapter's reader-knowledge target, phrased neutrally, e.g. "Who do you think the woman in the opening dream is? Confidence 0–100%." "What do you think the relationship is or was?"}; what you think is going on and what kind of story this is becoming; which lines, images or moments drove your guesses (quote them).
>
> After the final part, also answer: when (quote the line) you became fairly sure (70%+) of anything the checkpoints asked; any hint that felt heavy-handed, too obvious or too coy; dialogue that felt lively and up to 8 flat lines with why; with the names covered, could you tell the characters apart, and who sounds like whom; any mismatch between the text and the illustrations; would you keep reading, what hooked you, what would make you stop.
>
> Return all checkpoints exactly as you wrote them, then the final answers. Be candid; the author wants an honest cold read, not praise.

**Afterward:** tabulate each reader's checkpoints against the target, collect the flags all three share (those are the strongest), and list text/art mismatches for the on-model check.
