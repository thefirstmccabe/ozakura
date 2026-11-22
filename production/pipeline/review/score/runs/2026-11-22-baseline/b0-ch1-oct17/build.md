# Build review: Pilot v2, Prologue + Ch1 (Oct 17 build), §9 steps 7 and 9

**Scope:** all of the Prologue and Ch1 before handover. There's no snapshot diff or fix list for this run, so the diff and fix-confirmation steps (steps 2–3) were skipped.

**Build:** `v2/`, served at http://localhost:8150/.

**Sizes tested:**
- iPad landscape 1180×820, the main target.
- Phone landscape 844×390 and 667×375.
- Desktop Chrome 1440×900.
- Portrait was not tested, as instructed.

**Evidence:** everything is under `runs/b0-ch1-oct17/`:
- `qa/`: the qa_play report and 270 screenshots.
- `shots/T*` and `shots/F*`: freeze-frame sequences, each with a `log.json` of per-frame opacities. To capture them, the JS clock was faked and stepped and CSS transitions were slowed 4× and paused for each capture.
- `shots/sizes/`: the phone and desktop spot checks.
- `shots/evidence_*.jpg`: the frames behind the top findings.

**Doc gaps:** this checkout's `story/style-guide.md` has no §3b, §3c or §9. Its sections run §1–§3a, then §4a, §4–§8. I checked against §2, §3, §3a and §7, the README's Build and QA sections, and `production/pilot-v2/scene-outline.md` instead.

---

## Problems, most important first

### 1. The cut out of Natsuki's intro CG flashes an empty classroom, then she ghosts in (medium; every tap speed, every size)
**What happens:** `@cg - cut` removes the CG instantly. Only after that does `@show natsuki school_grin c` start a 0.35 s fade-in. For about 1–3 frames the reader sees an empty classroom. Then Natsuki fades in semi-transparent over the desks.

This is the hitch moment the chapter is built around (scene 1.4). See `shots/evidence_cg_cut_empty_room.jpg` and `shots/T14_cg_out/` (0 ms empty room, 50–200 ms ghosted sprite). The same thing happens under fast taps (`shots/F2_cg_out_fast/`, 250–400 ms).

**Repro:** c1_intro, tap from c1_0145 ("I do kendo…") to c1_0146, at 1180×820, normal speed.

**Fix:** in `ch01.ozs`, move `@show natsuki school_grin c` above `@cg - cut`. The sprite layer sits under the CG layer, so she's already in place when the CG cuts away. Or make it a short `@cg - fade`.

### 2. Speaker dimming works only in evening and night scenes; it's silently broken in every daytime scene (medium; all sizes)
**What happens:** `.spr.dim{filter:var(--bgf,) brightness(.78) saturate(.9)}`. On day backgrounds `setBg` sets `--bgf` to `none`, which makes the value `none brightness(.78) …`. That's invalid, so the computed filter is `none`.

The code still sets the `dim` class correctly (my state log shows `D` flags on the listeners), but nothing changes on screen. In the interlude and at night, the same code does dim. The result is inconsistent presentation within one chapter:
- Kitchen, entrance and lunch: nobody dims.
- Interlude: the listener dims.

Computed values:
- c1_0102 (Nanoha, dim class): `filter: none`.
- c1_0205 (Natsuki, dim class): `… brightness(0.78) saturate(0.9)`.

See `shots/evidence_dim_day_vs_evening.jpg`, `shots/dim_c1_0102.png` and `shots/dim_c1_0205.png`.

**Repro:** c1_entrance, c1_0108 (Ryōsuke speaks; Nanoha and Rika should dim), any size, normal speed.

**Fix:** in `setBg`, use `setProperty('--bgf', BG_LIGHT[name] || 'brightness(1)')`, so the day value is a valid filter list. Or decide dimming is unwanted and drop `dimFor`. Either way, make it consistent.

