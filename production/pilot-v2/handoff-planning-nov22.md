# Handoff to Planning (with items for Story and Production): process review, Nov 22

**Status (Nov 25):** §9 steps 1 (Story, Nov 25) and 2 (Planning, Nov 22) are done; the §4.6 rules are in canon §6 and the chapter map. Next is Planning's step 3.

From a review thread on Nov 22. The author asked for an analysis of the whole production process, answered ten questions, and approved the plan below ("Let's do it"). This thread changed no canon, outline, script, prompt or process doc. It wrote this file and a log row.

**Marking:** "Decided" means the author said it on Nov 22. Everything else is this thread's proposal, approved as a plan; the details (names, thresholds, file locations) are **[P]** and Planning's to settle.

---

## 1. What the author decided (Nov 22)
1. **Priorities:** higher quality first, even if slower; then less of his review time. He wants more iteration toward great writing before a chapter reaches him, and as much as possible running without him.
2. **Agent time and usage are not the constraint** ("the agents taking a long time is fine with me"). He doesn't want to be wasteful with it either.
3. **Where Ch1–3 fall short, in his words:** mostly there, with small misses that reach him; and it sometimes explains too much or tries too hard (on the nose, edgy, clue-heavy). He can't judge memorability, character appeal or scene pull on his own work, and relies on the readers for those.
4. **Readers** stand in for fans with his taste, weighted most (Blue Box, Muv-Luv, *The Fragrant Flower Blooms with Dignity*, Steins;Gate), while the story stays accessible to a wider manga and VN audience. Their perfect recall of earlier chapters isn't helpful.
5. **Blind A/B picks:** he'll try them (two or three versions of a short scene, in the engine, existing art, no voices), and wants his picks checked against what he says he likes.
6. **In-game flagging:** he'd love to flag a line inside the game while playing and speak the note, instead of chatting each item to a thread.
7. **His reversals** come mostly from thinking or talking a decision over, also from playing the build and from coming back fresh. Plot decisions are hard because he can't see the downstream consequences, because both options are often good, and because it takes a few passes.
8. **Threads:** renaming them is enough for now (list in §8). He asked for suggestions on the rest of the thread setup and on the outline gate; the suggestions in §5–§6 are what he then approved as part of the plan.
9. **Reader targets: where the rules live** (§4.6). He asked whether the percentage and balance rules are still needed, heard this thread's view, and made it the decision ("let's just make that the decision"). It refines his Nov 1 evening decision; it doesn't replace it. **For Story:** canon §5 and the chapter map, together with the Nov 1 handoff.

**Open, raised by the author:** whether to run more of the project on Fable 5.2 (§4.5).

## 2. What the review found
- **Production isn't the bottleneck.** Ch3 was built in about four hours unattended on Nov 1 and waited until Nov 21 for review. Three of 44 chapters are at or near approval after about seven weeks.
- **Changes reaching back into approved chapters are the main rework:** Natsuki's look (Oct 20, Oct 24) and voice (Oct 24, Oct 25, Oct 28), the gloss rule (Oct 19, Oct 25, Oct 25 evening, Oct 28), the reader targets (Oct 17, Oct 18 three times, Oct 25, Nov 1, Nov 1 evening), the cold open (in, out, in, replaced), Ryōsuke (renamed and re-voiced Nov 1, cut Nov 21).
- **Every check hunts for faults.** Continuity, lint, diagnosis, rewrite, overcorrection and the cold readers all remove problems from one draft. Nothing generates alternatives or selects for what's good.
- **The writing instructions are mostly prohibitions** (each dialogue brief's "rules that bite", §3b's "Never" column and tics list), with almost no positive examples of the target.
- **The harness has never been scored against the author.** About 60 punch-list items exist for Ch1–3; nobody has counted how many the reviewers would have caught.
- **The cold readers read Ch1–3 in one sitting with perfect recall,** so they never flagged the callbacks that needed memory (his Nov 21 items 5–7). They read text, not the screen, so they couldn't see a text box over a face (item 4) or three cream cardigans (item 12).
- **All 383 co-authored commits are Opus 5.5.** Writer, reviewers and readers have been the same model throughout.
- **Handoffs wait for the author to open the right thread.** See §7 for what is unprocessed today.

