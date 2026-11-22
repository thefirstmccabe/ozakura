# Build review: Pilot v2, Prologue + Ch1 (Oct 18 build)

Independent QA of `v2/` before handover (§9 steps 7 and 9). The scope was all of Ch1. Per this run's brief there was no snapshot diff or regression baseline, so §9 step 3 ("look at every changed frame") was skipped. Portrait was not tested.

**Verdict: no blockers.** The chapter plays start to finish at normal and fast tap speeds with no errors. Every line shows, every voiced line plays, and the Oct 17 regressions (text box hidden during CG changes, mirrored CG, tap-timing hard cut) are fixed. I found 12 problems, none severe. The first three are worth fixing before handover: Continue loses your place, Rika's frog clip has lost its crown, and listener dimming is broken.

Paths below are relative to `runs/b1-ch1-oct18/`. Screenshots are in `shots/`, and the qa_play output is in `qa/`, saved as JPEG to save disk space.

---

## Problems (most important first)

### 1. Continue sends you back to the start of the scene, and after a Load it can send you even further back (medium)
- **Repro (iPad 1180×820, any tap speed):** play into "Lunch with Mizuno" up to c1_0175. Tap Menu → Return to title → Continue. Play resumes at **c1_0162**, the first line of the scene, not c1_0175. The same happens after a page reload, which is what an iPad tab reload or closing Safari does.
- **Worse after a Load:** load a save made at c1_0151, then Menu → Return to title → Continue. Play resumes at the last scene start you *played into* before the Load. In my run that was the **cold open**. (`shots/func.json`, keys `loaded` and `continued`.)
- **Cause:** `v2cont` is written only when a `scene` command runs (`run()`, `case 'scene'`). `restore()` and `startAt()` (Load, Chapters) never update it, and neither does leaving the game.
- **Fix:** write `store.set('v2cont', snap())` in `line()` (cheap) or on `pagehide`/`visibilitychange` and in `toTitle()`. Keep the scene-start write as the fallback. If resuming at the scene start is intended, the README should say so, because the author reads in sittings on his iPad.

### 2. Rika's frog clip has no crown, though the text points straight at it (medium-low; art/text mismatch, off-model)
- **Repro:** c1_0104, any size. The narration says *"a small frog wearing a crown. The frog is new."* The sprite's frog clip has no crown (`shots/rika_clips.png`, `qa/101_c1_0104.jpg`).
- The approved reference `production/refs/inventory/full-rika.png` has the crown (`shots/ref_rika_head.jpg`), and so does style guide §2 ("frog with a crown"). It was lost in the sprite pass. All four Rika expressions and her face crops share the defect.
- **Fix:** do one edit on the Rika base sprite to add the small yellow crown, then regenerate or propagate it to `rika_school_{grin,pout,scheme,surprised}` and re-crop the face windows. Don't change the line.

### 3. Listener dimming never shows in day scenes; it only works under night or evening light (medium-low; latent inconsistency)
- **Repro:** c1_0029 (kitchen), c1_0102 (entrance) or c1_0186 (lunch). The engine adds `.dim` to the non-speaking sprite, but its computed `filter` is `none` (checked with `getComputedStyle`).
- **Cause:** `setBg()` sets `--bgf` to the literal `'none'` for unlit backgrounds. `.spr.dim{filter:var(--bgf,) brightness(.78) saturate(.9)}` then resolves to `none brightness(.78) …`, which is invalid, so the filter drops to `none`. Under `BG_LIGHT` backgrounds (night, evening) `--bgf` is a real filter list and the dimming works.
- In Ch1 this happens to be invisible, because no night or evening scene has two sprites on stage. From Ch2 on, any night or evening two-shot will suddenly dim the listener while day scenes never do.
- **Fix:** use `BG_LIGHT[name] || 'brightness(1)'`, or `removeProperty('--bgf')` for unlit backgrounds. If the author has been happy without dimming, delete `dimFor` and the `.dim` rule instead, so night scenes don't start doing it.

