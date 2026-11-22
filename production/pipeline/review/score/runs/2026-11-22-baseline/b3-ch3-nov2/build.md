# Build review: Pilot v2 Ch3 "Windows" (whole chapter, before handover)

Reviewer: independent QA agent (did not make the build). Scope: all of Ch3 (`c3_home` to the end card). Not a fix round, so there was no diff and no snapshot regression (both skipped as instructed). Nothing in ROOT was edited.

Build: `b3-ch3-nov2/v2/`, served on :8153. Sources read: the deliverable README (build and QA), style guide §3 to §3c and §9, `production/pilot-v2/script/ch03.ozs` (plus the syntax header of `ch01.ozs`), the compiled `v2/script.json`, and the engine in `v2/index.html`.

Shots and logs are under `runs/b3-ch3-nov2/`:
- `qa/`: the `qa_play.py --every` run at iPad size.
- `qa_clean/`: a clean rerun.
- `shots/`: freeze-frames, spot checks and contact sheets.
- `tl_ipad_normal/` and `tl_ipad_fast/`: per-frame layer timelines.

## Summary

- **12 problems:**
  - 1 must-fix.
  - 3 should-fix.
  - 6 low.
  - 2 backlog.
- **Automatic checks are clean:**
  - `qa_play` saw all 784 lines, with no missed lines, no bad requests and no voice line that failed to decode.
  - Every Ch3 voiced line plays.
  - `voice_levels.py` flagged nothing in Ch3.
- **The biggest problem is on iPad, the primary screen.** In the window scene, the text box and Kōhei's face window cover the rabbit. That rabbit is the scene's centerpiece, and the narration describes parts of it that the player can't see.

---

## Must-fix

### 1. iPad: in the window CGs, the text box and Kōhei's face window hide the rabbit, so the narration describes things the player can't see

- **How to reproduce:** iPad landscape 1180×820, scene `c3_window`, lines c3_0106 to c3_0322, at any tap speed.
- **Why it happens:**
  - At iPad proportions the CG's height exactly fills the screen, so there is no vertical crop to adjust.
  - The text box covers the bottom 21% of the CG (y 650 to 806).
  - In `cg_window_sill` and `cg_window_sill_turn` the rabbit sits at the bottom-left, at roughly x 70 to 250 and y 470 to 760.
- **What the player sees:**
  - **c3_0106:** "His little tail points straight at my window." The rabbit's body and tail are under the text box. Only the ears and the head show.
  - **Kōhei's lines (c3_0107, 0111, 0115, 0117, 0123, 0125, 0433, 0435, 0128, 0313, 0322):** his face window (x 35 to 209, y 619 to 793) sits directly on the rabbit. Only the ears are left.
  - **c3_0314:** the quarter turn ("so he's facing her instead") shows only as a slight profile on the head. It is easy to miss.
  - Nanoha's folded arms are also under the box.
- **Why the other sizes are fine:**
  - Phones already have a fix (`CG_PHONE_Y` at 100%, which crops from the bottom), and at 844×390 and 844×345 the rabbit sits above the box.
  - At desktop 1440×900 the box is narrower, so the rabbit sits beside it.
  - iPad is the one target where the problem remains.
