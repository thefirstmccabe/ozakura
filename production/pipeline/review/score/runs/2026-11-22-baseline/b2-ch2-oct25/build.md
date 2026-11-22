# Build review: Pilot v2 Ch2 "Kendo" (build of Oct 25), before handover

Reviewer: independent QA agent (didn't make the build). Scope: all of Ch2, §9 steps 7 and 9. No snapshot diff or fix-round regression in this run (no baseline; steps 2 and 3 skipped as instructed).

Paths below are relative to `/tmp/claude-0/-home-claude/8a181b96-a746-50e6-b79a-45dd7696162d/scratchpad/score/runs/b2-ch2-oct25/` unless absolute.

## Summary

11 problems: 3 must-fix, 3 should-fix (normal play, cosmetic), 5 backlog. The automatic checks are clean: every line reached, every request OK, every voiced line present, decodes and plays. The problems are in presentation: speaker dimming doesn't work in any Ch2 scene, the slip-to-catch handoff blinks to an empty dojo, and some staging doesn't match the text.

| # | Severity | Problem | Where |
|---|---|---|---|
| 1 | Must-fix | Speaker dimming is broken on every untinted background (all of Ch2's multi-character scenes) | c2_dojo, c2_lesson, c2_debrief |
| 2 | Must-fix (verify on iPad) | Slip → catch: Natsuki and the text box fade out before the video is playing, so the bare dojo flashes | c2_0186 → cg_catch |
| 3 | Must-fix | c2_0090 "she" reads as Rika: she's the only sprite on stage when "she" wipes the board and borrows the glasses | c2_lesson |
| 4 | Should-fix | After the catch, the standing "tears" sprite is fully visible through the fading CG (double exposure) | c2_0196 → c2_0197 |
| 5 | Should-fix | Expressions held past their line (laughing through quiet narration; surprised held for 4–5 lines) | c2_0044–0049, c2_0154–0158, c2_0080 |
| 6 | Should-fix | Narration moves to another place while the old background stays (Nanoha's "Again." note, her lit window) | c2_0056–0299, c2_0301 |
| 7 | Backlog | Chat panel covers the interlude label at phone landscape | c2_0262–0287, 844×390 |
| 8 | Backlog | The chat stays on screen through "Natsuki put the phone down" | c2_0288 |
| 9 | Backlog | Tapping during the catch video snaps from mid-motion to the final pose in 0.2 s | cg_catch anim |
| 10 | Backlog | Insert art departs from three panel briefs (nothing a reader is told) | ins_match p1, p2 |
| 11 | Backlog | Day and evening dojo plates are almost the same; the time jump to evening barely reads | c2_mop |

---

## Must-fix

### 1. Speaker dimming never works on daytime/indoor backgrounds
- **What:** `dimFor()` correctly adds `.dim` to the non-speaking sprites, but the CSS `.spr.dim{filter:var(--bgf,) brightness(.78) saturate(.9)}` becomes `none brightness(.78) saturate(.9)` whenever `setBg()` sets `--bgf` to `'none'` (every background not in `BG_LIGHT`). That value is invalid, so the computed filter is `none`. Dimming only works on `bg_dojo_evening` and `bg_bridge_dusk`, and Ch2 never has two sprites on stage there. Result: Ch2 never dims anyone. In the normal-speed run, 70 sprite-lines had `.dim` set and every one rendered `filter: none`.
- **Repro:** iPad 1180×820, any tap speed. c2_dojo c2_0078 (Takatsuki speaks; Kirishima and Natsuki should dim), or any line of c2_lesson / c2_debrief with 2–3 sprites. `getComputedStyle(sprite).filter` is `none` on the `.dim` sprites. Shots: `shots/probe_ipad/c2_0078.png`, `shots/probe_ipad/c2_0115.png`.
- **Fix:** in `setBg()`, use `BG_LIGHT[name]||'brightness(1)'` (or `removeProperty('--bgf')` for untinted backgrounds). Tested live on c2_0078: with either change, the dimmed sprites compute `brightness(.78) saturate(.9)` and the speaker keeps full brightness. The same CSS runs in Ch1, so its daytime multi-sprite scenes are almost certainly affected too. Rerun the Ch1 regression after the fix.

### 2. Slip → catch: a blink of empty dojo before the catch video
- **What:** the script does `@hide natsuki` and then `@anim cg_catch`. The sprite (0.35 s fade) and the text box (0.25 s) fade out at once, but the video only fades in (0.25 s) after its `playing` event. Sampled every 10 ms at iPad size: the sprite is below 0.1 opacity at about 270 ms, `playing` fires at 449 ms, and the video passes 0.1 at about 495 ms. That leaves about 0.2 s of bare dojo with no box, served from localhost. In the full normal-speed run on this (heavily loaded) machine, the gap was 0.8–1.7 s. It lands at the chapter's peak, between "Her heel goes out from under her" and the catch. I can't test Safari. The look-ahead `fetch()` of the mp4 may not prime Safari's media loader, so on an iPad over GitHub Pages the gap could be longer.
- **Repro:** c2_mop, tap past c2_0186 at iPad size, normal speed. Measurement log is in the notes at the end; frames in `shots/anim_ipad/`.
- **Fix:** keep Natsuki on stage until the video is visible. Drop the `@hide natsuki` before `@anim`, and have `playAnim()` call `hideAll()` in `onplaying` when it fades the video in. Also prime the element itself: set `animV.src` with `preload=auto` from the look-ahead loop, or put the video's first frame up as a still at once. Recheck on the iPad.

### 3. c2_0090: the reader pictures Rika in the glasses
- **What:** after Rika's "Okay. Explain everything." (c2_0088), only Rika's sprite is on stage when the narration says "Two minutes later she's wiped the practice schedule off the whiteboard…, borrowed a pair of glasses…, and picked up a shinai to point with." The natural reading is that *she* is Rika. Natsuki only appears afterward, in glasses, at c2_0091.
- **Repro:** c2_lesson, c2_0090, any size and speed. Shot: `qa/343_c2_0090.png` → `qa/344_c2_0091.png`.
- **Fix:** move `@show natsuki teach_smile c` above c2_0090. That's a staging fix inside Production. Or write "Mizuno" for "she" in c2_0090, which is a wording change to hand to Story.

## Should-fix (normal play, cosmetic)

### 4. Catch CG → scene: double exposure
- **What:** at `@cg -` the CG fades over 1 s, but `natsuki kendo_tears` fades in over 0.35 s underneath it. For about half a second her standing sprite shows at full strength through the CG, with her face over Kōhei's. Slow-motion freeze at 250 ms: CG 57%, sprite 95% (`shots/slowmo_ipad/c2_0196_slow0250.png`). The text box stays up throughout, which is correct.
- **Repro:** c2_mop, tap from c2_0196 to c2_0197, iPad, normal speed.
- **Fix:** let the CG clear before the sprite fades in (`@cg -` then a short `@wait 0.6`, then `@show`), or in the engine, delay or lengthen sprite fade-ins while a CG is fading out.

### 5. Expressions held past their line
- c2_0044–c2_0049: Natsuki's eyes-closed `school_laugh` stays up through the reflective narration "She doesn't ask why a second-year works three shifts a week… Then they get careful with me." It also stays centre stage while c2_0047 says "she gets up without a word and starts on the other side of the room" (`qa/302_c2_0046.png`, `qa/303_c2_0047.png`). Fix: `smile` at c2_0044, `@hide natsuki` at c2_0047, and show her again for c2_0050 "I'm new."
- c2_0154–c2_0158: Natsuki's open-mouthed `kendo_surprised` for "Yes, Captain." is held while Kirishima corrects Kōhei (`qa/398_c2_0154.png`, `qa/402_c2_0158.png`). Fix: back to `smile` or `grin` at c2_0155.
- c2_0078–c2_0082: Takatsuki's `surprised` is held through his "…" and "That was a joke." (`qa/334_c2_0080.png`). Use `takatsuki_kendo_frown` at c2_0080.
- These aren't the deadpan/smirk cases that `script_lint` check 6 covers. Both smirks (c2_0160, c2_0231) correctly return to a warm face on the next Natsuki line.

### 6. Narration moves; the background doesn't
- c2_0056–c2_0299 ("I walk home up the hill… a plastic container on the kitchen table… in Nanoha's handwriting. It says 'Again.'") plays over `bg_restaurant_night` (`qa/314_c2_0299.png`).
- c2_0301 ("When I get to the house, the light's on in Nanoha's window across the gap.") plays over `bg_bridge_dusk` (`qa/492_c2_0301.png`).
- Both are Nanoha beats in a Natsuki chapter, and both locations already exist in the build (`bg_fujisawa_kitchen`, `bg_houses_night_lit`). Suggest `@bg … fade` before c2_0299 and c2_0301. Check that the kitchen plate's time of day suits night; if not, add it to `BG_LIGHT`. This is a staging call, so Production can decide it.

## Backlog (spot-check sizes, edge cases)

7. **Phone landscape 844×390, interlude:** the Chie chat panel covers the "— Interlude: Natsuki —" label (`shots/spot_844x390/c2_0266.png`). Fix: drop the chat's top offset below the label when `#ilabel` is on.
8. **c2_0288:** the chat stays up while the narration says "Natsuki put the phone down…". The engine keeps the phone up one line after the last text. That suits c2_0276 ("looked at that last message") but not c2_0288 (`qa/531_c2_0288.png`). Fix: a script command to clear the phone, or clear it on 0288 specifically.
9. **Tap during the catch video (any time after 600 ms):** `animDone` cuts the CG in under the video and fades the video out in 0.2 s. A mid-motion frame snaps to the end pose. Intended skip behavior, but it reads as a jump. Consider a 0.5 s dissolve.
10. **Insert art vs. panel briefs:** these are for the insert/on-model check; a reader isn't told any of them.
    - Page 1 panel 2: Natsuki's tip should "stay on his throat," but it points at about his waist.
    - Page 2 strike panel: Kōhei's arms are forward, not "coming up for men."
    - The kneeling club members are in bogu on page 1 and mostly without it on page 2's Kirishima panel.
11. **`bg_dojo` vs `bg_dojo_evening`:** the day plate already has long golden light, and the evening plate is only slightly warmer (scene starts in `shots/ipad_normal/scene_c2_dojo.png` vs `scene_c2_mop.png`). "The light has gone long and orange" barely reads as a change of time. Either cool the day plate, or deepen the evening plate.

---

## What I checked and found fine

**Automatic checks**
- `qa_play.py --every` at 1180×820 (`qa/report.json`, 549 shots): no script errors, no failed requests, `voice_missing` empty, `missed_lines` empty, 534 lines seen, all 13 insert steps shown. 315 of 318 spoken lines are voiced; the 3 unvoiced are the intentional "…" lines c1_0222, c2_0080, c2_0230. The only console error is `net::ERR_TUNNEL_CONNECTION_FAILED` for Google Fonts, which this sandbox's proxy blocks. That's not a build problem.
  - Note: the first `qa_play` run was killed at c2_0170 by the sandbox's memory cgroup OOM killer. This machine is shared, and `dmesg` shows the kill. The rerun above ran to the end, so it's an environment issue, not the build. The partial first run is in `qa_crashed_run1/`.
- `voice_levels.py` on `v2/voice/` (`voice_levels.txt`): 315 lines, median speech RMS −20.4 dB, range −27.0 to −19.5. Two flags, both Prologue dream lines (p_0007 −5.9 dB, p_0010 −6.6 dB): the known "intended softness?" item from §9 step 5, not Ch2. No Ch2 flags: no clipping, nothing too short, nothing mostly silent. The Ch2 clip durations are plausible for their Japanese lines.

**Voice playback**
- In a full normal-speed playthrough (tap after each line's voice ends), all 145 non-insert voiced Ch2 lines started playing, and all 6 voiced insert steps played. Audio decodes: 165 OK, 0 failed.

**Script vs. build**
- All 284 Ch2 line IDs in `ch02.ozs` are in `script.json` with identical English text and speaker. All 152 voiced lines are in `voice/index.json` and `ja.json` with matching Japanese. No stray IDs.
- All 16 glossed terms have translator's notes.

**Face windows (§3a)**
- Kōhei has a window on every spoken line, in the right outfit per `@wear`: work in c2_tuesday, kendo in the dojo scenes, school on the bridge.
- Kirishima speaks from offscreen with a window (c2_0085, 0132, 0134), and has none when on stage.
- No windows for the manager or the classmates.
- No window for Natsuki inside the catch CG (`CG_CAST`).
- Natsuki gets a POV window in the interlude (c2_0259), and none on the phone texts.

**Sprite heights**, measured at 1180×820 against `CHAR` and style guide §1b, head tops in pixels:

| Character | Height | Measured | Expected |
|---|---|---|---|
| Kirishima | 5′11″ | 9 | 8.6 |
| Takatsuki | 5′8″ | 57 | 57.2 |
| Natsuki | 5′3″ | 138 | 138.1 |
| Rika | 5′1″ | 171 | 170.4 |

The teaching sprites (shinai headroom 0.16) keep Natsuki's eye line identical to her kendo sprites.

**Tints**
- Sprites take the evening and dusk tint on `bg_dojo_evening` and `bg_bridge_dusk`.
- The lit interiors (restaurant, apartment) are untinted, which suits them.
- Face windows are untinted.

**Expressions and outfits vs. text**
- Natsuki's outfits match the text: kendo ponytail in faded indigo keikogi, school hair down, glasses and a shinai pointer for the lesson.
- Her `tears` sprite has visible tears.
- Kirishima is in a white keikogi in sprite and insert alike; Takatsuki has slate-blue hair.

**Transitions**
I logged every layer change with its CSS transition duration in a fast-tap run (521 taps through the whole chapter, about 140 ms apart), plus a normal-speed run with video, and slow-motion freeze frames.
- All fades have non-zero durations: backgrounds 0.9 s, CG 1.0 s, sprites 0.35 s, text box 0.25 s, face window 0.18 s, insert 0.6 s, phone 0.35 s, interlude tint 0.8 s, black-out 1.8 s.
- The only 0-duration change is the CG cut placed *under* the catch video at its end. The video's 0.2 s fade masks it, and the last video frame matches `cg_catch.webp` closely (mean difference 5/255, p99 25).
- No hard cuts and no stuck or hidden text box. The box stays visible through the `@cg -` fade, and it is hidden during the anim and the insert and comes back after both.
- Frozen and seen OK:
  - chapter card → date card → classroom
  - classroom → restaurant crossfade (`shots/slowmo_ipad/c2_0003_*`)
  - Wednesday date card → dojo
  - sprites in and out
  - insert open, page-to-page crossfade, panel zooms and close (`shots/slowmo_ins/`)
  - same-background re-fade at c2_debrief, which is invisible
  - dojo → evening dojo, evening dojo → bridge
  - bridge → interlude with tint and label (`shots/slowmo_ipad/c2_0251_*`)
  - phone in and out
  - fade to black → "END OF CHAPTER 2 … Chapter 3, 'Windows,' comes next." (`shots/ipad_normal/zz_end.png`)

**Manga insert**
- 10 panel boxes for 10 scripted panels, in right-to-left reading order that matches the script.
- The lettering matches the script lines, with the kendo calls paired with English captions.
- Natsuki and Kōhei swap sides after the dō pass, and Kirishima's arm points to the scorer both times.

**Art vs. text**
- The catch CG matches: arm behind her back, other hand on her forearm, a single tear, wide eyes, sweat, bucket and rag, evening light.
- The backgrounds match the narration:
  - restaurant: drink bar, register, window booths
  - bridge: streetlights, dark-blue mountains, orange river, a train, the pale Ōzakura smudge on the hill
  - apartment: crossed-out SAPPORO/SENDAI boxes, pen cup, balcony over the river with cherry trees

**Spot checks** (scene starts plus the insert and the phone chat) at phone landscape 844×390 and desktop 1440×900 (`shots/spot_844x390/`, `shots/spot_1440x900/`): everything renders, with no layout breaks beyond #7. Insert panels fill the phone screen.

**Not tested**
- Safari/iPad and listening by ear.
- Portrait, per canon §2.
- Snapshot diff (no baseline for this run).

**Caveat:** the machine was heavily loaded by other jobs (load average 13–18 on 2 cores), so measured timings are noisier than on a real device. The transition durations come from the logged CSS values rather than from frame timing, so they're reliable.

## Notes: slip → catch sampling (item 2)
Columns: ms after the tap, then the opacity of Natsuki's sprite, the anim video and the text box, then the video's readyState.
```
 58  spr .91  anim 0    box .85
181  spr .28  anim 0    box .11   rs 1
270  spr .08  anim 0    box 0
360  spr 0    anim 0    box 0
449  EVENT playing
481  spr 0    anim .05
521  spr 0    anim .29
565  spr 0    anim .68
767  spr 0    anim 1
```
