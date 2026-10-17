# Handoff from the Planning thread, Oct 17 (evening)

Everything below is decided and committed (production log, 10-17 rows). Read the linked sections; don't rely on this summary alone.

## What changed today
- **Chapter production process** (`story/style-guide.md` §9), with reviewer prompts in `production/pipeline/review/` and tools in `production/pipeline/vn/` (`reader_view.py`, `script_lint.py`, `voice_levels.py`, `snapshot_diff.py`). Writing gates come before any art or voices: continuity check, lint, dialogue diagnosis/rewrite/overcorrection check, a **Japanese pass**, then three cold readers. Then on-model checks of every image, voice levels, a visual snapshot of every line with a regression diff after every fix, independent build review, and a handover note.
- **Character speech sheets** (§3b) for the whole cast, and the **address and pronoun sheet** with planned name changes (§3c). The author delegated those choices; they're decided.
- **Standing rules:** no item-by-item spend check-ins inside an approved cap (ask for a single item over about $5 or if the total would pass the cap); if Claude says something is "your call," it waits; [P] details go in the handover note and pilot-notes, the author judges them by playing, and the Story thread folds them in afterward; measure proportions on a pixel grid.
- **Ch1 cold reads** (`production/tests/oct17-dialogue-coldread/`; log 10-17): three fresh readers ended Ch1 split on who the dream woman is (none above 65%) and all guessed wife or lover. All three flagged the wrist simile, "someone you've met before?" and "Probably a stubborn crease" as heavy-handed. Nanoha's deadpan has become the house voice. The readers also caught art/text mismatches.

## Story thread
1. **Decide Ch1's reader-knowledge target** (what the reader should suspect and know by the end of Ch1), using the cold-read results, **and decide the three levers below yourself.** The author delegated these (Oct 17): make the calls, tell him what you chose and why in a few lines, log them, and pass them to Production. Don't wait for his approval.
   - **The wrist simile** ("She repeats it like she's writing it on the inside of her wrist"): keep, soften or cut. It moved all three readers toward Natsuki more than any other line.
   - **Natsuki's "Does he ever seem like… someone you've met before?"** in the interlude: keep, or make it oblique (one reader suggested she ask whether Kōhei ever hurt his left wrist).
   - **The dream voice:** currently Natsuki's actress (Zephyr) with an echo. Keep it as a clue for attentive listeners, or recast the dream so it stays ambiguous.
2. **Add a reader-knowledge target to every chapter outline from now on** (you decide these too, as part of the outline the author approves) (§9 step 1; chapter-map header note). Ch2–4 of the pilot need theirs before Production drafts them.
3. **You own §3b and §3c.** Check them against your plans. The name-change beats are in the chapter map's "Names" running thread; Ch30's beat depends on the farewell at the tree (scene bank 21a), which is still a Proposal.
4. **[P] details from the Ch1 build** (pilot-notes §3: Dad's calendar line, no Fukuda, Sendai, the collar CG, Ōno on screen) get folded into canon after the author has played them; no pre-review.

## Production thread
**A. Start now (don't depend on the Story thread):**
1. **Build items:**
   - Stable line IDs written into the `.ozs` source and honored by `compile_script.py` and the voice tools.
   - Port the panel-by-panel insert viewer into the v2 engine before the Ch2 insert. `production/insert-presentation-test/index.html` is the reference implementation, approved "don't change a thing"; spec in §4a.
   - Compose insert pages at 2× (3200 × 4544) so zoomed panels stay sharp on a Retina iPad.
   - Design every insert for panel-by-panel reading (§4a rules).
2. **Ch1 art mismatches** (log 10-17):
   - Natsuki's intro CG: hair back to shoulder length, tucked behind one ear (her locked design and the text). Check the falter variant too.
   - The collar CG text says Nanoha "has to stretch to reach," which the CG doesn't show: change the text, not the art.
   - Two of three readers saw the dream CG's cut on the back of the wrist: one edit pass so it reads clearly as the inside.
   - The four identical black-haired heads in the intro CG's foreground.
   - The Ōzakura needs one descriptive sentence in Ch1, so readers can link it to the dream's tree.
3. **Dream lines:** `voice_levels.py` measures both about 6 dB under the rest. Decide by ear whether that's intended softness.
4. **Baseline:** take `qa_play.py --every` shots of the current Ch1 build and keep them with its `script.json` as the baseline for the revision's regression diff.

**B. After the Story thread's Ch1 decisions** (it decides them itself, so this shouldn't take long):

> **ON HOLD (Oct 17, evening):** the author disagrees with these targets. He wants the past life kept more mysterious and who Kōhei ends up with kept about 50-50 until it's revealed. The Story thread revises them Monday. Don't start the Ch1 revision's writing changes (part B) until then; part A work continues.
>
> **Done Oct 17 (Story thread):** the Ch1–4 reader-knowledge targets and the Ch1 revision decisions are at the end of `production/pilot-v2/scene-outline.md`. In short: the wrist simile becomes an action (she writes 水 on the inside of her wrist); "someone you've met before?" becomes an ordinary attempt to place him; the Ōzakura's sentence goes in the interlude, at the window where Natsuki says "Oh"; the dream voice stays Zephyr with the echo plus about −1 semitone; "Probably a stubborn crease" and the river walk's snow simile go; Ryōsuke argues about taiyaki, not hot dogs. Childhood address forms for the shared-past flashbacks are in style guide §3c.
5. **Revise Ch1 under §9:** continuity check, `script_lint.py --chapter 1` (it currently flags "very" 8×, "says it like" 3×, "the way you" 2×, "Something about" 2×), then the dialogue passes on the whole chapter. `production/tests/oct17-dialogue-coldread/dialogue/scene-final.ozs` is a tested rewrite of the lunch scene (unchanged in the build since); use it as the starting point. Then the Japanese pass and three cold readers against the target.
   - The address-sheet fixes: plant "Chibi" ("Night, Chibi" / おやすみ、チビ, answering "Good night, Kō-chan"); Natsuki's えっと、きみは…… to Nanoha becomes えっと…….
   - The biggest chapter-wide wins: give Akane her own voice apart from Nanoha's; keep Natsuki's jokes off Nanoha's deadpan; cut the tics.
6. **Re-voice only changed lines,** run the regression diff and an independent review, then hand over with a short note of what changed and why. The author doesn't need to replay Ch1 unless he wants to; his review time goes to Ch2.
7. **Ch2–3 rewrites:** shipped lines to change are listed in the log (Kōhei's お前 to Natsuki becomes "Mizuno"; his なのは becomes *omae*, no name or "Chibi"; Takatsuki's 俺 becomes 僕). Emi keeps "Kōhei-kun."

**Sequencing:** Ch1's revision and then Ch2 both run under §9, so the two chapters reach the author in the same state.