- **Screenshots:** `shots/strip_ipad_window.jpg`, `shots/ipad_rabbit_zoom.jpg`, and `qa/602_c3_0106.png` to `qa/636_c3_0322.png`. For comparison: `shots/phone_rabbit_zoom.jpg` and `shots/strip_desktop.jpg`.
- **Suggested fix:**
  - Re-export `cg_window_sill` and `cg_window_sill_turn`, and keep `cg_window` consistent with them. Outpaint wall below the window, or move the composition up and right, so that:
    - the rabbit, tail included, and the sill sit above about 75% of the frame height;
    - the rabbit sits right of about 18% of the frame width, clear of the face window.
  - Rebuild the living stills from the new frames.
  - A CSS-only option would be an iPad-only scale-up anchored at the top-right for these three CGs. It costs the right edge of the window, and it needs checking against the 35% and 100% phone crops.
  - Run the on-model check again afterward (rabbit's orientation, the bun, the scrunchie).

## Should-fix

### 2. At the sill-to-turn CG change, the new pose snaps in, then the old pose ghosts back, then the new pose settles

- **How to reproduce:** iPad 1180×820, normal tapping. Tap on c3_0313 ("…Thanks. For tonight.") to go to c3_0314.
- **What the player sees (frame capture):**
  - At about +0.25 s after the tap, the rabbit jumps almost all at once to the turned pose.
  - From about +0.3 to +0.6 s, the old back-turned ears come back as a double exposure.
  - The turned pose settles by about +1.1 s.
  - Instead of a 1 s dissolve, the moment reads as "snap, double image, settle", and it lands on the scene's punchline beat ("His sentence has been reduced").
- **Screenshots:** `shots/strip_turn_frames.jpg` (frames +218, +252, +402, +502 ms) and the raw frames in `shots/flicker_sill_turn2/`.
- **Why it happens (`liveOn`/`liveOff` in `index.html`):**
  1. On a CG-to-CG fade, `liveOff()` removes `.on`, so the `<video>` starts its 0.9 s fade-out from opacity 1.
  2. In the same call, `liveOn` points that same element at the new clip.
  3. Once the new clip's first frame decodes (about 0.25 s), the new pose shows at 57 to 85% opacity on top of the old still (z-index 4 over 2 and 3). The new still is only at 0 to 12% at that point.
  4. As the video keeps fading out, the old still underneath shows through until the new still catches up.
  - Measured with `tools/cgdip.py c3_0313`:
    - at +332 ms, the video (new clip) is at 0.57 while the new still is at 0.00;
    - at +546 ms, the video is at 0.46 while the new still is at 0.48.
- **Suggested fix:** when one living still replaces another without a cut, drop the old video instantly (`transition:none` before `liveOff()`, as the cut path already does), so the matching still underneath takes over. Then load the new clip, which fades in after `playing`. The other option is two `<video>` elements.
- **Scope:** in Ch3 only c3_0313 to c3_0314 goes from one living still straight to another. Re-run a freeze-frame of this change after the fix.

### 3. c3_0113 to c3_0118: the text says the rabbit faces Kōhei, but the CG still shows its back

- **How to reproduce:** any size, scene `c3_window`, lines c3_0113 to c3_0118.
- **What the player sees:**
  - c3_0113: "I … turn him around to face the window."
  - For the next 5 lines (Nanoha's "Kōhei.", "You are undermining my authority", and the rest), `cg_window_sill` keeps showing the rabbit's back and tail.
  - At c3_0119, "She turns him back around", which matches the CG again.
- **Suggested fix:** either
  - add a third sill state (the rabbit facing out) for c3_0113 to c3_0118, which is cheap as an edit of `cg_window_sill` that changes only the rabbit; or
  - reword c3_0113 so that Kōhei only reaches for the rabbit, which needs a Story-thread decision.

### 4. c3_0082: "your TV is bigger" contradicts the art

- **How to reproduce:** any size. c3_0082 ("We only came over here because your TV is bigger"), then c3_0406 and c3_0411 later in the same chapter.
- **What the player sees:**
  - The Fujisawas' TV in `bg_fujisawa_living_night` is a small CRT on a cart.
  - The Tachibanas' living room (`bg_tachibana_living`, `cg_lunch`) has a large flat-screen.
  - The player sees both rooms within about 15 minutes.
- **Suggested fix:**
  - If the line is meant as Nanoha's transparent fib, leave it, but the author should know it reads as an art mismatch.
  - Otherwise, a Story-thread rewording (for example, "your sofa is better"), followed by a single voice retake of c3_0082.

## Low

### 5. Akane is "asleep on the sofa" but the art shows an empty sofa and a standing Akane

- **How to reproduce:** any size, c3_0060 to c3_0088.
- **What the player sees:**
  - At c3_0060, the narration says she is asleep under a fleece blanket. The background shows the sofa empty, with the blanket folded on the arm.
  - From c3_0070 on, she stands at full height in front of that empty sofa.
  - At c3_0088, "She pulls the blanket up over her head. Conversation over." plays while her standing, winking sprite is still up. She is hidden only at c3_0089.
- **Suggested fixes:**
  - Cheap: move `@hide akane` above c3_0088.
  - Fuller: a variant of `bg_fujisawa_living_night` with a blanket-covered shape on the sofa for c3_0060 to c3_0067.

### 6. Emi's previous line stays on screen through the move indoors

- **How to reproduce:** iPad, normal speed. Tap on c3_0285.
- **What the player sees:**
  - `@bg bg_tachibana_living` and `@wait 0.9` run while the text box still shows "Tachibana Emi" and "Barging? You're saving me…".
  - This lasts about 1 to 1.5 s, over the new room, with nobody on stage.
  - Then Mio appears and her line replaces it.
- **Suggested fix:** clear the name and text, or hide the box, when a background change is followed by `@wait`. The script-only alternative is to drop the `@wait 0.9`.

### 7. Kōhei's face window shows the school blazer where the scene says he isn't wearing it

- **How to reproduce:** any size. c3_0102 to c3_0322, then c3_0344 to c3_0420.
- **What the player sees:**
  - In `c3_window`, his face windows show the blazer collar right after "I take a shower" at night.
  - In `c3_steps` through `c3_lunch` (`@wear kohei school`), he is in uniform on Saturday afternoon. Natsuki has changed into a track shirt.
- **Context:** there is no casual or home face set for Kōhei, so this is a compromise.
- **Suggested fix:** list it as a [P] compromise in the handover note, or add a home face set later. It is visible only as the collar in a small window, so it is low priority.

### 8. Small text and art nits, mostly normal VN sprite convention (one item)

**Props and poses:**
- c3_0185 to c3_0375: Nanoha is "sweeping petals", but her sprite has no broom. Genji's sprite does carry one.
- c3_0359 and c3_0365: "She lifts the camera" and "pulled the camera back against her chest with both hands". The sprite holds the camera at her waist with one hand.
- c3_0405: "Mizuno shoulders her practice bag". There is no bag.

**Text and background details:**
- c3_0099: "I open my window". `bg_kohei_room_night` has shown it open since c3_0095.
- c3_0282: "front door is already open". The doors are closed in `bg_houses_day`.
- c3_0184: "Below it, the big flat boulder". At iPad size the boulder is mostly under the text box.

None of these needs action unless the author notices them. The cheapest worthwhile fix is a broom for Nanoha, as an edit of the sprite.

### 9. The window CG's smile loops through the serious part of the conversation

- **Where:** c3_0122 to c3_0313, any size.
- **What the player sees:** Nanoha's chin-on-arms contented smile, animated as a living still, stays up through the clinic, "they still don't know what it is", Dad's pancreatic cancer, and "You're not the only person who loves her."
- **Assessment:** it can read as warmth. It can also read as her not listening. This is the author's call.
- **Possible fix:** a softer, more serious variant of the sill CG for c3_0122 to c3_0313.

### 10. Genji reads large next to Natsuki in two-shots

- **Where:** c3_0268 to c3_0394 and c3_0399 to c3_0404, at iPad size.
- **What was measured:**
  - The heights match the lineup: head tops at 57.8" against Natsuki's 63".
  - Genji's head, though, measures about 175 px tall against about 145 px for Natsuki's, at 1180×820 (1×). That is about 20% larger. For a stooped 5′2″ old man beside a 5′3″ girl, it reads a little big.
  - At the left position his sprite is clipped by the screen edge.
- **Screenshot:** `shots/genji_natsuki_heads.jpg`.
- **Suggested fix:** if the author agrees after a look, trim Genji's `h` or `v` in `CHAR` by about 5 to 8%, or give him a `VSET` entry.

## Backlog

### 11. The name tag briefly overlaps the fading face window

- **Where:** when Kōhei's line is followed by a speaker who has no face window, for example c3_0072 to c3_0073, or c3_0407 to c3_0408.
- **What happens:** the name tag jumps left at once (`withface` is removed), while Kōhei's face fades out over 0.18 s. For about 3 frames the new name tag sits over the fading face.
- **Suggested fix:** delay removing `withface` until the face's `transitionend`.

### 12. A CG-to-CG change removes the old CG on a fixed 1060 ms timer, not when the new CG has faded in

- **What was seen:**
  - The test machine was heavily loaded by other jobs (load average 20 to 30).
  - At c3_0105 to c3_0106, the new `cg_window_sill` started its fade about 950 ms late while its image decoded. The timer then removed `cg_window` while the new CG was at 0.26.
  - Kōhei's bedroom showed through at about 75% for several frames, under the text box.
  - At normal load (`tools/cgdip.py c3_0105`, 3 runs), coverage stayed at 0.98 or above. So this is unlikely on an iPad, but it is fragile.
- **Suggested fix:** start the fade and the timer after `next.decode()`, or remove the old image on the new image's `transitionend`.

---

## What I checked and found fine

**Automatic QA (`qa_play.py --every`, 1180×820, `qa/report.json`):**
- 784 lines seen out of 784; no missed lines.
- 0 bad requests; voice missing 0.
- 460 of 463 spoken lines are voiced. The 3 unvoiced lines are the intentional silent "…" lines (c1_0222, c2_0080, c2_0230).
- The match insert showed all 10 steps.
- Console errors:
  - One Google Fonts `ERR_TUNNEL_CONNECTION_FAILED`. The sandbox has no font CDN, so screenshots use fallback fonts.
  - 31 `ERR_CONNECTION_REFUSED`, caused by my local server timing out mid-run during Ch2. That was a harness problem, not the build.
- A clean rerun (`qa_clean/report.json`) has only the font error.

**Voices:**
- **`voice_levels.py`:** 460 lines, median speech level −20.4 dB, range −27.0 to −19.5 dB. Two flags, both in the prologue dream: p_0007 (−5.9 dB) and p_0010 (−6.6 dB). These are the known dream lines (§9 step 5) and still need the by-ear "intended softness" call. No Ch3 line was flagged.
- **Coverage:** all 131 spoken Ch3 lines are in `voice/index.json`. The Japanese text in `voice/ja.json` matches `ch03.ozs` exactly.
- **Packing and length:** the voice files are packed with no gaps. Clip lengths look right for the text; the 4 short-kanji outliers (c3_0093, c3_0094, c3_0355, c3_0356) check out.
- **Playback:** jumping to each of the 131 lines plays it in the engine, with signal on the voice channel (`voiceplay.json`, 131 ok, 0 failed).

**Staging against the script:**
- **Who is on screen:** matches `@show`/`@hide` throughout.
- **Name tags:** full names on every spoken line through Ch8, per §3a. For example: Tachibana Genji, Tachibana Mio, Tachibana Emi, Kirishima Aoi, Takatsuki Shō, and Fujisawa Kōhei on his own lines. The timeline check found no name-tag mismatches. The tags fit at 844×345.
- **Face windows (§3a):**
  - Kōhei has one on every spoken line: school faces, and the kendo faces at Saturday practice.
  - None appear on narration.
  - Other characters get one only when off stage or out of the CG: Natsuki at c3_0284, 0381, 0409, 0289 and 0291; Nanoha at c3_0263, 0397 and 0404.
  - No character ever had a face window and an on-stage sprite at the same time.
- **Expressions:** they match the lines. The §3 deadpan and smirk rule holds: Nanoha's deadpan at c3_0084 returns to a smile by c3_0086, and Natsuki's smirk at c3_0425 is answered once and then cleared.
- **Sprite heights:** they measure true to the lineup on one shared floor: Nanoha 4′11″, Akane 5′0″, Emi 5′2″, Natsuki 5′3″ (the ponytail adds about 1″), Takatsuki 5′8″, Kirishima 5′11″, Mio 4′0″. Head sizes are consistent across each character's outfit sets (`shots/assets/height_compare.jpg`).
- **Night tint:** applied to the sprites in `bg_fujisawa_living_night`. The bedroom night backgrounds have no sprites. `bg_houses_night` has Nanoha's upstairs window dark, as c3_0059 says.

**Locations:**
- No mirroring problems.
- The window CG's view matches the lit window seen across the gap in the bedroom background.
- The `cg_lunch` layout matches `bg_tachibana_living` (TV, garden doors, kitchen).
- The seating matches c3_0413: Grandpa on Kōhei's right, Mio between Akane and Mizuno, Nanoha by Emi, no Kazuo.
- The tree CGs match `bg_shrine_tree_day`.
- The point of light in `cg_tree_light` sits under the low branch. It is small but visible at iPad size (`shots/tree_light_zoom.jpg`).

**Transitions (per-frame computed timeline plus screenshots, iPad):**
- Chapter card, then date card, then the first line, with the background fading in from black.
- Every background change, the Saturday date card, and every sprite enter, exit and move. The c3_0311 move slides Akane left while Nanoha enters on the right.
- CG from nothing (`cg_window` slow, `cg_tree_natsuki`, `cg_tree_light`, `cg_lunch`): the box hides first, then the CG fades in, then the line.
- CG to CG with the box staying up. This is the Oct 17 z-index regression, and it is fine.
- CG to background: `@cg -` together with `bg_kohei_room_night_dark` gives "her light goes out"; the tree and lunch CGs fade out over the sprites.
- The end: fade to black, then the "END OF CHAPTER 3" card naming Ch4 as "The Light at the Shrine", which matches the chapter map.
- The only transition defects are items 2, 6, 11 and 12.

**Fast tapping:**
- At 150 ms between taps, the chapter reached the end card.
- No stuck state, no CG skipped, no text box hidden during a line, and no opacity jump flagged as a hard cut (`tl_ipad_fast/`).

**Spot checks:**
- Every scene start and the CG lines at phone 844×390 and 844×345 (`shots/spot_844x390/`, `shots/spot_844x345/`, `shots/strip_phone_cg.jpg`, `shots/strip_phone345.jpg`):
  - 16 px text, no text overflow, the box fully on screen;
  - the window CGs crop from the bottom as intended, and the cropped lunch CG is fine.
- Desktop 1440×900 (`shots/spot_1440x900/`, `shots/strip_desktop.jpg`) is fine.
- Portrait was not tested (canon §2).

**Translator's notes:** Usagi-san, torii, tamagoyaki and itadakimasu show their gloss on first use. Karaage, kinpira, onigiri, men and Chibi are later uses and show the term with note only. All of these terms have entries in `notes`.

## Test-environment caveats

- **Load:** the machine was shared with other heavy jobs, at a load average of 20 to 30 for most of the run. Timing-only anomalies were not reported unless they reproduced at lower load (about 6) or were confirmed with frame captures. Examples of what was discounted:
  - sprites or face windows arriving up to 0.5 to 1.3 s late;
  - a 1.5 s face-window hang at c3_0163.
  - Item 2 reproduced at the lower load. Item 12 did not.
- **Not covered here:** Safari, real devices, and listening by ear. `qa_phone.py` was not run because it is outside this check's scope; the phone sizes were spot-checked only.