## 3. Step one: score the harness against the author (Planning)
Before changing any prompt, build the baseline.
- **Ground truth:** every author item in `reviews/ch1/punch-oct19.md`, `punch-oct20.md`, `punch-oct24.md`; `reviews/ch2/punch-oct25.md`, `punch-oct25b.md`, `punch-oct28.md`, `punch-oct28b.md`, `punch-oct31.md`; `reviews/ch3/punch-nov21.md`; plus the Oct 17 round recorded only in the production log (10-17 rows). Tag each item by kind [P]: unclear referent or meaning; explains itself or on the nose; tone (edgy, brooding); callback that needs memory; untranslated term; staging or art against text; character look or voice; engine or layout; story decision. Mark which a text or screen reader could in principle have caught.
- **As handed over** (the builds he was reacting to; verify before use): Ch1 `54bf849` (Oct 18 revision); Ch2 `c2d2f5d` (Oct 25, before the first punch batch); Ch3 `3b6f495` (Nov 2, the state he played on Nov 21).
- **Score:** run the current reviewers and readers on those builds and count the author items they raise. Then score every new reader, judge or prompt the same way. A change is kept only if the count goes up without burying it in false alarms (report both).
- This needs nothing from the author.

## 4. The writing harness (Planning; tools built as on Oct 17)
### 4.1 Readers
- **Lossy memory.** A reader gets the new chapter plus only their own notes from the previous sitting. One reader per round comes back cold after a gap, with a two-line recap at most.
- **Ask what the author can't judge:** who they like and why; a line they'd repeat to someone; where they skimmed; whether they want the next scene; what confused them. The three percentages are asked at arc ends only (author, Nov 1 evening).
- **A confusion reader** whose only job is to flag every line where a referent or meaning is unclear.
- **Readers see the screen.** `reader_view.py` gives them screenshots at the lines (the text box over the art, the sprites on stage), not only CG copies.
- **Personas:** the author's taste weighted most; one wider-audience reader as the accessibility check.
- **Model mix:** at least one reader and the judge on a different model from the writer.

### 4.2 From correction to selection
- **Examples before prohibitions.** The drafting brief leads with scenes the author approved or praised, each annotated for why it works: Ch3's steps (3.4, "really nicely done"), the Chie texts, Ch2's Wednesday-morning kitchen, and his Oct 8 likes (pilot-notes §7). Hard rules that a script can check move into `script_lint.py`; the brief keeps only the few that need judgment.
- **Several drafts of each key scene** [P: three], written from different angles, compared blind in pairs by the judge and the readers; the winner goes on to the existing polish steps.
- **A narration pass.** His repeat flags are in narration (c3_0080, c3_0351, c2_0278–0279, "It was fine."), and the Oct 31 fresh-read chat found the same thing in Ch2's interlude in one pass. Today's diagnosis and rewrite prompts are aimed at dialogue.

### 4.3 A taste judge
- Built from three sources: the punch lists (what he rejects), his stated likes, and his A/B picks.
- Checked against all three. **Where what he says and what he picks disagree, show him the disagreement** (his request); don't quietly choose one.

### 4.4 The author's A/B
- Two or three versions of one short scene, playable in the engine with existing art and no voices, one tap to pick. About ten minutes on his iPad; three or four sessions in total [P]. Plain web pages on the site (style guide §8).

### 4.5 Models
- Test Fable 5.2 against Opus 5.5 as the writer inside the first A/B, blind, instead of assuming.

