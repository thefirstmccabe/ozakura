# On-model image check (§9 step 4): Ch3 "Windows", build b3-ch3-nov2

**Scope.** `ch03.ozs` has six `@cg` lines and no `@anim`, `@insert` or `@panel` lines: `cg_window`, `cg_window_sill`, `cg_window_sill_turn`, `cg_tree_natsuki`, `cg_tree_light` and `cg_lunch` (all in `v2/img/bg/`). Four of them also have living stills in `v2/img/live/`, so I checked those too, frame by frame (84 frames each). `production/pilot-v2/art/layout/` holds only `cg_collar_layout.jpg`, so there's no layout sketch for the one multi-character CG (`cg_lunch`). I checked its seating against the narration instead.

**Read:** style guide §1–§2; the `prompts.md` Ch3 entry; the script around every CG; and these references: `refs/handoff/Nanoha-Pajamas-Bun.png`, `Nanoha-School-Loose.png`, `Natsuki-Athletics-Ponytail.png`, `refs/locations/window-night-from-kohei.png`, `houses-street.png`, the sprites in `v2/img/ch/` (nanoha_home, natsuki_track, natsuki_kendo, akane_home, mio_home, genji_shrine, emi_home), Kōhei's face window `v2/img/face/kohei_smile.webp`, and the plates `bg_kohei_room_night`, `bg_kohei_room_night_dark`, `bg_shrine_tree_day` and `bg_tachibana_living`.

**Method.** All coordinates are full-resolution pixels (2400×1340) unless I say otherwise. I measured heights and head sizes on grid overlays every 20 px, with color masks (copper hair, pale-blue scrunchie), row-by-row luminance profiles and difference images against the plates and the previous CG. I checked alignment between consecutive CGs by phase correlation.

---

## 1. `cg_window` (lines 66–72, c3_0100–c3_0105): **FAIL (minor, craft)**