### 3. After a Load, the chapter's final fade to black is a hard cut (medium; a tap-timing/state edge case like the Oct 17 one)
**What happens:** `restore()` calls `setBg(bg,'cut')`, which sets both background images' `transition` to 0 s. `setBg('black', tr)` never sets a transition; it only removes `on`. So the fade length is whatever the previous background left behind. Continuous play inherits the 1.8 s from the lit-window crossfade and fades correctly. After a Load it cuts instantly.

Measured: the continuous fade is 1.00 → 0.80 → 0.44 → 0.04 over 1.2 s. After save and load it's 0.00 by the first frame. See `work/endtest.py` and `shots/T20_end/` at 0 ms.

**Repro:**
1. c1_night: save in any slot at c1_0257 or c1_0258.
2. Load it.
3. Tap through "I stand there…".

The street cuts straight to black. Any size, normal speed.

**Fix:** in `setBg`'s black/white branch, apply `tr` to `bgImgs` (`transition: opacity ${dur}s`) before removing `on`. Make `#bgSolid` honor `slow` too (see 4).

### 4. `@flash white` isn't a flash; it's a held white screen (medium-low; Prologue)
**What happens:** `compile_script.py` turns `@flash` into `{t:'bg', name:'white', tr:'flash'}`. In the engine, `setBg('white')` returns before its `flash()` call, so no flash ever plays. The engine's own `flash` command is never emitted, so `flash()` can't be reached from the script at all.

What the reader sees instead (`shots/evidence_flash_whiteout.jpg`, `shots/T03_flash/`):
1. The dream CG dissolves to flat white over about 0.7 s, while the box still shows the previous line (p_0011, "Hands that aren't mine…").
2. p_0012–p_0014 play on a blank white screen.
3. `@bg black slow` then goes white→black in 0.6 s (the fixed `#bgSolid` transition), not the 1.8 s that `slow` means elsewhere.

**Repro:** Prologue, tap from p_0011 to p_0012, 1180×820, normal speed.

**Fix:**
- If a flash was meant: emit `{t:'flash'}` so the CG stays behind the flash, and let `@bg black slow` fade the CG out. Note that the `bg` case also turns `slow` into a 1 s CG fade.
- If the white-out was meant: write it as a background change and hide the box during it (see 5).

### 5. The text box stays up over fades to black (medium-low)
**What happens:** the `cg` command hides the box, but `@bg black`/`white` don't. The last line stays on screen over black:
- Prologue end: about 2.1 s of "That I kept them waiting far too long." through `@bg black slow` and `@wait 1.0`, until the chapter card.
- Chapter end: about 2.4 s of "I stand there…" before the end card.

See `shots/evidence_box_over_black.jpg`, `shots/T04_prologue_end/` and `shots/T20_end/`.

**Repro:** p_0014→chapter card, or c1_0258→end card, any size, normal speed.

**Fix:** in `run()`'s `bg` case, add `box.classList.add('hidden')` when the name is `black` or `white`.

### 6. The two past-life voice lines are 6 dB quieter than everything else (medium-low; audio)
**What `voice_levels.py` reports:**
- 169 lines.
- Median speech RMS −20.4 dB; range −26.8 to −20.0.
- 2 flags: **p_0007 −26.5 dB** and **p_0010 −26.8 dB**. These are past_natsuki, the first voice the reader hears.

**Cause:** `voice_pack.py` computes the leveling gain from the dry take, then applies `aecho=0.85:0.6:…`, whose 0.6 output gain pulls the line down.

**Repro:** Prologue p_0007 and p_0010. Voice levels are size-independent.

**Fix:** measure RMS after the echo, or add about +6 dB of makeup gain for past_natsuki. Then rerun `voice_levels.py`.