### 4.6 Reader targets: where the rules live (Decided, author, Nov 22)
The author asked on Nov 22 whether the percentage and balance rules are still needed, and adopted this thread's answer as the decision. Story writes it into canon §5 and the chapter map with the Nov 1 handoff; Planning writes it into style guide §9 and the cold-reader prompt. The Nov 1 principle (take chances), the three writing rules and the four tripwires all stand; this says where each is enforced:
- **Invariants, kept hard:** nothing confirms the dream woman before the bloom; the ending isn't settled before he chooses. Checked against the clue ledger and by readers at arc ends.
- **Budgets, set in the arc outline:** which chapters belong to which girl, how many uncanny beats each gets, how much present-day closeness Natsuki gets. The scene writer never sees a percentage.
- **Measurements, read as direction:** the three numbers at arc ends. Three readers are too few for a threshold.
- **Two changes to the Nov 1 version:** the three writing rules move from the drafting brief to the outline check (Story checks the arc outline against them; the scene writer isn't given them); "never both girls' uncanny moments in one chapter" becomes a default with exceptions named in the arc outline (the bloom involves both by design).
- **For Ch4,** whose outline was approved Oct 24 under the old rules: Story checks it against the three rules once, as part of folding in the Nov 1 handoff.
- **The number to watch:** Natsuki's support near 40% or better (canon §5, Oct 21).

### 4.7 Humor (author, Nov 24; the prompt and harness details are this thread's proposal [P])
**Author:** the story needs humor: "If the characters don't talk to each other in humorous ways at times all the dialogue will be unnatural." What fails is the execution: the attempts are "flat or too dry, or too much time is spent for them for the level of the joke," sometimes so dry he can't tell a joke was meant. His example: Ch1's extended bit where Nanoha theorizes that the school conspires to keep them in the same class "didn't work at all. It was just flat"; the current "Rika-chan counts as several" is "more natural." Such a bit "might have worked if it went all in with a full-on manga cutscene in a wacky different art style." No comedic voice acting is needed, and it probably can't be achieved; use the visuals more (and CGs far more than a traditional VN would).

**Why it happens (review thread):** §3b prescribes the dry, extended kind (Nanoha: "committed deadpan bits and elaborate straight-faced theories"); the text is English and the voice Japanese, so a deadpan line has no delivery; and nothing weighs a joke's length against its payoff.

**Proposal [P]:**
- **Prompt:** a joke gets one line and at most one reply; anything longer has to escalate or reveal character. Humor comes mainly from situation and reaction (teasing, a quick comeback, someone flustered, the reader knowing more than a character). Revisit §3b's humor column with Story.
- **Legibility:** someone on screen reacts (a laugh, a groan, a retort), or the sprite does.
- **Harness:** the writer tags each line it means as humor. Readers mark what they took as a joke and whether it landed. Report three things: jokes nobody noticed, jokes noticed that fell flat, and lines spent per joke. A joke that misses is cut, not polished.
- **Score:** add "failed joke" as a kind when tagging his Ch1–3 items; some filed as "on the nose" or flat are probably this (the baseline caught none of the flat lines).
- **His A/B:** one scene done with one-liners, with situation and reaction, and as an extended bit.
- **Visual gags (with a design pass):** one simple gag style for comic inserts and reaction panels. The cost rule applies to pictures too: full gag inserts a few times an arc, small reaction panels often.
- **Positive examples are scarce:** so far only "Rika-chan counts as several." The author has been asked for two or three more.

## 5. Story decisions (Story)
- **Fold in the Nov 1 and Nov 21 handoffs first** (§7). Ch4 shouldn't start on the old rules.
- **A consequence trace before a plot decision is committed:** every chapter-map row, clue-ledger entry, planned address shift and built line the change touches, as a short list the author sees at decision time.
- **A settling period** [P: a few days] before a plot decision is applied to approved chapters.
- **One batch of backward changes per arc,** not one per decision.
- **The outline gate (approved as suggested):** one page per arc with the turning points, what changes between the three leads, and anything touching an Open item; plus a short list of inventions he'd want to know about (a new character, a new recurring device, anything that shifts a relationship). Story fills in the scenes. Readers stress-test the arc page before anything is built.
- **Still waiting:** the chapter map's header has marked it a Proposal since Oct 18.

## 6. Handover, review and threads
- **How far ahead production runs (approved as suggested):** Ch4 as now. For Ch5–8, build the arc but hand over Ch5 as soon as it's done while 6–8 continue. Move to one handover per arc once it's earned [P tests]: the harness catches about two-thirds of his Ch1–3 items in the §3 score, and his punch list on a new chapter is short with no new rules in it. Not continuous building: the spine has grown from 40 to 44 and plot decisions are still moving.
- **In-game flag (Production):** a button that records the line ID and the screen, takes a note, lets reading continue, and at the end exports the whole list in the punch-file format. For speech, start with the note field and the iPad keyboard's dictation key; test Safari's in-page speech recognition on his iPad before offering one-tap talk.
- **One handoff inbox (Planning)** [P: `production/handoffs/open/` and `done/`], each file headed with its owner and "needs the author: yes/no".
- **A scheduled sweep (Planning):** on evenings and weekends, inside the hours rule, pick up open handoffs that need no author decision; apply, run one independent check, log, archive. Confirm first that a scheduled session can get push access to this repo.
- **One "waiting on you" list,** oldest first, each item answerable in a line. Today's list (status board) has four items; the cold-open sword grip (Oct 18) is probably moot since the Nov 21 cold open.
- **Two kinds of conversation for the author:** talking story, and playing and flagging. Whatever thread he's in files what he says for the right owner. The ownership table in `CLAUDE.md` stays.

## 7. Housekeeping
**Unprocessed handoffs (as of Nov 22):**
- `handoff-story-nov1.md` (Story and Planning): the loosened reader targets. Not in canon §5 (line 402 still reads "Decided Oct 18"), the chapter map's windows table, style guide §9 step 3, or `production/pipeline/review/cold-reader.md`. The word "tripwire" appears in none of them.
- `handoff-story-nov21-ch3.md` (Story and Planning): the camera-beat cut and the callback rule. The rule isn't in the style guide.
- `handoff-production-nov21.md` (Production): Takatsuki replaces Ryōsuke in Ch1–3; waiting for the author's go.
- Check whether `handoff-production-oct24.md`, `handoff-production-nov1.md` and `handoff-story-oct25.md` are consumed and should move to `archive/`.

**Stale spots a doc lint should catch (Planning builds the lint; owners fix):**
- Style guide: Ryōsuke in §1b's heights and full-body list, §2's table, §3a's colors and §7's cast; Sōta in §1b and §3a; **two conflicting rows in §3c** (line 243, Takatsuki → Nanoha "Tachibana"; line 246, "Tachibana-san"); §3's "Current inventory" (Oct 24 counts); §9 step 3's "windows of about 3–4 chapters… no reader is sure (70%+)".
- `production/pilot-v2/README.md`: "$40 cap… Ask before going over" (lifted Oct 24).
- `README.md`: "first week, 3 chapters".
- `story/pilot-notes.md`: "Last updated 2026-10-17".
- **Rules and history are mixed** in the style guide ("author, Oct 28; it was once per scene from Oct 25"). State the current rule only; the log and git keep the history.

**Engineering (Production):**
- **Bundle the fonts.** `v2/index.html` loads them from Google Fonts, which the test environment can't reach, so text fit has only been tested with a local copy (Ch3 handover, "Not covered").
- **Partial clones.** The working tree is about 1 GB (`production/` is 826 MB) and every thread clones all of it; `story/` is under 400 KB. Document a sparse or filtered clone per thread in `CLAUDE.md`.
- **Per-image settings out of the engine file** (`CG_FRAME`, `CG_PHONE_Y`, `VSET`, sprite heights in `v2/index.html`) into a data file, so chapter work stops editing code that approved chapters run on.

**Leave alone:** stable line IDs, regression runs against approved builds, fresh-agent checks, the two-round stop rule, the ledger.

## 8. Thread names (renamed Nov 22, at the author's request)
| Was | Now | State |
|---|---|---|
| Story bible length and pacing | Ōzakura · Story | Active |
| Visual novel project organization | Ōzakura · Planning | Active |
| Music production workflow | Ōzakura · Audio | Active |
| Ōzakura pilot v2 production | Ōzakura · Production · Ch3 | Active until Ch3 is approved |
| (new, when Ch4 starts) | Ōzakura · Production · Ch4 | — |
| Pilot v2 production punch list | Done · Production · Ch1–2 | Finished |
| Visual novel dialogue critique | Done · Ch2 interlude fresh read | Finished |
| Visual novel phone layout | Done · phone layout | Finished |
| Natsuki alternative hairstyles | Done · design · Natsuki Oct 20 | Finished |
| Love triangle promise reveal mechanics | Done · triangle discussion Oct 18 | Finished |
| visual novel production test | Done · shipped pilot | Finished |
| Manga adaptation test | Hold · Manga Vol. 1 | On hold |
| Production process improvement (this review) | Done · process review Nov 22 | Finished once Planning picks this up |

## 9. Order of work
**Story is on hold until Ch3 is done** (author, Nov 21, in the Story thread: nothing more gets committed there until then). Step 1 waits for that; steps 2–3 don't depend on it, so Planning starts now. The Story thread also holds a pending list of the author's Nov 21 changes that aren't in the repo yet (the cold open's staging, Kōhei's resentment of Takatsuki dropped, the summer legend told as a story he doesn't believe, the style guide §3c duplicate rows, corrections to `handoff-production-nov21.md` and to the 11-21 log row). Until Story commits them, treat canon §2, the scene outline's P.0 and that handoff as not final.

1. Story folds in the Nov 1 and Nov 21 handoffs (§7) and its pending list, once Ch3 is done.
2. Planning builds the §3 score and reports the baseline.
3. Planning rebuilds the readers and the judge (§4.1–§4.3), scored against the baseline.
4. The author's first A/B, including the model comparison (§4.4–§4.5).
5. Production adds the flag button and bundles the fonts (§6, §7).
6. Planning sets up the inbox, the sweep and the doc lint, and rewrites style guide §9 and the reviewer prompts to match. *(Nov 27: a request to consider moving the inbox and the sweep up is in `handoff-planning-nov27.md`.)*
7. Ch4 is produced on the new harness. Its punch list is the first live test.