- **On model: pass.** The bun sits on top of her head. The scrunchie mask measures 166×60 px (x 647–813, y 480–540): 0.58 of her face width and 0.22 of her head height (crown to chin, 275 px). In the pajama reference it's about 0.13 of head height, so this is the puffier scrunchie §1 asks for. The pale-blue pajamas have white piping. Her eyes are brown. A hair sample reads #4e3835 against the #51423d swatch. The face matches `nanoha_home_smile` (soft oval, straight fringe). The cat on the pocket is hidden by the rabbit, which is fine.
- **Scale: pass.** The window opening is about 885 px tall, or 3.2 of her head heights. She leans about a foot in front of the window plane, which makes the window roughly 3 to 3½ ft tall, which is plausible. The rabbit is about 350 px tall (1.3 head heights, roughly 11 in), and it stays that size across all three window CGs (sill 362 px, turn 375 px).
- **Matches the text: pass.** She's leaning on the sill in pajamas with the bun and scrunchie, holding the white rabbit in both hands, with a solemn straight face. The window is open: the left sash has slid behind the right, and her forearms and the rabbit's feet overlap the bottom rail. It's night and her light is on. One small point: she holds the rabbit at arm's length at chest height rather than snug under her chin (ear tips at y≈815, chin at y≈795, rabbit's head y≈890–990). I'm passing that, because the ears reach her chin.
- **Location and continuity: pass.** The CG matches the locked `window-night-from-kohei.png`: a sliding two-sash window on a plain wall, with Kōhei's own sliding sash and crescent latch at the right edge (x≈2045–2160). The flower paintings have no text, as the prompt asks. The background lines up with `cg_window_sill` to within 1 px, so the swap doesn't jump. The plate shown before this CG contradicts it; see §7.
- **Canon and content: pass.** The framing is modest, and both hands are complete.
- **Craft: FAIL.** A **2-px black column runs down the right edge** (x 2398–2399). Column mean luminance there is 20 and 2, against 68–73 just inside, and 1,269 of 1,340 rows fall below 30. `cg_window_sill` has no such line (its edge column reads 71), so the line appears and then vanishes on the next swap. It's probably padding left over from the crop-and-redraw step.
  - **Fix (code):** copy column 2397 into 2398–2399, or crop 2 px and rescale, then re-export the webp and thumbnail.

## 2. `cg_window_sill` (lines 73–103): **FAIL (text match)**

- **On model: pass.** Same design as `cg_window`, with a soft smile and a blush.
- **Scale: pass.** See above.
- **Matches the text:**
  - Pass for c3_0106. The rabbit sits on the left corner of the sill (x≈290–495, y≈818–1180) with its back and round tail to Kōhei's window. Her chin (y≈1035) rests on her right hand, which is folded on her forearm (y≈1040).
  - **FAIL for c3_0113–c3_0118.** At c3_0113, "I turn him around to face the window," the rabbit faces Kōhei until c3_0119, "She turns him back around." For those five lines (c3_0114 "Kōhei." through c3_0118 "My authority is absolute."), the CG still shows the rabbit's back and tail. Nothing changes between `@cg cg_window_sill` (line 73) and `@cg cg_window_sill_turn` (line 104), so the joke plays against a picture that contradicts it.
  - **Fix (smallest):** add a rabbit-facing state shown from c3_0113 and switch back to `cg_window_sill` at c3_0119. Build it with the same recipe as the turn: a region edit of the rabbit only (x .10–.255, y .57–.965) composited back with `region_composite.py`, with the front-facing rabbit in `cg_window` as the reference. The prompt log says the edit model wouldn't face the rabbit to the frame (852 and 853). If it still won't, paste `cg_window`'s rabbit head over the sill rabbit and repaint the paws by hand.
- **Location and continuity: pass.** Aligned with `cg_window` (≤1 px).
- **Canon, content and craft: pass.**
- **Living still (`live/cg_window_sill.mp4`): pass, with an advisory.**
  - The loop is effectively static. Across the loop only 48 px change by more than 20 levels, and the median frame-to-frame change is 0.04 levels, so the curtains don't visibly stir. The face hold is invisible and the loop seam is clean (0.8).
  - The video plays about 4 levels darker than the master (signed RGB −3.8/−4.1/−3.7), so there's a faint dip if the player cuts from the still to the loop.
  - Files are 84 frames (3.5 s), while `prompts.md` says they were trimmed to 96.

## 3. `cg_window_sill_turn` (lines 104–109): **PASS**

- The only change is the rabbit. Against `cg_window_sill`, everything outside the pasted region is encoding noise (1,333 px over 30 levels, mean 1.06), so there are no seams at the composite edges.
- The rabbit is in profile facing right, toward her: a quarter turn, as c3_0314 says. That also matches c3_0164 later ("still sitting sideways"). Its size and design match the sill version.
- Living still: same result and advisory as §2 (no visible motion, 3.7 levels darker, seam 0.74).

## 4. `cg_tree_natsuki` (lines 191–193): **FAIL (on model: hair; content: framing and outfit)**

- **On model, hair: FAIL.** I measured with a copper mask.
  - In this CG her head runs from crown y 686 to chin ≈y 820 (134 px). The ponytail is tied at ≈y 728, about 30% of the way down the back of her head, and runs to y 1058: 2.46 head heights, ending 74% of the way from the shoulder line (≈y 850) to the waistband (≈y 1130). It is about **100 px wide at y 880–960, or 0.75 head heights**, and falls in big S-curl ringlets.
  - In `natsuki_track_smile` (head ≈385 px), the ponytail is tied at the crown and its visible width is 100–117 px, **0.26–0.30 head heights**, with smooth, gentle waves.
  - In `cg_lunch` the same afternoon, the ponytail is 0.38–0.45 head heights wide and also tied at the crown.
  - So the tree CG's ponytail is about 2.5–2.9× fuller than the sprite's and about 1.7–2× fuller than the lunch CG's. It's also tied lower and is curlier. That's exactly the drift §2 warns about ("longer, bigger and messier"). Length is *not* a fail: the lunch CG's ponytail is about as long (≈2.35 head heights), and the sprite's disappears behind her shoulder, so I can't measure it there.
- **Outfit and content rule: FAIL.**
  - The sprite and §2 give "dark sweats": loose, straight-leg drawstring joggers. Here they're **fitted**, with a center seam and shading that models the seat. Her waist is ≈145 px at y 1080 and her hips ≈190 px at y 1200 (≈1.3×).
  - The crop ends at upper thigh, so her rear (x≈510–700, y≈1150–1340) is the largest, nearest shape at the bottom of the frame. For a 16-year-old, that's the figure-emphasis framing §1 rules out ("never design or frame the school-age cast for figure or sex appeal").
  - The track shirt is also a fitted crew top with a dark collar band, not the sprite's quarter-zip. That's minor.
- **Fix (one edit pass covers both failures):** an edit of the figure only, with `natsuki_track_smile` as image 1, asking for:
  - "high ponytail tied at the crown, slim, smooth with soft gentle waves, never curly"
  - "loose straight-leg dark drawstring joggers as in image 1, relaxed fit, no seat shading"
  - "navy quarter-zip track top"

  Composite it back over the master with `region_composite.py` so the plate stays put.
- **Scale: pass.**
  - Her feet are out of frame, so I used the ground plane. The edges of the stone path converge at y≈980, which I took as the horizon. The torii pillar measures 615 px from its base (y≈1200) to the top beam (y≈585). Projected about 7 heads tall (≈940 px), she stands about 2.9× nearer the camera than the torii, which is consistent with her figure being cut at the thighs.
  - The implied camera height is about 3½ ft. That's a low camera rather than Kōhei's eye, which is fine for a non-POV CG.
  - The trunk measures 405 px wide at the torii's depth. If the torii is 10–13 ft tall, the trunk is 6.6–8.4 ft across, which fits "three adults couldn't link arms around it."
- **Matches the text: pass.** She has stopped dead with the camera up (c3_0368–0369). Her hair is still up from practice, she wears the navy track top, and the camera is a heavy black DSLR. The torii, boulder, low level branch, valley, river and town are all present, and every branch is in bloom.
- **Location and continuity: pass.** This is a regeneration of `bg_shrine_tree_day`, not a paste onto it. It's aligned within 1 px, with a mean color shift under 4 levels (R +3.6), so the cut plate → CG → plate doesn't jump. Only the petals re-scatter, which reads as natural.
  - Advisory: the stone path at bottom left is empty and unswept. The next line (c3_0185) puts Nanoha on that path sweeping "neat pink drifts" with a second broom against the lantern, and the plate behind her sprite has no broom either. Accept this as a reveal, or add the broom to the plate.
- **Hands and anatomy: pass.** The right hand is on the grip, the left cradles the body, and the strap hangs down.
- **Living still: pass.** The petals fall. The ponytail doesn't actually move, which is fine. The loop seam is within normal frame-to-frame change (1,102 px over 40 levels at the seam, against an in-loop median of 448 and a maximum of 1,310), and the video is about 2 levels darker than the master.

## 5. `cg_tree_light` (lines 225–228, c3_0263): **PASS (advisory)**

- The CG is the shipped plate plus one code-drawn light (`tree_light.py`): a core of radius 7.5 px and a halo of 20/60 px at (1236, 757). Outside the light, the file differs from the plate only by encoding noise (max 51 levels, on line edges). The place is identical, it's daytime, the low branch is in place, and nothing contradicts the text. The point reads clearly: core luminance 234 against 76–122 in the plate behind it.
- **Advisory:** the core sits *on* the bark, not in the air under the branch. Along column 1236 the branch's underside ends at y≈768, 11 px below the center. Along row 757 the crook ends at x≈1265, 29 px to the right. The halo spills below the edge, so the glow reads as being at the branch's underside where it joins the trunk.
  - Moving it 20–25 px lower, to y≈780–790, puts it in air, but against a background of luminance 200–215 where a white glow barely shows. That's the trade-off the Nov 1 cold read already settled, so I'm not failing it.
  - If the author reads "on the branch," the cheapest change is to shift the point to about (1258, 772), the crook corner, with half the halo still against dark bark.

## 6. `cg_lunch` (lines 301–308, c3_0411–c3_0416): **FAIL (outfit continuity; three minor items)**

- **Matches the text, seating: pass.**
  - Grandpa sits on Kōhei's right (the right side of the frame).
  - Mio sits between Akane and Natsuki on the far side.
  - Nanoha sits next to Emi on the left.
  - Kazuo is absent.
  - Everyone has hands together, Mio is leading, and Natsuki's mouth is open, so she's loudest.
- **Matches the text, food: pass.**
  - Karaage piled in a mountain.
  - A pyramid of onigiri.
  - **Two** plates of tamagoyaki, front left and far center.
  - The big bowl of kinpira (burdock and carrot).
- **On model: pass** for:
  - **Emi:** dark low bun, light-blue shirt, mustard apron.
  - **Nanoha:** hair long and loose, cream cardigan over a lavender top, as in `nanoha_home_smile`. That sprite has no clip, so there's none here either.
  - **Akane:** lavender-silver hair, small clip on her left, cream cardigan over a pink top.
  - **Mio:** blunt bob, braid on her left, mint star T-shirt, bandage on her right elbow.
  - **Natsuki:** quarter-zip track top, ponytail tied at the crown.
  - **Genji:** white tenugui headband, dark samue.
  - Hands: I checked all seven pairs at zoom, and every finger count and joint is fine.
- **Scale: pass.** Crown and chin on the grid, with head height in px:

  | | Crown y | Chin y | Head (px) |
  |---|---|---|---|
  | Emi | 275 | 540 | 265 |
  | Genji | 310 | 575 | 265 |
  | Nanoha | 312 | 525 | 213 |
  | Natsuki | 285 | 485 | 200 |
  | Akane | 288 | 475 | 187 |
  | Mio | 385 | 545 | 160 |

  - Head sizes follow depth order: the near-side adults first, then Nanoha mid-left, Natsuki at the far corner, and Akane and Mio on the far side.
  - Akane and Mio sit at the same depth. Mio's crown is 97 px lower, about 4.7 in at ≈20.8 px/in, against about 6½–7 in expected for kneeling heights of 5′0″ and 4′0″. Mio is sitting up a little, which is within posture tolerance.
  - Natsuki's crown sits level with Akane's when she should be about 1½ in higher seated. That's also within posture and measurement tolerance (the horizon, from the table's receding edges, is only good to ±20 px). No fail.