### 4. Backgrounds that contradict the narration (low)
- **c1_0099:** *"The entrance hall is chaos. Two hundred students…"* is shown over an empty entrance hall with no crowd (`qa/096_c1_entrance_start.jpg`).
- **c1_0133–c1_0160:** homeroom has *"a room full of strangers"* and *"someone in the front row actually claps,"* but `bg_classroom_day` is empty. This is VN convention, and the Natsuki CG does show classmates, so it's a minor point.
- **c1_0260:** this is the first mention of the title tree (*"…from the bridge it looks like a pink cloud caught on the hillside"*), but `bg_river_morning` shows only mountains and no hillside tree (`qa/053_c1_0260.jpg`).
- **Fix (cheapest first):** soften the entrance line to fit an empty plate, or make a crowd variant of `bg_school_entrance`. For the Ōzakura, either add the distant pink mass on the hill to the river plate or move the line to the shrine scene where the tree is shown.

### 5. A few expressions don't match their lines (low)
- **c1_0024 and c1_0025.** Akane's one quiet, sincere line (*"…You always are."*, *"She says it to the rice cooker"*) is played on `akane_school_pout`, which has puffed cheeks and looks straight at the camera. That reads as comic. §3b asks for "a quiet sincere line under the teasing." Akane has no softer expression, so use `smile` at most, or make a looking-down variant.
- **c1_0201.** The narration says *"Mizuno laughs, and after a second Nanoha does too"*, but the sprites stay on `natsuki grin` and `nanoha blush` (`qa/189_c1_0201.jpg`). Switch them to `natsuki<laugh>` and `nanoha<happy>`.
- (Ok as is: at c1_0100–c1_0101, Nanoha appears only once Rika "hits" her. It reads as a pop-in, which is fine.)

### 6. Nanoha's face-window crop cuts off her chin (low)
- **Repro:** the interlude, c1_0207–c1_0223 (7 lines), at any size. Her `img/face/nanoha_school_*` crops are much tighter than Kōhei's head-and-shoulders set: her mouth sits on the bottom edge and the frame is mostly hair (`shots/crop_interlude_face.png`, `shots/faces_sheet.png`). Akane's, Natsuki's and Rika's crops are equally tight, but they aren't shown in Ch1.
- **Fix:** re-crop the non-Kōhei faces with `faces.py`, a bit looser and centred lower (eyes at about 40% from the top), to match Kōhei's framing.

### 7. Ōno-sensei's hair clips at the top of the screen on iPad (low)
- **Repro:** c1_0135–c1_0136, at 1180×820. The 6′0″ sprite's head top is at y = −8 px (measured; the other sprites are within 2 px of the lineup, see "Fine" below) (`shots/teacher_top_crop.jpg`).
- **Cause:** `SCALE` puts a 5′9″ head at 95% of stage height, so anyone over about 5′11″ clips. Kazuo (6′0″) will clip the same way later.
- **Fix:** anchor the scale to 6′0″ at about 97%, or accept the clip.

### 8. On small phones, long narration covers the speakers' faces (low; phones are secondary)
- **Repro:** at 667×375 (iPhone SE landscape), the text box is 197 px tall (53% of the screen) for c1_0038 and c1_0204. At c1_0038 it covers Akane's and Nanoha's faces up to the eyes (`shots/sizes/667x375/c1_0038.png`). At 844×390 the same lines take 43%.
- **Fix:** split the three longest narration lines (c1_0038, c1_0162, c1_0204, about 280–330 characters), or reduce the text size and line height on short viewports.

### 9. The control buttons are small tap targets, right next to the tap-to-advance area (low)
- AUTO / SKIP / LOG / SAVE / LOAD / MENU are about 30 px tall on iPad (11.9 px text) and 27 px on phones, against the 44 pt guideline. A near miss lands on the box and advances the story.
- **Fix:** give the buttons `min-height:44px` with the same visual size (padding), or treat taps within about 12 px of a button as dead.

### 10. CG-to-CG crossfades remove the old CG on a timer instead of when the new one is opaque (low; robustness)
- In `setCg()`, the "over" path hides the old CG `dur*1000+60` ms after the new image's `onload`, but the new image's CSS fade can start late on a first decode.
- **Repro (iPad size, single tap, moderate load):** at c1_0147, tap to go from falter back to intro. The falter CG was removed while intro was at 0.90 opacity, so the classroom background showed through at 10% for a moment (`shots/freeze_single2/freeze.json`, T14). Under heavy load the new fade started about 0.5 s late.
- The video recording shows nothing visible at normal speed. A slower device or a cold image cache makes it worse.
- **Fix:** `await next.decode()` before adding `on`, and remove `cur` on the new image's `transitionend`, keeping the timer as a fallback.

