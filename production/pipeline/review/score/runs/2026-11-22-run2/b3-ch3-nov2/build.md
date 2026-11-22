# Build review: Pilot v2, Chapter 3 "Windows" (pre-handover, whole chapter)

Reviewer: independent QA (fresh agent; didn't make the build). Build: `v2/` in the Nov 2 checkout, served on port 8163.
Scope: all of Ch3 (`c3_home` through the end card). No snapshot diff or diff-scoped regression this run (no baseline), per the brief.
Paths below are relative to `/tmp/claude-0/-home-claude/8a181b96-a746-50e6-b79a-45dd7696162d/scratchpad/score2/runs/b3-ch3-nov2/`, except script and build paths, which are relative to the checkout.

## Bottom line

The chapter plays cleanly. Every line shows. The voices, faces and sprites match the script. I found no script errors, no failed requests and no stuck state. Three things are worth fixing before handover. All three are cheap, and none is a playback bug:

1. **Nanoha's "your TV is bigger" (c3_0082) contradicts the art.** The Fujisawa TV is a small CRT on screen beside her, and the Tachibanas' TV, shown 150 lines later, is a big flat-screen.
2. **The night bedroom plate contradicts the narration around it (c3_0096–c3_0099).** Kōhei's casement is already open before "I open my window", and Nanoha's window is closed with the curtains drawn while the text says "her window's open, and she's waiting."
3. **Genji stands at 4′10″, not 5′2″.** `CHAR.genji.h` is 58, while style guide §1b has him at 5′2″ (stooped, [P]). Beside Natsuki he reads about 5 in shorter instead of about 1 in.

Under the §9 stop rule, items 1–3 are **must-fix**. A reader hits 1 and 2 in normal play on every screen, and 3 is an off-model height relationship. Items 4, 5 and 10 are optional polish. Items 6–9 go on the backlog / carry list.

**Test conditions (they matter for how to read the transition findings).** This machine was shared with several other review runs. For most of the session the load average stayed between 20 and 37 on 2 cores, so every timer, CSS transition and video frame ran several times slower than on an iPad, and transitions sometimes started seconds late. Near the end the load dropped to 4–8, and I re-ran the whole chapter at normal tap speed with video then; that clean run is the reference for every transition verdict below. I report a transition glitch only when I could tie it to the code or reproduce it. Glitches that appeared only once under starvation are marked as such. Google Fonts is blocked in this sandbox (`ERR_TUNNEL_CONNECTION_FAILED`, the one console error in every run), so all screenshots use fallback fonts, and the text-fit checks were measured with fallback metrics. Separately, my first local server was stopped by the session's 30-minute background limit partway through two runs. I discarded everything recorded after the outage and re-ran it: the full `qa_play.py` pass and the second half of the normal-speed replay.

---

## Problems, most important first

### 1. Text/art mismatch: "your TV is bigger" (c3_0082). Must-fix, cheap.
- **Where:** c3_home, line c3_0082, Nanoha: "We only came over here because your TV is bigger, and the surgeon is handsome." It shows at every size and tap speed.
- **What:** In `bg_fujisawa_living_night`, the Fujisawa TV is a small old CRT on a stand, sitting right next to Nanoha's sprite at stage right when she says it (see `shots/phone/844x390_c3_0082.jpg`). The Tachibana living room (`bg_tachibana_living`, from c3_0406) has a large flat-screen. A reader sees both TVs in the same chapter.
- **Fix:** Reword the excuse to something the art doesn't contradict (for example, the sofa, or Akane already being asleep on it), plus one single-line retake of the Japanese (テレビが大きい). This is a wording change inside the approved targets, so the Story thread can decide it. If the flimsy excuse is meant as the joke, the art undercuts it anyway, because the Tachibanas' TV is plainly bigger.

### 2. Text/art mismatch: the night bedroom plate (c3_0096–c3_0099). Must-fix.
- **Where:** c3_window, lines c3_0095–c3_0099, on `bg_kohei_room_night`, at all sizes (crop: `shots/art_kohei_window_open.jpg`).
- **What:** c3_0096 says "her light's on, and her window's open, and she's waiting", but the plate shows her window shut with the lit curtains drawn and nobody there. Three lines later, c3_0099 says "I open my window", but his casement is already swung open on the plate from the first line of the scene.
- **Fix, either way:**
  - **Narration only:** no voice cost. For example, c3_0096 "When I come upstairs, her light's on." and c3_0099 "My window's still open from this morning. The night air…" (wording is the Story thread's call).
  - **Plate edit:** a region edit with `region_composite.py` that closes his sash and opens her window. If you make it, check that `bg_kohei_room_night_dark` still matches "I leave my window open a while longer" (c3_0323), where his window should stay open.

### 3. Genji's height is 4′10″, not 5′2″. Must-fix: change the number or record the choice.
- **Where:** every Genji sprite (c3_0376–c3_0382, c3_tea, the steps). It shows clearly beside Natsuki at c3_0390–c3_0394 and c3_0399–c3_0404 (`shots/desktop/1440x900_c3_0391.jpg`, `shots/phone/844x390_c3_0391.jpg`).
- **Measured** at iPad 1180×820 (16.2 px per inch): Genji's head top is 57.8 in, Natsuki's 63, Akane's 59.9, Nanoha's 58.8, Emi's 61.9, Mio's 48.0, Takatsuki's 67.9 and Kirishima's 70.8. Every height except Genji's matches §1b. Genji is `CHAR.genji = {h:58, v:1.0}` in `v2/index.html`, against "Genji 5′2″ (stooped)" in the style guide. Visually he reads a head shorter than Natsuki. If he ever shares a frame with Nanoha (4′11″), he'd also look shorter than her.
- **Fix:** If 5′2″ is meant as his stooped height, set `h:62` (one number in `CHAR`; this scales his whole sprite up about 7%, head included, so recheck him beside Natsuki). If 4′10″ is the intended stooped height, change §1b to say so, so the next CG layout (`cg_layout.py`) uses the same figure. Either is a [P] call Production can make.

### 4. Natsuki is only a face window while she talks to Mio (c3_0408–c3_0292). Low; staging.
- **Where:** c3_lunch, from c3_0409 to c3_0291, at iPad (`shots/phone/844x390_c3_0409.jpg` shows the same staging).
- **What:** Mio stands alone at center while Natsuki trades four lines with her face to face, shown only in the face window. §3a rule 2 allows a window for "a crowded scene", but this isn't one, and the TV exchange 20 lines later (c3_0423) puts both girls on stage. The door exchange at c3_0284 (Natsuki behind Kōhei, Emi on stage) is fine as it is.
- **Fix:** `@move mio l` and `@show natsuki track_grin r` before c3_0409, then let the existing `natsuki(...)` face tags become `natsuki<...>` sprite expressions.

### 5. Two small art/text compromises. Low; probably accept, but decide on purpose.
- **Usagi-san (c3_0113–c3_0118):** Kōhei turns the rabbit to face his window (c3_0113). `cg_window_sill` keeps showing the rabbit's back and tail for the five lines until Nanoha turns him back (c3_0119). No existing art shows him facing out.
- **Akane on the sofa (c3_0060–c3_0067):** "Akane's asleep on the sofa under a fleece blanket, curled up small" plays over `bg_fujisawa_living_night`, which shows the sofa empty with the blanket folded on it. She then appears standing (`akane_home_sleepy`, c3_0070) while she "pulls the blanket up over her head" (c3_0088). This is the standard sprite compromise. The only real fix would be a small CG, which isn't worth it for this beat.

### 6. Emi's line stays on screen through the 0.9 s wait into the Tachibana living room (c3_0285 → c3_0406). Backlog (engine-wide).
- **Repro:** iPad, normal tap speed. Tap past c3_0285. The background changes, Emi fades out, and for the `@wait 0.9` (about 1.1 s in the clean run) her name tag and line ("Barging? You're saving me…") stay up over the new room with nobody on stage. Then Mio appears. Frames: `shots/clean/t_c3_0285.jpg`.
- **Cause:** `run()`'s `wait` case doesn't hide or clear the box. Ch1's `@wait 0.6` before Akane in c1_morning behaves the same way, so this is the established behavior, not a Ch3 regression.
- **Fix (next engine pass):** clear the name and text, or fade the box out, when a `wait` follows a `bg` change.

### 7. CG-to-CG change can flash the room between CGs on a starved device. Backlog; seen once, not reproduced.
- **Seen once:** in the normal-speed iPad replay at cg_window → cg_window_sill (tap on c3_0105), with load average about 32 and video capture running. The outgoing CG disappeared and `bg_kohei_room_night` showed for about 0.5 s before the new CG faded in (frames in `shots/frames/t_c3_0105_sill.jpg`, t=309.80–310.55). DOM sampling in the same run agrees: at +1253 ms `cg_window` had lost `on` (opacity 0), while `cg_window_sill` had `on` but a computed opacity still at 0.0.
- **Not reproduced:** in 8 later per-frame trials (3 normal; 5 with 4× CPU throttling, covering both c3_0105 and c3_0313), the incoming CG never let the background show. The full low-load replay also showed a normal crossfade for both changes (`shots/clean/t_c3_0105.jpg`, `shots/clean/t_c3_0313.jpg`).
- **Cause in code:** `setCg` removes the outgoing image on a fixed `setTimeout(dur*1000+60)` after the incoming image's `onload`, not after it has actually painted. If decoding or compositing the 2400×1340 WebP stalls for more than about 1 s, the background shows through. On an iPad this is unlikely; on an older phone it's possible.
- **Hardening (cheap):** `await next.decode()` before adding `on`, and drop the outgoing CG on the incoming one's `transitionend`, keeping the timer as a fallback. The same `decode()` would also make `cgWait` time its 1.1 s beat from a painted image.
- **Note:** The Oct 17 regression (text box hidden during CG changes) is not present. The box stays up through both CG-to-CG changes and through `@cg -`.

### 8. The title theme fades out, then restarts at the end card. Low; for the author's ear.
- The script ends `@bgm title` (c3_0306) → `@bgm -` → `@bg black slow` → `@wait 1.0` → `@endchapter 3`. `endPilot()` then calls `playBgm('title')` again. The same theme plays under the last two narration lines, fades to silence for about 2 s on black, and restarts from its loop start on the end card.
- **Fix:** If the silence on black isn't intended, drop the `@bgm -` while Ch3 is the last chapter. Revisit when Ch4 is appended, since the line will then lead into Ch4's chapter card.

### 9. No face-window crops for Emi, Mio or Genji. Backlog; latent.
- `img/face/` has none of `emi_home_*`, `mio_home_*` or `genji_shrine_*`. I simulated `faceFor()` on every Ch3 line, and none needs one: each of them speaks only while on stage or inside `cg_lunch`, whose `CG_CAST` includes them.
- **Risk:** the first off-stage line from any of them would request a missing file and show an empty window. Ch4's FB1 has Genji ([P], chapter map).
- **Fix:** run `faces.py` for the three sets before Ch4.

### 10. Two minor expression nits. Optional.
- **c3_0065, Kōhei:** "I'm home. What happened? Did she eat? Did she take her—". The window uses `neutral`, but the line is anxious. `serious` (as at c3_0076 and c3_0078) fits better.
- **c3_0424–c3_0425, Mio:** she is still `home_grin` through "She wins three in a row" and Natsuki's "Kagero says thanks for playing", and only turns to `pout` on her own line (c3_0426). Switching her to `pout` at c3_0424 lets the loss land on her face.

---

## What I checked and found fine

**`qa_play.py --every` at iPad 1180×820** (whole build; report in `qa/report.json`; shots converted to JPEG in `qa_jpg/`, Ch3 contact sheets in `shots/qa_sheets/`):
- 796 shots, 784 lines seen. `missed_lines` is empty, `bad_requests` is empty and `voice_missing` is empty.
- 460 of 463 spoken lines are voiced. The 3 unvoiced lines are c1_0222, c2_0080 and c2_0230, all outside Ch3.
- The manga insert's 10 steps were all seen.
- The only console error is the blocked Google Fonts request.
- I read all 229 Ch3 frames plus the end card. Every one is settled and staged as the script says.
- (It took three attempts. The first crashed when Chromium ran out of memory on the shared machine, and the second hit a full shared disk. The third ran clean.)

**Normal-speed replay by real taps** (iPad landscape 1180×820, touch, Chromium, starting from the last line of Ch2). I ran it twice: once under heavy load, and once as a full clean pass after the load dropped (load average 4–8; `shots/ipad_clean/replay.json`, frame sheets in `shots/clean/`):
- All 229 Ch3 lines (98 narration, 131 spoken) displayed in order, with no tap ignored or doubled. All 131 voices played during the clean pass.
- The chapter transition works: the Ch2 interlude ends, then black, the "CHAPTER 3 / Windows / 第三話" card, the "Thursday, April 10" card, and the houses at night.
- The end card reads "END OF CHAPTER 3" with "Chapter 4, 'The Light at the Shrine,' comes next", matching the chapter map.

**Fast-tap replay** (taps about every 100–150 ms through typing, cards and CG waits, whole chapter):
- All 229 lines were displayed (`state.read` holds every Ch3 ID).
- At every line, the sprite on screen matched the engine's sprite state, so no stale expression won the preload race.
- Taps during CG loads and cards were ignored as designed. The end card was reached with no errors.

**Freeze-frames** (video of the replay, plus per-frame DOM sampling):
- The chapter card and date cards.
- The background changes c3_home → living room → bedroom → dojo → steps → tree → steps → houses → Tachibana living room.
- `cg_window` (slow) with the box hidden and back after the beat.
- `cg_window` → `cg_window_sill` → `cg_window_sill_turn`: the box stays up, and the living stills fade in after the still.
- `@cg -` with the bedroom crossfading to `_dark`, matching "her light goes out".
- `cg_tree_natsuki` in and out, `cg_tree_light` with Nanoha's face window, and `cg_lunch` in and out.
- Sprite swaps, slides and two-shots (c3_0067, c3_0311, c3_0088, c3_0331, c3_0334, c3_0370, c3_0375).
- Apart from item 7, the only anomalies were late or stalled starts caused by the machine load; none reproduced as a logic error.

**Living stills:**
- `cg_window_sill`, `cg_window_sill_turn`, `cg_tree_natsuki` and `cg_lunch` are 3.5 s loops at 24 fps.
- The rabbit's facing is stable through each loop (back turned in `_sill`, sideways toward her in `_turn`), and the loops stay on model.

**Staging against the script, every line:**
- Simulated sprite state, CG cast and face-window choice for all 131 spoken lines. Kōhei has a window on every spoken line with the line's expression. Others get a window only when off stage or out of the CG: Natsuki at c3_0381, c3_0284 and c3_0409–c3_0291; Nanoha at c3_0263, c3_0397 and c3_0404. Every face file exists. Nobody on stage got a window, and no CG character got one during their CG.
- Outfits match the text:
  - Kōhei's windows switch to kendo at practice and back at the steps.
  - Nanoha's home set has her hair down; the window CGs have pajamas, a top bun and the scrunchie.
  - Natsuki's track set has the navy shirt, dark sweats, ponytail and camera.
  - Emi has the yellow apron; Mio has the star T-shirt and the controller.
  - `cg_lunch` has the right seating: Grandpa on the right, Mio between Akane and Natsuki, Nanoha next to Emi, and no Kazuo.
- Expression rules (§3 Oct 24): Nanoha's deadpan (c3_0084) is gone after one line, and Natsuki's smirk (c3_0425) lasts only for Mio's reply. Natsuki's questions use `curious`.
- The speaker brightens and the others dim. Narration and Kōhei's lines dim no one.

**Heights:** measured on screen at iPad. All match style guide §1b except Genji (item 3). Head sizes are consistent between Nanoha's home set (`VSET .82`) and her school set, and between Natsuki's track, kendo and school sets.

**Night and evening tints:** `bg_fujisawa_living_night` gives the sprites its lamplit tint, sepia(.14) saturate(1.04) brightness(.93). No sprites appear on the other night plates (houses, bedroom), and the day scenes have no tint.

**Address and speech (§3b–§3c), spot-read against the script:**
- Natsuki uses きみ and "Fujisawa"; Nanoha says "Natsuki-san", "Kōhei" and, at night, "Kō-chan".
- Kōhei uses お前 and "Chibi", glossed `{Chibi|~shorty}`.
- Akane says "Natsuki-san". Mio says "Natsuki-nee" and "Kō-nii" and refers to herself as Mio.
- Takatsuki avoids "you" in the Japanese. Emi says "Kōhei-kun".
- Full name tags show on every line (Ch1–8 rule), Kōhei's included.
- Translator's notes exist for every glossed Ch3 term, and first uses show the gloss.

**Voice:**
- `voice_levels.py` ran on `v2/voice/`: 460 lines, median speech RMS −20.4 dB. Its only 2 flags are prologue lines p_0007 and p_0010 (−5.9 and −6.6 dB, the dream lines §9 step 5 already notes as possibly intended softness). No Ch3 line is flagged for level, clipping, length or silence.
- Coverage: all 131 Ch3 spoken lines are in `voice/index.json`, in their own scene's pack, and `voice/ja.json` matches the script's Japanese exactly.
- Playback: jumping to each of the 131 lines, the voice started and was audible on the voice bus every time (AudioContext running). Clip lengths are plausible for their text; the slowest clips are slow because of deliberate pauses: c3_0124 between its two sentences, c3_0396 at its ellipsis.

**Phone landscape 844×390** (touch, scene starts plus 21 key lines):
- Text is 16 px, as §3a specifies. The controls strip sits on the box's top edge. No text overflows, including the longest lines c3_0182 (276 characters) and c3_0350 (180), though with fallback fonts.
- The window CGs crop from the bottom (`CG_PHONE_Y`), so the rabbit stays above the box and the top of Nanoha's bun stays in frame.
- The point of light in `cg_tree_light` is visible above the box.

**Desktop 1440×900** (scene starts plus 11 key lines): layout is fine (text 23 px, box 1180 px wide), two-shots don't collide, and Takatsuki's shinai stays on screen.

## Not checked
- Snapshot diff and diff-scoped regression: no baseline for this run.
- Safari/iPad hardware and listening by ear (§9 step 8 leaves these to the author).
- The real UI fonts: Google Fonts is blocked here, so text fit at phone size should be confirmed once with the actual fonts (`qa_phone.py`).
- Frame-accurate fade timing: the recorded video isn't frame-accurate, and the clean run was still on a shared machine.
- Portrait: out of scope (canon §2).