### 7. Sprite expressions contradict the narration on a few lines (low; staging)
Spoken lines all match (each `who<expr>` was checked against its line). The mismatches are on narration lines, which keep the previous expression:
- **c1_0200** "They both laugh…": Nanoha is `blush` (pained, near tears) and Natsuki is `smile`.
- **c1_0226** "They both laughed, and the moment closed up…": Nanoha is `deadpan` and Natsuki is `blush`.
- **c1_0229** "a different smile… Smaller. It looked like it cost her something": Natsuki stays on her stock `smile`. `wistful` would fit.
- **c1_0089** "She says it like a weather report": Nanoha is `sad`. `deadpan` reads closer.

**Repro:** c1_lunch and c1_interlude, any size.

**Fix:** add `@show` expression changes before those narration lines.

### 8. Fast tapping brings the box back over a barely-visible CG and skips the scripted silent beat (low)
**What happens:**
- The 1.1 s hidden-box pause after `@cg` is cancelled by the next tap. With taps every 110 ms, the box is back while the dream CG is at 12–35 % (`shots/F3_dream_fast/`) and the Natsuki CG at about 40–60 % (`shots/F1_cg_in_fast/`).
- A tap during `@bgm -` / `@wait 0.8` at "Her grin stutters" skips the outline's "beat of silence at the hitch".

Nothing hard-cuts, but these are the chapter's two most important images.

**Repro:** p_0002→p_0003 and c1_0137→c1_0138, 1180×820, tapping every 110 ms.

**Fix:** ignore taps for the first 0.5–0.6 s of a `cg` pause and of `@wait`s at or above 0.5 s.

### 9. Night and evening tints are too light (low; staging)
**What happens:** at night (`brightness(.8) saturate(.82) hue-rotate(-6deg)`), Nanoha's face and white shirt read as daylit against `bg_houses_night` (mean value 0.34). In the evening interlude the sepia tint barely warms the sprites against a strongly orange room. See `shots/tints.jpg`.

**Repro:** c1_0236 and c1_0205, 1180×820.

**Fix:** go darker and cooler at night (for example `brightness(.62) saturate(.75)` plus a slight blue). Add more warmth in the evening (for example `sepia(.35) saturate(1.15) brightness(.92)`).

### 10. The title menu sits on top of Nanoha (low; title)
**What happens:** at every size the menu column and the left-side shade cover Nanoha, one of the three leads on `cg_title`. "Continue" and "Chapters" run across her face and body. At 667×375 the "PILOT V2 · PROLOGUE & CHAPTER 1" subtitle also runs into the tree trunk.

See `qa/00_title.png`, `shots/sizes/desktop_1440x900_00title_menu.jpg` and `shots/sizes/phone_844x390_00title_menu.jpg`.

**Fix:** shift the CG's `object-position` right, or move the menu or the art so all three characters are clear.

### 11. Chapters → Chapter 1 skips the chapter title card (low; UX)
**What happens:** `sceneStart('c1_morning')` points at the scene command, which comes after `@chapter 1`. Picking Chapter 1 goes straight to "Monday, April 7" and never shows "Chapter 1 · The House Next Door".

**Repro:** Title → Chapters → Chapter 1, any size.

**Fix:** have chapter starts point at the `chapter` command.

### 12. The night music loop is only 34 s (low; Audio thread)
**What happens:** `night.mp3` is 34.0 s. The author's Oct 11 note in style guide §7 says "Keep; extend (43 s loop)", so this is shorter than before rather than extended. c1_night runs several minutes at reading pace, so the loop repeats 5 or more times. `daily.mp3` (51.8 s) also carries three long scenes. The loop seams themselves are clean: the spectral distance at the seam is within each track's normal variation.

**Fix:** pass to the Audio thread to extend `night` (and ideally `daily`) to 2–3 minutes, per §7 "Finishing".

### 13. Akane's sprite skirt is mid-thigh; §2 specifies "navy pleated skirt below the knee" (low; art)
**What happens:** the box mostly hides it in play. But the hem and bare thigh show faintly through the translucent box and in the strip below it at 1180×820 (`qa/024_c1_0011.png`, `qa/040_c1_0027.png`). This conflicts with the design sheet and the "modest framing" rule.