### 11. The first CG of a sequence always pauses 1.1 s, even for slow 1.8 s fades, so the dream's living still is mostly missed (low polish)
- **c1_0263 → p_0003:** the text box returns while `cg_dream` is only about 60% in, and the living-still loop fades in about 2 s later, under the reader's text.
- **Cold open, `cg_cold_mist`:** the Kling loop starts fading in about 1.2 s into a 3.4 s shot and is fully visible only at about 2.1 s. It is then removed instantly as `cg_cold_mirror` starts, so the "living" part runs for about 1 s.
- The instant swap from video to still is barely visible: the loop frames differ from the still by only 2–4/255 on average.
- **Fix:** in `case 'cg'`, use `pause(tr==='slow'?1900:1100)`. Lengthen the mist `@wait` to about 4.5 s, or start the loop sooner with a shorter `liveOn` delay.

### 12. Voice levels: the two dream lines are flagged about 6 dB quiet (needs an ear check)
- `voice_levels.py` on `v2/voice/` reports 159 lines, a median speech RMS of −20.4 dB, and 2 flags: **p_0007 at −26.3 dB (−5.9)** and **p_0010 at −27.0 dB (−6.6)**. There is no clipping and no short or mostly-silent clips (`voice_levels.txt`).
- §9 step 5 already notes these as possibly intended softness, and nothing here can listen. Have someone check them by ear on the iPad against `memory` (BGM ducks to 55% under voices).

---

## Notes (not counted as problems)
- **Akane's skirt** ends above the knee, while style guide §2 says "below the knee." The sprite matches the approved reference `refs/design-oct10/r3/akane-teen-uniform.png` (`shots/ref_akane_uniform.jpg`), so the fix belongs in §2's wording, not the art.
- **Ōno-sensei** looks closer to 30 than §2's "40s". This is for the on-model check to judge.
- **Kitchen:** "the whiteboard on the fridge" (c1_0007–c1_0009). The fridge is cropped out at iPad aspect and appears only on wide desktop windows.
- **Title:** the menu sits over Nanoha's figure in the title art at every size. It's readable because of the shade.
- **For the Story or dialogue pass, not the build:** the dream narration says "She says it like…" three times (p_0008–p_0009), which is on §3b's tic list. It may be a deliberate anaphora kept from the prologue.
- **Unverified risk:** the cold-open "seen" flag is keyed by scene id (`v2holdSeen.cold_open`). If the author's iPad played an earlier build with a `cold_open` hold, a tap now skips the new Oct 18 cold open on its first showing. I couldn't verify this without looking at older builds. Clear or version the key at handover if that applies.

---

## What I checked and found fine
- **qa_play.py** (`--every`, 1180×820, `qa/report.json`) found 0 bad requests, 0 missing voices and 0 missed lines. It saw 259 of 259 lines. 159 of 160 spoken lines are voiced; c1_0222 "…" is intentionally unvoiced. The only console error is the Google Fonts stylesheet, which this sandbox's proxy blocks; that's the environment, not the build. Screenshots therefore use fallback fonts.
- **Build integrity:**
  - A fresh compile of `ch01.ozs` is byte-identical to the shipped `v2/script.json`.
  - `voice/ja.json` matches the script's Japanese.
  - `voice/index.json` has exactly the 159 voiced IDs.
  - Every referenced sprite, face, background, CG, living still, BGM and SFX file exists and loads.
  - Clip durations are plausible for their text, with no outliers. A transcript check wasn't possible here (no speech-to-text).
