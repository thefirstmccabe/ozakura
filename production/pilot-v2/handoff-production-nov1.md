# Production kickoff, Nov 1 (from the Story thread to a new Production thread)

The author is out running errands and wants this to **run start to finish without him**. Work through the three steps in order. Production log row 11-01 records the decisions behind them.

## How to run
- **Read first:** the repo's `CLAUDE.md`, then the status board (`story/production-log.md` §0), this file, then the Production thread's reading list in `CLAUDE.md`.
- **Don't stop for anything you can decide.** That covers wording inside the approved outline, [P] staging, layout values, tools, and any spend inside the limits below. Decide it, log it, and move on.
- **Stop and ask only for:** a plot beat, arc or relationship the outline doesn't settle; a single item over about $5; Ch3 passing **$15** in total; or blocked access. If one thing is blocked, park it in the log and carry on with the rest.
- **Commit and push at every checkpoint.** Workspaces get wiped.
- **Hours** follow the project instructions. After 9:30 pm, keep working, but send the author one-line notes only.
- **End with** a handover note (style guide §9) and a short message to the author covering what changed, what to play, and what's waiting on him.

## Step 1: Renames and name tags in Ch1–2
**Renames (author, Nov 1):**
- **Ryōsuke's surname is Ishida** (いしだ; was Tokiwa, ときわ). Readers confused it with Takatsuki.
- **The restaurant is Kitchen Komugi** (キッチンこむぎ; was Hoshino Kitchen). Readers confused it with Hoshikawa (Rika).

**Where the old names appear:**
- "Tokiwa" 3 times in `script/ch01.ozs` (c1_0109, c1_0110, which is voiced as ときわ, and c1_0133).
- "Hoshino" once in Ch1 and 3 times in Ch2.
- Also check `compile_script.py` (`SPEAKERS`, `SPEAKERS_FULL`), `notes.txt`, any lettered sign in the restaurant background, scene titles and the dev index.
- Re-voice every line that says either name aloud, with the same §7 voice.

**Name tags (author, Nov 1):**
- **The full name, family name first, on every spoken line through spring (Ch1–8),** Kōhei included ("all dialogue").
- From Ch9, go back to the Oct 25 rule: the full name on a character's first spoken line in each chapter only.
- Rewrite the "Name tags" rule in style guide §3. It's your section; Story only updated its example names.
- Update the compiler and the cold-reader material to match.
- Do this before step 2, so the phone pass sees the long tags.

**Already done by Story:** both renames in canon, the chapter map, pilot-notes, style guide §3b–§3c (and the example names in §3 and §7) and the scene outline. The log's history rows keep the old names.

**Regression:** run a snapshot diff of every line in Ch1 and Ch2 (style guide §9 step 10). Only the renamed lines and the tags should change. Ch1 is approved.

**Ch2:** the author called it done on Oct 31. Once steps 1 and 2 land, mark Ch1 and Ch2 approved on the board and keep the builds as the regression baseline for Ch3. This session's git proxy refuses tag pushes, so use an `approved/v2-ch2` branch, the way Ch1 did.

## Step 2: Make the phone layout work right
**Start from:** style guide §3a, "Phones" (the Oct 31 values, [P], judged by playing), and `reviews/ch2/punch-oct31.md`.

**Known issues:**
- A few lines in 1.3 and in the kendo lesson still show at the old (iPad) text size. These were parked on Oct 31 and are now in scope.
- The new full-name tags will be longer.

**Method:**
- Play Ch1 and Ch2 start to finish at these sizes, with a screenshot of every line:
  - 844×345 (iPhone Safari with its bars showing; the main target)
  - 844×390 (opened from the Home Screen)
  - the smallest supported phone (iPhone X class, about 812×375 before Safari's bars)
- Fix anything that overflows, clips, overlaps, falls back to the iPad size, or is hard to read or tap. Check all of these: the text box, name tag, face window, the controls, the text-message panel and stickers, translator's notes, menus and the save screen, the insert's panel-by-panel view, the CGs and the rotate screen, and notch clearance on both sides.
- **iPad and desktop must stay pixel-identical** (snapshot diff).
- No phone-only art and no separate phone layout (§3a).
- Leave the author a list of the changes with before-and-after shots.

## Step 3: Ch3 "Windows"
**The outline is approved** (author, Nov 1): `production/pilot-v2/scene-outline.md`, the "Ch3 — Windows" section and the "### Ch3" reader targets.

**Run style guide §9 in full:**
1. Draft.
2. The writing gates: continuity, lint, dialogue diagnosis, rewrite and overcorrection check, and the Japanese pass.
3. Three cold readers reading Ch1 through Ch3, giving three numbers at every checkpoint against the Ch3 targets. Judge them by canon §5's loosened 70% rule (one reader's spike is fine if it doesn't stick). Style guide §9 step 3 still has the old wording; Planning owns it, and canon governs.
4. Art, with an on-model check of every image.
5. Voices with the §7 cast.
6. Build and QA on iPad, desktop and phone.
7. Handover.

**Notes for Ch3:**
- **The base is the shipped Ch3** (`script.json`, the `c3_` IDs). The outline lists what to drop. Fixes 1, 2, 3, 5 and 6 matter most: no recognition at the tree, no "You're late," no near-confession, no "Next Saturday," and one-sided sparring.
- **The Saturday secret:** the author finds it a little too subtle but wants it left alone. Don't push it further. Do make sure Natsuki's Saturday line, that she asked Nanoha on Thursday, lands clearly.
- **New CG (author, Nov 1):** the lunch table, everyone saying "Itadakimasu!" over Emi's mountain of food, with steam as its living still. The other CGs are the window, in the new layout, and Natsuki's first sight of the tree.
- **Rules to keep:**
  - Kōhei is never on stage; the landing photo is described in his narration, not shown.
  - Hair color is never mentioned.
  - Kendo terms follow §5, and a term is glossed only on its first use in the whole story.
  - Texting follows §3b.
  - Use the new names.
- **Budget:** aim for about $10 and stop before passing $15. Log every spend in `ledger.md`.
- **Stop at the Ch3 handover.** Ch4 waits for the author's review.

## For reference
- **Audio:** the restaurant classmate's voice (Callirrhoe, [P]) hasn't been confirmed by the Audio thread yet. Keep it.
- **Story's Oct 31 decisions** (log 10-31): "Chibi" gets no translator's note, and Kōhei's narration doesn't go back to his Ch1 pen grip.