- **Problems:**
  1. **Kōhei's sleeves don't match his outfit (FAIL, moderate).** The POV sleeves are pale sage-gray with white cuffs: the median of RGB samples at (1010–1060, 1310–1338) and (1320–1380, 1310–1338) is (160,172,162) and (156,168,157). `@wear kohei school` has been in force since c3_steps (line 149), and every Kōhei line in this scene shows `kohei_smile` etc. in a navy blazer and white shirt (swatch #3f4050). The face window and the CG disagree on screen.
     - **Fix (code or edit pass):** recolor the two sleeves to the navy blazer (#3f4050), with a white shirt cuff showing at each wrist.
  2. **"Miso soup for everyone" (c3_0412) isn't true (minor).** There are six miso bowls for seven diners, and the POV place in front of Kōhei's hands has no soup, rice or chopsticks. Mio also has no rice bowl (five rice bowls in all).
     - **Fix:** an edit pass adding a miso bowl, rice bowl and chopsticks at the near edge, in front of the POV hands (and rice for Mio). Or accept it: the text-change alternative ("Miso soup all round") still contradicts the empty place.
  3. **Mio's face (minor, on model and text).** Her eyes are shut in a laughing arc, which doesn't read as "already supervising" (c3_0413). Her open mouth shows a continuous row of upper teeth, with no trace of the gap-toothed grin in §2 and her sprite. All six faces at the table also share the same closed-eye smile, which makes the group read uniform.
     - **Fix:** an edit pass on Mio's face only: eyes open and side-eyeing the table, with the gap tooth showing.
  4. **Baked-in text on the calendar (minor, content rule).** The calendar header (x≈630–800, y≈180–420) renders pseudo-Latin glyphs ("OAL SSLESL") and numbers ("15", "25"). The plate's calendar shows only dots.
     - **Fix (code or edit):** paint the header and numbers out to plain dots, matching `bg_tachibana_living`.
- **Location and continuity: pass.** The CG matches `bg_tachibana_living`: family photos and a child's drawing on the left wall, the calendar, the TV, the garden door with its cherry tree and stone lantern, the kitchen to the right and the bookshelf. The camera is closer and the table larger, which is fine for seven diners. The light comes from the garden, and it's daytime.
- **Living still: pass, with an advisory.** The loop is effectively static: only 138 px change by more than 20 levels, and the steam doesn't visibly move. The face holds are invisible. The video plays about 4 levels darker than the master.

## 7. Plates around the window CGs (continuity; outside this check's pass/fail, reported because they sit next to the CGs)

1. **`bg_kohei_room_night` (shown from line 61, just before `cg_window`).**
   - It draws Kōhei's window as an **outward-swinging casement that's already open**. That contradicts c3_0099 ("I open my window") and the CG's sliding sash with crescent latch, which matches the locked `window-night-from-kohei.png`.
   - Across the gap, Nanoha's window shows drawn curtains and nobody at it, but c3_0096 says "her window's open, and she's waiting."
   - Her window frame projects at about half the height of his (≈345 px against ≈690 px in the crop), which puts it noticeably more than three feet away for a camera across the room.
   - **Fix:** re-shoot the plate from the locked window views with a sliding sash, shut until line 65 (or start the scene on a variant with his window shut), and her window open and lit.
2. **`bg_kohei_room_night_dark` (line 111 onward).** Nanoha's sill has **no rabbit**, but c3_0164 says "On her side of the glass, the rabbit is still sitting sideways."
   - **Fix (code):** paste a small, darkened, sideways rabbit (from `cg_window_sill_turn`) onto her sill corner in the plate. Or change the text to say he can't see it now.

---

## Summary of failures

| # | Image | Problem | How checked | Smallest fix |
|---|---|---|---|---|
| 1 | `cg_window` | 2-px black column on the right edge (x 2398–2399) | Column luminance 20/2 against 68–73 inside, 1,269/1,340 rows below 30; absent from the next CG | Code: copy column 2397 outward, re-export |
| 2 | `cg_window_sill` | Rabbit shows its back during c3_0114–c3_0118, while the text has it turned to face Kōhei | Script order against the CG lines; no image change between lines 73 and 104 | New rabbit-facing state via region composite (turn recipe), shown at c3_0113, back at c3_0119 |
| 3 | `cg_tree_natsuki` | Ponytail too full, curly, tied low (off-model drift) | Copper mask: width 0.75 head heights against the sprite's 0.26–0.30 and the lunch CG's 0.38–0.45; tie about 30% down the head against the crown | Figure-only edit pass with `natsuki_track_smile` as image 1, composited back |
| 4 | `cg_tree_natsuki` | Fitted sweats with seat shading, framed at the bottom-center foreground (school-age modesty rule); sprite has loose joggers | Grid: waist ≈145 px, hips ≈190 px; seat at x≈510–700, y≈1150–1340; sprite comparison | Same edit pass: loose drawstring joggers, no seat shading, quarter-zip top |
| 5 | `cg_lunch` | Kōhei's POV sleeves are sage-gray (RGB ≈160,172,162), but his face window shows the navy blazer (`@wear kohei school`) | Pixel samples against swatch #3f4050 and `kohei_smile` | Recolor the sleeves to navy with white cuffs |
| 6 | `cg_lunch` | "Miso soup for everyone": 6 bowls for 7 diners, POV place empty, Mio has no rice | Bowl count by place | Edit pass adding bowls at the POV place (and rice for Mio) |
| 7 | `cg_lunch` | Mio's eyes closed (not "supervising"), no gap tooth; six identical closed-eye smiles | Face zoom against `mio_home_smug`, §2 | Edit pass on Mio's face only |
| 8 | `cg_lunch` | Pseudo-text baked into the calendar ("OAL SSLESL", "15", "25") | Zoom against the plate's calendar | Paint out to dots |
| 9 | `bg_kohei_room_night` (plate) | Casement window already open, her window closed and empty, gap reads wider than 3 ft; contradicts the CG and c3_0096/c3_0099 | Plate against the CG and `window-night-from-kohei.png`; window heights ≈345 vs ≈690 px | Re-shoot the plate from the locked window views |
| 10 | `bg_kohei_room_night_dark` (plate) | No sideways rabbit on her sill (c3_0164) | Zoom of her sill | Paste in a darkened sideways rabbit |

**Advisories (not counted):**
- `cg_tree_light`: the point sits on the bark at the branch's underside rather than below it. Optional move to about (1258, 772).
- The living stills for `cg_window_sill`, `cg_window_sill_turn` and `cg_lunch` show no visible motion.
- All four living stills play 2–4 levels darker than their masters.
- The living stills are 84 frames, not the 96 the prompt log states.
- `cg_tree_natsuki`'s path shows no Nanoha or drifts just before c3_0185 introduces her there, and the plate lacks the second broom.
- `cg_window`'s rabbit is held at chest height rather than snug under her chin.

**Passes:** `cg_window_sill_turn` and `cg_tree_light` pass outright. `cg_window` fails only on the edge line. Faces, swatches, scale and locations are otherwise on model across all six CGs.
