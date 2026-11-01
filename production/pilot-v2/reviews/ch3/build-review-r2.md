# Ch3 "Windows": build review, fix round (Nov 1)

**Scope:** one fix round, `2e600de..7f91fc0` (v2/index.html, ch03.ozs, dark_window.py, the dark plate and the four living stills), answering `build-review.md` and `onmodel-r1.md`. Prompt: `production/pipeline/review/build-review.md`. No snapshot diff was supplied, so I used freeze frames instead.
**How:** Chromium/Playwright with local fonts, landscape only. iPad 1180×820: c3_home → c3_window → Saturday card and c3_lunch at normal speed, with freeze frames on every changed transition; c3_window and c3_lunch to the end card with real clicks every 110 ms; the tree CG coming up; save/load at c3_0164. Phone 844×345 (notch left, 2×) and desktop 1440×900: the chapter menu and the key lines. The living stills were also measured frame by frame against their stills and the old clips. Shots and scripts are in the session scratchpad, `review2/`, not the repo.

## Problems (nothing must-fix)

**1. The dark-window plate leaves warm light outside its box. Should fix: cheap, code only.** Seen on c3_0163, c3_0164, c3_0323 and the Saturday card, most clearly at desktop 1:1 (`review2/desk_dark_crop.png`, `review2/glow_pair.png`). `dark_window.py` darkens only x 1788–2188, y 314–656 (of 2400×1340), but the lamp light reaches past that:
- **Left of the frame:** a peach rim on the frame and wall at about x 1745–1790, y 470–600. It is pixel-for-pixel the same as in the lit plate, so a faint glow stays beside a dark window.
- **Top:** a 3–4 px warm sliver along the top of the right pane, at about x 2140–2175, y 309–313.
- **Bottom:** the lower frame rail is pulled to the same navy as the glass. This is the "smudge under her sill" the handover already lists.

*Fix:* widen the box about 45 px left and 8 px up (x0 ≈ .726, y0 ≈ .229). Cool and desaturate only the warm pixels in that outer ring, so the gray frame keeps its value. Stop the mask about 6 px above the rail.

**2. The plate crossfade dims Kōhei's room just as her light goes out. Optional; engine.** c3_0322 → c3_0163, all sizes, normal speed. `setBg` fades the old plate out while the new one fades in, so for about half a second the black backdrop shows through. At about 450 ms the lit plate is at 0.42 over the dark one at 0.58, so about 24% of the backdrop shows, and the CG is still at 0.32. Screenshots measure the wall and desk 16% darker than when settled, recovering by about 1.5 s. The room seems to brighten while her window darkens. It is mostly hidden by the CG fading out, and it reads as "the light goes out", not as a glitch.
*Fix (carry list):* in `setBg`, keep the old plate opaque until the new one has faded in, as `setCg` already does with `over`. Every mid-scene plate change would lose the dip, so it needs a regression run.

**3. Emi's last line hangs over the living room during the new wait. Optional.** c3_0285 → c3_0406, normal speed, every size. During `@wait 0.9`, the box still shows "Barging? … Akane-chan's already here." with the Tachibana Emi tag, but Emi is gone and the room is fading in (`review2/sheet_lunch2.jpg`). Then Mio arrives. It isn't wrong, just slightly stale.
*Fix, if wanted:* hide the box for a `wait` that follows a `bg` in the same step (`line()` shows it again). This matches how the box hides while a CG comes up from none.

**4. Fast taps skip the new waits (expected).** With taps every 110 ms, Mio appears over the half-faded house front (c3_0406), and Emi over a plate still fading in (c3_0283), because a tap ends a `wait`. At normal speed both are right. This is covered by the carry-list engine option from the last review (hold a `show` that comes in the same step as a `bg` until the plate is up).

**5. Docs.** pilot-notes §7, "Running bits", still says "facing the corner means a reduced sentence". §3 and the handover now say he faces her. The handover's `{FINAL_QA}` is still open, which is expected until the final runs.

## Each claimed fix, verified
1. **Chapter menu.** Three cards at every size: iPad x 100–832; phone 47–828 of 844, clear of the notch; desktop 230–962. Chapter 3 plays its chapter card, then "Thursday, April 10", then c3_0309 over the night houses plate. The `cg_window` thumbnail shows Nanoha at her window and the rabbit. It isn't a peak or a spoiler, so I'm fine with it over a background plate.
2. **The sill CG at c3_0106.** It crossfades from `cg_window` with the box up and no cut. Lines c3_0106–c3_0120 play over the rabbit set down with his back to Kōhei. c3_0312 is gone from the script, `script.json` and every reference. `script.json` recompiles byte-identical from the .ozs files. Note: his tail is under the box at every size, but his head and ears read as "back to me".
3. **The rabbit's direction.** In `cg_window_sill_turn` he is in profile facing right, at Nanoha. At iPad his eye and nose show above the box on c3_0314 (`review2/rabbit_ipad.png`). "Facing her instead" and "sitting sideways, halfway out of trouble" both match the art.
4. **The window goes dark.** The dark plate holds from c3_0163 through c3_0164, c3_0323 and the Saturday card at all three sizes, and after save/load at c3_0164 (the slot thumbnail too). The lit window shows only under the fading CG and is gone by about 0.9 s, in step with the line. See problems 1 and 2 for the remaining polish.
5. **Akane.** "Barely open" and "She squints up at me" fit the half-open `akane_home_sleepy` eyes.
6. **The lunch seating.** c3_0413 matches `cg_lunch`: Genji at the near right, Mio between Akane and Natsuki, Nanoha beside Emi. It makes no claim about an empty place.
7. **Entrances.** Emi first shows on the tap to c3_0283, over the house front. Mio comes in after the living room has fully faded in: her sprite is at 0.03 opacity at about 0.8 s and her line starts as she fades in.
8. **Emi on the floor.** Her sprite bottom is at 821/820 (iPad), 346/345 (phone) and 901/900 (desktop). Her trousers run to the last pixel row below the box, and her head height is unchanged.
9. **Living stills (84 frames each).**
   - **Tree loop point:** petal-size changes over 60/255 dropped from 47 to 13, within an ordinary frame step's 1–12. Frame by frame, the petals keep moving across the wrap, with no blinks (`review2/blob_tiles.png`).
   - **Sharpness:** the step at the loop point went from 3.5–4% to under 1% on all four clips. What's left is a faint codec grain change (mean 0.7–1.9/255, was 1.1–2.5). In-game the tree's loop step measured 0.6/255, which can't be seen.
   - **Alignment and fade-in:** the clips sit within 0.07 px of their stills. The held faces (Nanoha and the rabbit; the six diners; Natsuki) are still held and match the still. The clip now starts 0.5 s into the source, but the engine fades it in only after about 1.15 s of playback, so the dissolve from the still is the same as before: about 15 petals cross-dissolve, and nothing jumps (`review2/tree_nat_fade.png`).
- **The earlier three fixes still hold.** No Nanoha face window on the turn CG (c3_0315, c3_0162; checked at iPad, phone and desktop), and Kōhei's window still shows on c3_0322. On the phone the window CGs crop from the bottom and the rabbit's head is above the box (box top 251). Genji's height is still 58.

## Also fine
- **Fast taps:** all 42 c3_window lines and 35 c3_lunch lines appeared. No CG or sprite was left on screen, the box was never missing, and the end card shows.
- **Other checks:** no console errors or failed requests at any size. No voiced line or voice file changed; every edit is narration, so no retakes are needed. Ch1–2 don't use `emi_home` or anything else this round touched.