- **Normal-speed real-tap playthrough** (iPad, tapping once typing and voice finish): all 259 lines shown in script order, **all 159 voiced lines started playing**, 0 errors, end card reached (`shots/play_normal/play.json`).
- **Fast mashing** (a tap every 120 ms from Begin to the end card): all 259 lines shown fully in order, nothing skipped unseen, all voiced lines started, 0 errors (`shots/play_fast/play.json`). The cold open ignores taps the first time and skips to the chapter card with one tap the second time.
- **Every transition was freeze-frame sampled** (stage state every 20–40 ms, plus video, `shots/freeze*`, `shots/coldopen*`):
  - **Backgrounds and sprites:** background crossfades (room→kitchen, kitchen→river, river→entrance, entrance→classroom, lunch→evening interlude, interlude→night, night→lit night at 1.8 s, night→black) are all smooth. Sprite fade-ins, fade-outs, `@move` slides and `@hideall` are smooth too.
  - **Background → CG** (collar, Natsuki intro, dream): CG fades over the stage, the text box hides during the pause and returns with the line.
  - **CG → CG** (intro → falter → intro): the text box stays up the whole time, and a fast tap mid-fade fades the falter CG back out smoothly. The Oct 17 hard-cut and hidden-box regressions are fixed.
  - **CG → background** (collar → river with Kōhei's face window, intro → classroom with Natsuki fading in underneath): smooth.
  - **Cold open:** mirror → hand → mist (living still) → mirror, then the intentional hard cut to black and the chapter card, then the date card. All in order.
  - **Dream ending:** the flash to white masks the CG cut as intended, the closing lines sit on white, then a 1.8 s fade to black and the end card.
- **Layout:**
  - The collar CG keeps the river on the left, like `bg_river_morning`.
  - The intro CG keeps the windows on the left, like `bg_classroom_day`. No mirroring problem.
- **Face windows (§3a):**
  - Kōhei has a window on all 44 of his spoken lines, with expressions that fit (smile 13, deadpan 10, neutral 10, surprised 6, annoyed 3, grin 1, flustered 1).
  - Ōno-sensei gets a window at c1_0151, during a CG that doesn't show him.
  - Nanoha gets windows on her 7 interlude lines (she is the POV).
  - No window appears for on-stage speakers, for "???", or in the dream.
- **Sprite heights, measured** (alpha bounds at 1180×820): Nanoha, Natsuki, Akane, Ryōsuke and Rika head tops are within 2 px of the §1b lineup (4′11″, 5′3″, 5′0″, 5′7″, 5′1″). Ōno is the exception (problem 7).
- **Night and evening tints:** Nanoha at night gets `brightness(.8) saturate(.82) hue-rotate(-6deg)`. Natsuki in the evening interlude gets sepia. The interlude also shows its vignette and the "— Interlude: Nanoha —" label.
- **Script staging:** who is on stage, the order of entrances and exits, and expression changes all follow `ch01.ozs`. The exceptions are in problem 5.
- **Address sheet (§3c):**
  - Kōhei uses *omae* only with Nanoha and Akane, and *ore* throughout. He calls his mother "Kaa-san" and says "Night, Chibi" (planted).
  - Natsuki uses *kimi* with a bare "Fujisawa," "Nanoha" from day one, and asks to be called Natsuki in front of him.
  - Nanoha says "Mizuno-san," then "Natsuki-san"; "Kōhei" and "Kō-chan" in private; "Rika-chan", "Akane-chan".
  - Rika says "Nano-chan" and "Fujisawa-kun", with *atashi*. Ōno calls himself "Sensei" and uses bare surnames.
  - Kōhei's narration uses "Tokiwa," "Mizuno," and "Nanoha".
- **Save, load and backlog:**
  - Save and Load during a CG line (c1_0151) restore the CG, the text box, Ōno's face window and the voice.
  - The backlog shows name colors, the Japanese text and replay buttons.
- **Phone landscape** (844×390 and 667×375) and **desktop** (1440×900 and 1920×1080):
  - Every scene start and key line renders with no horizontal scroll, no text overflow and no JS errors.
  - The box stays 1180 px wide and centred on wide screens, and sprites sit at sensible positions.
  - The exception is problem 8 (box height on small phones).

## Limits of this run
- The machine was shared and heavily loaded (load average up to about 30 from other jobs) for much of the session. Timing measurements taken under that load were discarded, and the key transitions were re-sampled at lower load (about 5).
- Chromium only: nothing here tests iPad Safari or WebKit, the audio session or Silent Mode, or listens to anything.
- There was no snapshot diff or baseline for this run.
- Test scripts are in `scratchpad/br_b1_ch1_work/`: `freeze2.py`, `play.py`, `sizes.py`, `func.py`, `coldopen.py`, `cont.py`.