**Fix:** correct the skirt length in the Akane school set at the next sprite touch-up.

### 14. qa_play.py doesn't actually reach every line (low; QA tooling)
**What happens:** it saw 268 of 272 lines and skipped p_0006, c1_0208, c1_0221 and c1_0227. The cause is a race: `check()` reports `typing`, but by the time the separate `advance()` call runs the line has finished typing, so that advance moves past the line. My own walker hit the same race once (c1_0049).

The README says qa_play "plays every line", so its sign-off overstates coverage.

**Fix:** do the typing check and the advance in one `evaluate`, e.g. `(()=>{const v=window.__vn; if(v.check().typing) v.advance();})()`.

---

## Checked and found fine
- **qa_play report:**
  - No page errors and no bad requests.
  - 169 of 170 spoken lines voiced. c1_0221 "…" is unvoiced on purpose (`|| -`).
  - Every voiced line decodes; none missing.
  - The one console error is Google Fonts failing through this sandbox's proxy (`ERR_TUNNEL_CONNECTION_FAILED`). Screenshots therefore use fallback fonts, and typography is unverified here.
- **Voice playback in the browser:** every voiced line over 1 s was confirmed playing about 0.75 s after it appeared. In auto mode, 22 consecutive lines advanced only after their voice ended, with no cut-offs. Clip lengths are plausible for their lines.
- **Face windows (§3a):**
  - All 45 of Kōhei's spoken lines show his window with the scripted expression.
  - No window for anyone else: every other speaker is on stage, or is in `CG_CAST`/`NOWIN` (Ōno-sensei, ???).
  - No window on any narration line.
  - Name and text colors match the §3a hues, and the backlog uses them.
- **Who's on screen:** matches the script throughout. `@move` slides work: Akane goes c→l at Nanoha's entrance, and Natsuki c→r at lunch. `@hideall` and scene-change fade-outs are clean. The interlude has no Kōhei window, and the vignette and "— Interlude: Nanoha —" label fade in and out correctly.
- **Sprite heights:** the on-screen head tops at 1180×820 match the §1b heights to within 1 px. For example, Ryōsuke (5′7″) is 129–134 px above Nanoha (4′11″), against 129 px expected. Natsuki is about 4″ above Nanoha, Rika 2″ and Akane 1″, all as specified.
- **Transitions (frame by frame, normal speed):**
  - Background crossfades: 0.9 s, or 1.8 s for the lit window.
  - CG fade-ins: the box hides, then returns after 1.1 s, sitting above the CG (no z-index regression).
  - The dream's living still crossfades in at about 2 s with no visible jump. The still and the video's first and last frames differ by about 2–4/255.
  - Chapter and date cards hand off cleanly.
  - No mirrored or reversed locations: the CG classroom layout matches `bg_classroom_day`.
- **Taps and modes:**
  - Touch taps: the first finishes the line, the second advances. Tapping on the text box advances too.
  - Skip runs from the Prologue to the end card in 24 s with no stuck state.
  - The end card text ("Chapter 2, 'Kendo,' comes next") matches the chapter map.
- **Phone landscape (844×390, 667×375) and desktop (1440×900):**
  - Scene starts and two- and three-sprite shots fit.
  - The face window and name tag line up.
  - No text overflow. The box grows to about 38 % of the screen height for the longest narration at 667×375, which is acceptable.
- **The dream CG** is the least-saturated image in the build (mean saturation 0.14), which fits canon §2's cool, desaturated past-life treatment.

## Not verified
- **Snapshot diff and fix confirmation:** none exist for this run.
- **Portrait:** not tested, by instruction. Note that `manifest.webmanifest` says `"orientation": "any"` and the build has no rotate-your-device screen. If landscape-only applies, both are missing.
- **Voice content:** no speech-to-text was available, so clips weren't transcribed. One clip is worth a listen: c1_0141 has a 160 ms sound about 300 ms after the line ends. I couldn't match it to the start of c1_0143, so it's probably a breath.
