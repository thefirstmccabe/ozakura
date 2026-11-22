# Build review: Pilot v2 Ch2 "Kendo" (Oct 25 build), before handover

Reviewer: independent QA (style guide §9, steps 7 and 9). Scope: the whole of Ch2. No diff or snapshot regression for this run (skipped as instructed). Nothing in ROOT was edited.

**Verdict:** not ready to hand over yet. Five items are must-fix under the §9 stop rule (#1–3, #5 and #6), plus one borderline item (#4). All of them are cheap script or engine changes. #7 is an art call for the author, and #8–11 go on the backlog.
- **Backgrounds that don't match the narration:** Wednesday's date card plays over Tuesday night's restaurant; Kōhei's walk home plays over the restaurant, and his arrival home over the bridge; the interlude label appears over the bridge.
- **Insert page turns dip to black:** pages 2 and 3 are never decoded ahead of time. I confirmed that decoding them first removes the dip.
- **Empty-stage beats** before the catch animation and before the insert.
- **One ambiguous "she"** read with the wrong girl on stage.
- **Laugh and surprised faces held for 7–9 lines.**
- **The debana-kote panel reads as a blade clash** more than a wrist hit.

Voices, face windows, sprite heights, tints, fast tapping, the CG exit and the end of the chapter all check out.

**Test conditions (please read).** This machine was shared with other jobs during the run: load average 6–32 on 2 cores, one test browser was killed for memory, the disk filled once, and the local server hit its time limit once. Because of that, `qa_play.py` had to be run more than once; the report used is from the clean final run (§ "qa_play report" below). Paint and transition *timings* here are slower than on any iPad. I judged transitions by their code path plus recorded video frames, re-timed the key ones when the load was lower, and give the durations only as upper bounds. Google Fonts is blocked by this sandbox's proxy (one `ERR_TUNNEL_CONNECTION_FAILED` per page load), so screenshots use fallback fonts. That's an environment issue, not a build issue. Nothing here can test Safari or listen by ear.

Screenshots and evidence: `/tmp/claude-0/-home-claude/8a181b96-a746-50e6-b79a-45dd7696162d/scratchpad/score2/runs/b2-ch2-oct25/shots/` (paths below are relative to it). The test scripts I wrote (replay with video and layer sampling, the expected-state checker, voice playback, insert decode timing) are in `…/runs/b2-ch2-oct25/work/`.

---

## Problems, most important first

### 1. "Wednesday, April 9" card plays over Tuesday night's restaurant; the walk home happens in the restaurant (must-fix)
- **Repro:** any size and speed. Play from `c2_0055` through `c2_0059`.
- **What happens:** `c2_0056` "I walk home up the hill", `c2_0057` (the bridge, the rough throat) and `c2_0299` (the container on the kitchen table, "Again.") all play over `bg_restaurant_night`. Then `c2_dojo` runs `@card` *before* `@bg bg_dojo`, so the Wednesday card sits on top of the lit restaurant. The dojo only starts to cross-fade in after the card, under the first dojo line (`c2_0059`), which begins typing over the restaurant. Evidence: `s_card.png` (card over the restaurant; first dojo letters over the restaurant), `qa_prev_jpg/315_c2_dojo_start.jpg` (the dojo still mid-dissolve under the first line).
- **Fix (ch02.ozs, staging only):** add `@bg black` (or a night exterior or kitchen) before `c2_0056`. In `c2_dojo`, put `@bg bg_dojo` (or `@bg black`) *above* `@card Wednesday, April 9`, so the card plays over black or the dojo and the first line starts after the cross-fade.

### 2. The window line plays over the bridge, and the interlude label appears over Kōhei's bridge (must-fix)
- **Repro:** any size. `c2_bridge` → `c2_interlude`.
- **What happens:** `c2_0301` "When I get to the house, the light's on in Nanoha's window across the gap." and `c2_0251` "It's only trash bags." play over `bg_bridge_dusk`. The build already has the lit-window night plate (`bg_houses_night_lit`, made with `gap_glow.py`), which is exactly this shot. Then `c2_interlude` runs `@mode interlude` *before* `@bg bg_natsuki_apartment_night`, so "— Interlude: Natsuki —" and the vignette come up over the bridge, and the first interlude line starts during the cross-fade. Evidence: `s_inter.png`.
- **Fix:** add `@bg bg_houses_night_lit` before `c2_0301`. In `c2_interlude`, put `@bg bg_natsuki_apartment_night` before `@mode interlude …`, or fade through black for the POV switch.

### 3. Insert page turns dip to black: pages 2 and 3 are never pre-decoded (must-fix: the fix is verified and small)
- **Where:** `c2_match`, the `ins_match` insert, at the turn to page 2 (the debana-kote: "Kote-e-e!" / "Kote ari!") and the turn to page 3 ("Dō-o-o!").
- **Repro:** iPad landscape 1180×820, normal taps.
  - **At moderate load:** I took a screenshot every ~0.1 s after the tap and measured each frame's mean brightness. Page 1 reads at about 80 and the black ink background at under 20. At the turn to page 2, brightness dropped 95 → 47 → 23 → 18 between 0.3 and 0.7 s, and the page appeared at 0.8 s. At the turn to page 3 it dipped to 33 at about 0.45 s.
  - **Under the heavy load earlier:** page 2 stayed black for three taps (about 7.5 s) and page 3 for one, while the DOM said the page was `on`, opacity 1 and `complete`, so the image had loaded but hadn't been decoded for painting. Evidence: `s_insert_steps.png` (steps 05–07 and 11 are black), `s_insmid.png`.
- **Cause (code):** `insertStart` awaits `decode()` only for page 1 (`im0.decode()`). Pages 2 and 3 sit invisible with `decoding='async'`, so they're only decoded when they start to cross-fade in, while the old page is already fading out. Each page is 3200×4544 (14.5 MP, about 58 MB decoded). The look-ahead preloader does `new Image()` for insert pages but never calls `decode()`.
- **Fix:** decode every page up front: `pages.forEach(p => p.querySelector('img').decode())` in `insertStart`, plus `i.decode()` in the preloader. I tested this by running exactly that once page 1 had opened: both page turns then went straight from page to page with no dip (brightness 93 → 78 → 81). Optionally, in `insRender`, hold the old page until the new page's decode resolves. Smaller page masters (about 2400 px wide is enough for the iPad zooms) would also cut decode time and memory.
- **On iPad:** expect a short dark dip at each page turn, which lands on the chapter's key beat. The code gap is certain and the fix is one line.

### 4. Empty stage, with no text box, before the catch animation and before the insert (borderline; fix it in the same pass as #3)
- **Catch (`c2_mop`, the tap after `c2_0186` "Her heel goes out from under her…"):**
  - The script runs `@hide natsuki` and then `@anim cg_catch`. `playAnim` hides the text box and only fades the video in on its `playing` event. Until then the reader sees the empty evening dojo, with no Natsuki and no text.
  - Measured at moderate load on a first play: about 0.35 s of empty room (from 246 to 589 ms after the tap); the video was up at 652 ms. Under heavy load it was 0.9–2.4 s. On replays, once the video was cached, there was no gap.
  - It's brief, but it's a dead beat at the moment of the fall.
  - The animation then opens on a room that doesn't match (see #8). The engine already guards the *end* of the animation against "the empty room" (the comment in `playAnim`) but not the start. Evidence: `s_anim_start.png`.
  - **Fix:** drop `@hide natsuki` before `@anim`. Have `playAnim` hide on-stage sprites in `animV.onplaying`, so the surprised sprite holds until the video covers it.
- **Insert (`c2_match`, the tap after `c2_0138` "We bow. We step in. We crouch at the line…"):**
  - The box hides and the empty dojo shows until page 1 finishes decoding: 0.7–0.9 s at moderate load, and 5.5–6 s under heavy load. Evidence: `s_insin.png`.
  - **Fix:** decode page 1 in the look-ahead preloader (part of the #3 fix), so the await in `insertStart` resolves at once.

### 5. `c2_0090` "she" reads as Rika (must-fix, staging)
- **Repro:** any size. `c2_lesson`, line `c2_0090` "Two minutes later she's wiped the practice schedule off the whiteboard…, borrowed a pair of glasses…, and picked up a shinai to point with."
- **What happens:** Rika has just spoken and is alone on stage (`rika school_grin l`). Natsuki's teach sprite only appears on the next line, already in the glasses. A reader takes "she" as Rika, then has to re-read. Evidence: `qa_prev_jpg/343_c2_0090.jpg` and `qa_e.png`.
- **Fix:** move `@show natsuki teach_smile c` above `c2_0090`. If wording is preferred instead, "Two minutes later Mizuno's wiped…" (a dialogue item for the Story thread).

### 6. Big expressions held long past their beat (must-fix: cheap, and a reader sees it)
Style guide §3 (Oct 24) says a punchline face plays its line, and at most the answer, then goes back to a warm face. That rule names deadpan and smirk, and `script_lint.py` check 6 only looks for those two. The same problem shows up here with laugh and surprised faces:
- **Natsuki `school_laugh` (eyes shut, open-mouthed laugh), `c2_0042` → `c2_0049`, 8 lines.** It's still on screen for the quiet beat `c2_0046` "She doesn't ask why a second-year works three shifts a week… Then they get careful with me." Evidence: `qa_b.png`, `qa_c.png`, `qa_prev_jpg/302_c2_0046.jpg`. Fix: `@show natsuki school_smile` at `c2_0044` (after "Don't start.").
- **Natsuki `kendo_laugh`, `c2_0167` → `c2_0172`, 7 lines.** She is still laughing while Takatsuki says "you laughed inside your men after the point. That was the part of zanshin you left out" (`c2_0300`), and through his note on Kōhei's dō. Evidence: `qa_holds.png`. Fix: `natsuki<blush>` (or `smile`) at `c2_0300`.
- **Rika `school_surprised` (open mouth, wide eyes), `c2_0113` → `c2_0121`, 9 lines.** It's held through Takatsuki's "hardest thing in kendo" and the calm kamae demonstration. Evidence: `qa_e.png` (`c2_0115`, `c2_0118`). Fix: `rika<grin>` or `rika<scheme>` at `c2_0115`.
- Smaller instances (author's taste): Natsuki `kendo_surprised` held `c2_0154` → `c2_0158`, through Kirishima's note to Kōhei.
- **Suggestion for Planning:** widen lint check 6 to `laugh` and `surprised` (for example, flag anything held more than 3 lines).

### 7. The debana-kote panel reads as a blade clash more than a wrist hit (text/art mismatch; the author's call on cost)
- **Where:** `ins_match` page 2, panel 1 (`c2_0142` "Kote-e-e!"). The script's panel brief says "her strike lands on his right wrist as his arms come up." Takatsuki later says "you were on his wrist the moment he lifted."
- **What the art shows:** Kōhei's arms are extended forward at chest height, not lifting. The impact flash sits at his hands, right where the two shinai cross, so at a glance it reads as a clash of blades rather than her landing first as he starts to lift, which is the point of debana. Evidence: `qa_insert.png` (step 05), `assets/page2.png`. It isn't wrong enough to stop handover, but it's the chapter's central technique.
- **Fix, if wanted:** regenerate that one panel with Kōhei's hands just starting to rise and her tip clearly on his right forearm or wrist, and paste it in with `region_composite.py`. (Trivial, for the same pass: Kōhei's grille in the close-up on page 2 has no vertical center bar, though Natsuki's has one.)

### 8. The catch CG's dojo doesn't match `bg_dojo_evening` (backlog)
`cg_catch` has plain plank walls, low barred windows along the floor, a bucket and a wet cloth. `bg_dojo_evening`, shown just before and just after, has the kamidana wall and armor racks, and no bucket. It could pass as another wall of the same room, but at the bg → animation → bg changes it reads as a different room. That's worse with the empty beat in #4. Evidence: `s_dojos.png`, `s_cg_exit.png`. Fix only if the CG is redone; otherwise a cheap patch is to add the bucket and cloth to a `bg_dojo_evening` variant for `c2_mop`.

### 9. Every kendo sprite holds a shinai (backlog)
Natsuki holds a shinai during "Hand me a rag" and the zōkin race (`c2_0176`–`c2_0181`), and in `kendo_tears` while the narration says she's "wiping her face with her sleeve" (`c2_0197`). It's a sprite-set limitation. Add an empty-handed kendo pose the next time the set is touched.

### 10. Takatsuki at `r` is cut by the right edge at iPad size (backlog)
At 1180×820, his raised elbow and the shinai tip leave the frame in `c2_0062`–`c2_0066`, where he's alone on stage, and in the lesson. Evidence: `crop_0062.png`. Fix: use `rc` when he's alone, or nudge `POSX_W.r` from 80 to 78.

### 11. Phone landscape: the chat panel covers the interlude label (backlog, spot-check size)
At 844×390, "— Interlude: Natsuki —" is clipped to "— Interlud" behind the Chie chat panel. Evidence: `phone/c2_0271.png`, `phone/c2_0275.png`. Fix: on short screens, push the phone panel below the label, or hide the label while the phone is up.

---

## qa_play report (iPad 1180×820, `--every`)
This is the clean final run over the whole build (Prologue, Ch1 and Ch2). The report is at `/tmp/claude-0/-home-claude/8a181b96-a746-50e6-b79a-45dd7696162d/scratchpad/score2/runs/b2-ch2-oct25/qa/report.json`. To save disk, its 549 per-line screenshots were converted to 1180×820 JPEGs in `…/runs/b2-ch2-oct25/qa/jpg/`. `shots/qa_prev_jpg/` holds the Ch2 shots from an earlier, interrupted run of the same build, which are cited above.
- `errors`: one, `ERR_TUNNEL_CONNECTION_FAILED`. That's the Google Fonts stylesheet, blocked by this sandbox's proxy; it's environmental.
- `bad_requests`: none. `voice_missing`: none. Every voiced line decodes: 315 of 318 spoken lines are voiced, and the 3 unvoiced are intentional "…" lines, including `c2_0080` and `c2_0230`.
- `missed_lines`: none (534 line stops seen). `insert_steps_seen`: `ins_match` 13 of 13.
- In this run, with the load lower, the 900 ms-delayed insert screenshots show pages 2 and 3 painted (`shots/qa_insert.png`). That's consistent with #3 being a sub-second dip on a normal machine rather than a long blank.
- `qa_play.py` only captures frames at lines, so the bg changes, card, animation and insert openings were freeze-framed separately, from video and from timed screenshots (above).

## What I checked and found fine
- **Script build:** `v2/script.json` matches `ch02.ozs` for all 284 Ch2 lines (IDs, order, text), and `voice/ja.json` matches the voiced column for every voiced line. The insert has 10 scripted panels and 10 panel boxes across 3 pages (13 steps). Panel order runs right to left per §4a, and the panels' lines are logged to the backlog.
- **Voices:** 152 voiced lines (the two unvoiced "…" lines, `c2_0080` and `c2_0230`, are deliberate). Every one is in `voice/index.json`.
  - `voice_levels.py` ran over all 315 lines in the build: median speech RMS −20.4 dB, range −27.0 to −19.5 dB. It raised only two flags, `p_0007` (−5.9 dB) and `p_0010` (−6.6 dB). Those are the prologue dream lines §9 already names, to be judged by ear for intended softness. All Ch2 lines are within ±3 dB, with no clipping and no clip under 0.25 s or mostly silent.
  - Clip lengths are consistent with line length: no outliers that would suggest a wrong cut.
  - In the engine, every one of the 145 text-box voiced lines started playing when reached (`voicePlaying` plus the voice meter), and all 7 insert lines played on their panels.
- **Face windows (§3a):**
  - Kōhei has a window on every spoken line, with the right outfit set (work apron at the restaurant, kendo at the dojo and the mop scene, school at the bridge) and expressions that fit the lines (deadpan "It stays tied.", surprised "…Mizuno?", flustered "…No.").
  - Kirishima's three off-stage lines in the lesson get his window.
  - There's no window for the manager or the classmates, none for Natsuki inside the catch CG (`c2_0196`), and none inside the insert.
  - Natsuki's interlude line gets her window (rule 3), and the texts use the chat UI.
  - Verified at every settled line in a full normal-speed playthrough, plus targeted re-checks.
- **Sprite heights (measured from element geometry and each sprite's top opaque row):** head tops land at Kirishima 5′11″, Takatsuki 5′8″, Natsuki 5′3″ and Rika 5′1″, matching §2 and the engine's table. Natsuki's kendo and teach sprites (which have headroom) agree with each other: the ponytail tuft sits about 1 inch above the crown in both.
- **Night and evening tints:** `bg_dojo_evening` and `bg_bridge_dusk` filters are applied to the sprites. The restaurant at night (lit interior) is untinted and reads fine. The interlude vignette comes on and goes off.
- **Transitions (freeze-frames from recorded video):**
  - Scene changes cross-fade, with no hard cuts seen.
  - The CG exit (`@cg -` → `kendo_tears`) is a 1 s dissolve with the text box up the whole time, so the Oct 17 regression where the text box went missing during CG changes doesn't recur. The box sits above the CG layer.
  - At the animation → held CG swap, the video's last frame matches `cg_catch` (no pixel differs by more than 40/255), so the swap is invisible.
  - The chapter card ("CHAPTER 2 / Kendo / 第二話") plays over black.
  - The chapter ends with a slow fade to black, then "END OF CHAPTER 2 · To be continued · Chapter 3, 'Windows,' comes next."
- **Fast tapping (553 taps through the whole chapter, median 0.15 s apart, iPad size):**
  - Nothing got stuck, no line was skipped (every Ch2 line appeared), and the run reached the end card.
  - The catch animation ignores taps until it has been up for 600 ms, then ends cleanly on the CG with the text box back.
  - Insert taps step panel by panel, and card taps behave.
  - No console errors apart from the blocked font request.
- **Phone landscape 844×390 and desktop 1440×900 (every Ch2 scene start, plus the 3-sprite lines, the face-window line, the catch CG and the chat):** the layout holds, text fits the box with no overflow, the three-character dojo and lesson shots fit, and the chat is readable. Desktop is clean.
- **Address and pronouns (spot check of the voiced Japanese against §3c, not a full Japanese pass):** Natsuki uses *kimi* to Kōhei; Takatsuki uses *boku*, surnames and no "you"; Rika uses *atashi*; members call Kirishima "Captain" (主将); Kirishima uses bare surnames. Natsuki says "Takatsuki-kun" and Rika says "Nacchan".

## Not covered
- The snapshot diff (no baseline for this run).
- Safari, iPad hardware, and listening by ear.
- On-model checks of the sprites beyond what the staging check needed.
