# On-model image check (§9 step 4): Ch2, build of Oct 25

Reviewer: independent art check, run on the ROOT checkout only.

**What Ch2 shows** (from the `@cg`, `@anim` and `@insert`/`@panel` lines in `production/pilot-v2/script/ch02.ozs`):
1. `@insert ins_match`, 3 pages and 10 panels (`v2/img/ins/ins_match/page1–3.webp`, geometry `ins_match.json`), at c2_0139–c2_0150
2. `@anim cg_catch` (`v2/img/anim/cg_catch.mp4` and `.webm`, 3.04 s, 73 frames at 1920×1072), at c2_0188
3. the CG it holds on, `v2/img/bg/cg_catch.webp` (2400×1340), through c2_0196 (`@cg -` at line 273)

**References used:** style guide §1–§2 (the swatches, heights, outfits and Natsuki's face A); `art/prompts.md` (the Ch2 sections, the catch, the insert and the round 1 fixes); `insert-match/insert-script.md` and `insert-spec.json`; `refs/inventory/bogu-kohei.png` and `bogu-natsuki.png`; `refs/design-oct10/r3/kohei-short-A.png`; the sprites `natsuki_kendo_{smile,laugh,grin,tears}` and `kirishima_kendo_calm`; `refs/lineup/lineup-1-school.png`; and the plates `bg_dojo` and `bg_dojo_evening`. `production/pilot-v2/art/` has no layout sketch for these pieces (its only one is `cg_collar_layout.jpg`, for Ch1).

**Method:** I cut every panel from the composed pages at the panel boxes in `ins_match.json`. I measured on gridded crops (10 to 20 px grids, labelled in source pixels), sampled colours as medians over boxes, and extracted all 73 animation frames to diff them against the CG.

**Scale targets** come from the lineup, measured on a 10 px grid. Head length (crown to chin): Natsuki 71 px and Kōhei 74 px, a ratio of 0.96. Eye line to chin: 30 and 32 px, a ratio of 0.94. Standing height ratio: 63/69, or 0.913.

---

## 1. `ins_match` page 1 (p1-1, p1-2, p1-3): **FAIL (minor)**

**Passes:**
- **On model.** Kōhei: navy keikogi, hakama and bogu with a dark-red dō, as in `bogu-kohei`. Natsuki: dusty-blue gi, black dō and a long copper ponytail out of the back of her men. Her gi hue measures 216° in p1-1, 226° in p1-2 and 222° in p1-3, against 228° on the sprite, with no violet drift. Her ponytail measures RGB 151/89/63, against the swatch #b55e36. Kirishima has a black crew cut, a white gi and a navy hakama, matching his sprite.
- **Men on in every panel.** Both fighters are barefoot. No hands are missing or extra.
- **Screen direction.** Kōhei is on the left and Natsuki on the right in all three panels. In p1-2 she stays on the right, in the foreground.
- **p1-2 text match.** His shinai is lifted vertically, which is the men feint. Extending her blade's line from her hands (800, 590) through her tip (660, 395) in the half-size view reaches about (565, 262), which is his chin and throat. So her tip is aimed at his throat, as "her tip stays on his throat" requires.
- **p1-3 text match.** He commits with his arms up. Her shinai rises toward his raised wrists.
- **Light** comes from the left-hand windows, as on the `bg_dojo` plate.

**Problems:**
- **P1. p1-1: the shinai cross at mid-blade, not at the tips.** Measured at 1:1 in panel pixels: Kōhei's tsuba is at (1285, 770) and his tip at (1770, 600), so his blade is 514 px long. Natsuki's tsuba is at (1660, 770) and her tip at (1180, 600). The two tsuba are only 375 px apart, which is 0.73 of a blade length, so each tip sits about 110 px past the other fighter's tsuba, over the hands. Tips crossing by a few inches needs the tsuba about 1.9 blade lengths apart, so the fighters are drawn about 2.6× too close for "shinai tips crossed" (c2_0138 and the panel line). A reader who knows kendo will see two people already inside striking range.
  - Smallest fix: accept it as a [P] license, alongside the sonkyo that is already accepted as not drawn. A real fix is a reroll at wider spacing; an edit can't correct this without moving the bodies.
- **P2. p1-2: the dojo is rotated 90°.** In p1-1 (and p2-2) the kamidana and name boards are on the wall behind Kirishima, which is perpendicular to the line between the fighters. p1-2 looks along that line, from Natsuki toward Kōhei. The kamidana should therefore be on the right-hand wall. Instead it is straight ahead, above Kōhei, because the plate's front view was reused.
  - Smallest fix: accept it as manga license, or do one edit pass that repaints the back wall behind Kōhei as the plate's side wall (lattice windows and the shinai rack).
- **P3. Baked-in pseudo-text.** The name plaques in p1-1, p1-2, p2-2 and p3-1, and the zekken on the kneeling members in p1-1 and p3-2, carry pseudo-kanji. Zoomed 2× on p1-1, some glyphs look Latin ("Hb", "o", "c"). The shipped `bg_dojo` plate has the same kind of plaques, so this matches the location, but it breaks the no-text rule and a Japanese-pass reader will catch it.
  - Smallest fix: a code pass that softens the plaque and zekken glyphs into illegible brush marks (a box blur plus a smudge), or accept it to match the plate.
- **P4. Kōhei's arms go back down between p1-3 and p2-1.**
  - In p1-3 his fists are above his head: fists at y ≈ 0–90 against his men top at y ≈ 170 (panel px).
  - In the next beat, p2-1 ("as his arms come up"), his hands are at chest and chin height: y ≈ 560–760 against his men top at y ≈ 170.
  - The motion reads backwards. It also undercuts debana, since he is fully committed before her strike.
  - Smallest fix: accept it, or an edit pass on p1-3 (his arms only) bringing his fists to about forehead height.

**Note (not counted):** p1-1 still shows a one-knee kneel rather than sonkyo. It was already accepted on Oct 24, and "crouch" in the script tolerates it.

## 2. `ins_match` page 2 (p2-1 to p2-5): **FAIL**

**Passes:**
- **Reading order.** The right-to-left order in `ins_match.json` puts p2-2 (right) before p2-3 (left) and p2-4 (right) before p2-5 (left), which matches the script order.
- **p2-2.** Kirishima raises his left arm (image right) toward Natsuki's side; she was on the right in p2-1. He is on model, and the kamidana behind him matches p1-1. The eight seated members are varied faces, not clones, and I compared them side by side.
- **p2-3.** Kōhei's eyes are brown. His hair samples at RGB 56/44/41 against the swatch #3d3232 (61/50/50), so it is dark brown, not black. There is a bead of sweat.
- **p2-4.** Natsuki's eyes are green and she is laughing, with sweat. The face is face A's laugh and grin family. Her lid opening is about 0.35 of eye width, against 0.43 on `natsuki_kendo_grin` and 0.73 on `_smile`, measured on 4× grids, so the narrow eyes come from the laugh, not drift. The white dots on her cheek match face A's blush highlights.
- **p2-5.** Text match: back at the line with tips crossed. Scale passes. On grids, Kōhei measures 230 → 1080 = 850 px from men top to sole and Natsuki 307 → 1075 = 768 px, a ratio of 0.904 against 0.913. Her gi hue is 227°, and there is no seam from the hue shift.

**Problems:**
- **P5. p2-1 (should fix): the kote lands on his tsuba, not his wrist.** At 1:1, her blade runs from (700, 320) through the spark at (520, 230) and his tsuba at (500, 200) to her tip at (265, 70), all in crop pixels. At his wrist (x ≈ 355, where the glove cuff meets the bare forearm at y ≈ 185–250), her blade is at y ≈ 122, which is about 60 px above the wrist and not touching it. The spark is centred on the tsuba and the top of his fist.
  - This contradicts the panel line ("her strike lands on his right wrist"), Natsuki's lesson ("Kote. The wrist."), and Takatsuki in the debrief ("you were on his wrist").
  - Smallest fix: an edit pass on a crop around the hands. Lower her blade a few degrees about her hands so its last third lies across his right glove cuff, and recentre the spark there.
- **P6. p2-1: Kōhei's tare is maroon.** The hanging tare flap below his dō samples at RGB 69/37/46 (hue 340°). On page 1 and in p2-5, p3-1 and p3-2 his tare is navy (38/38/55), as in `bogu-kohei`. The Oct 24 recolour box fixed his men but missed the tare. Two smaller things:
  - The men's grille rim is half red and half blue where that box cuts across it.
  - There is a small orange speck on his hakama, at about panel (720–730, 870–900).
  - Smallest fix: code. Apply the same boxed hue shift to the tare flaps (toward 232°, with lightness about ×0.55 to match 38/38/55), touch up the rim, and paint out the speck.
- **P7. p2-5 (should fix): the kamae is drawn as deep fencing lunges, and the blades cross at mid-blade.**
  - Stance: Kōhei's feet are 422 px apart, centre to centre, against a figure height of 850. That is 0.50 of his height, about 2′11″ at 5′9″ plus the men. Natsuki's are 427 px apart against 768, about 3′0″.
  - In chudan the feet are roughly a foot apart, with the right foot just ahead and the left heel up.
  - Blades: the tsuba are 386 px apart against a blade length of 451 px, 0.86 of a blade, so each tip reaches past the other's tsuba.
  - This is the static "back at the line" frame, right after a chapter that spends a scene on correct kamae (c2_0118, c2_0125). Readers have just been told what it should look like.
  - Smallest fix: reroll p2-5 asking for upright chudan kamae with a narrow stance (right foot slightly ahead, left heel raised) and only the last few inches of the shinai tips crossing.

**Notes (not counted):**
- In p2-3 and p2-4 the fringe hangs out below the tenugui, which c2_0292 has "tied tight over my hair". This is a common manga convention.
- In p2-4 there is a small white glint at the lower lash line of her left eye, about 6 px at panel scale. It reads as a highlight, not a tear.
- The club does not stay consistent. In p1-1 four members along the side walls all wear men. In p2-2 eight members along the back wall wear none. In p3-2 seven members are mixed.
- Two members have light ginger or brown hair (the girl with a bun in p2-2, the bob in p3-2; hue 23–27° against Natsuki's 18–19°). They thin out the distinctiveness of her copper. Optional: darken them.

## 3. `ins_match` page 3 (p3-1, p3-2): **FAIL (minor)**

**Passes:**
- **p3-1.** Natsuki leaps in with her shinai raised for men, and Kōhei lunges low and cuts across her body. "Left foot forward (the wrong foot)" is legible:
  - His back foot is seen from the front with its big toe on the image-right side, which makes it his right foot.
  - His front foot shows its arch to the camera, which makes it his left foot.
  - This supports Takatsuki's line in the debrief.
  - The raw panel is 2048 px, upscaled 1.43× to 2920. At 1:1 the line work is soft but clean, and on device the panel is shown downscaled, so it's fine.
- **p3-2.** The two have passed each other: Natsuki is now on the left and Kōhei on the right. Kirishima's raised left arm (image right) points toward Kōhei's side, as the script requires. Men are on.
  - Scale, measured on 2.5× grids: Natsuki 204 → 1160 = 956 px and Kōhei 174 → 1165 = 991 px, a ratio of 0.965 against 0.913. This is marginal. Kōhei leans forward and Natsuki stands upright, and the two sit at opposite edges of the panel, so readers can't compare them. Not counted.

**Problem:**
- **P9. p3-2: the background and light don't match p1-1.** The fighters have swapped sides, so the camera faces the same way as in p1-1, but:
  - there is no kamidana behind Kirishima, only windows and a plank wall, where p1-1 and p2-2 both put it behind him;
  - the sunlight comes from the right (shafts on the right half of the back wall, slanting down to the left), where p1-1, p1-3 and p2-1 light from the left.
  - Smallest fix: accept it as a [P] license. A strict fix would be an edit pass putting the kamidana wall behind Kirishima with the light from the left.

## 4. Animated catch (`v2/img/anim/cg_catch.mp4` and `.webm`): **FAIL (minor)**

**Passes:**
- Both files are 1920×1072, 24 fps, 3.04 s, and they match.
- **Hands, checked on 12 frames.** His right hand is behind her back throughout. His left hand closes on her forearm around frames 14–18. Her right hand rests on his chest. No arm crosses her chest, and there are no extra hands.
- **The tear** appears only in the last half second.
- **The ponytail swing** comes within about 10 px of the left edge in frames 34–37 but is never cut off. It was already accepted.
- **The last frame matches the CG.** The mean absolute difference is 5.2 levels and the 99th percentile 25. It is globally 3.4 levels darker (signed mean −3.2, −3.7, −3.4), which is not a visible pop.

**Problems:**
- **P11. (Shared with the CG.)** A floating droplet appears from frame about 55 onward. It is 58 px brighter than the wall background by frame 60, at about (874, 404) in video pixels. See section 5.
- **P14. Her gaze breaks mid-catch.** From frame about 19 to 36 (roughly 0.7 s) her head turns toward the camera and she looks down and away from him. Her face in those frames reads off-model: smaller, heavier-lidded eyes and a narrower face (compared on crops of frames 1, 24, 28 and 73). She is looking up at him in the start frame and the CG, so she glances away and back during the catch.
  - Smallest fix: accept it, or one Kling retake with "she keeps her face turned up toward his the whole time; no head turn toward the camera" (about $0.42 per take, per prompts.md).

## 5. CG `cg_catch.webp`: **FAIL (minor)**

**Passes:**
- **On model.**
  - Natsuki: face A (round green eyes, strong lash line, hatched blush). Her hair measures RGB 168/88/57 against #b55e36. Her irises sample warm jade (RGB 73/88/70 on the near eye) under the orange light. She has a ponytail with a plain dark tie, a side-swept fringe and the two face-framing locks. Her hakama is dark navy (42/47/64), matching the sprite's 48/50/68.
  - Kōhei: the round 1 haircut holds. It is short and slightly unruly, the fringe is above his brows, and his ear shows. His hair samples about 103/68/59 in warm light. His gi and hakama are navy, and the gi sleeves end at the forearm on both of them.
- **Scale.** On 2× grids, her measures against his: eye line to chin 164 vs 157 px (1.04), distance between irises 80 vs 77 px (1.05), ear length 85 vs 92 px (0.92). The target is 0.94–0.96. She overlaps the front of his hakama, so she is a little nearer the camera, which accounts for the face measures running about 5–10% high. Pass.
- **Text match, c2_0188–0196:**
  - one arm behind her back and the other hand around her forearm;
  - her weight is held;
  - sweat at her hairline (a drop under the fringe at about (878, 462)) and a strand down her cheek;
  - lips parted on the breath;
  - eyes wide and confused;
  - one tear from the corner of the eye down the cheek, matching the Oct 24 rewording;
  - his ears red, which sets up c2_0207;
  - long orange light through high windows, a shining wet floor, the bucket and the zōkin.
- **Light** comes from the upper left, as on `bg_dojo_evening`.
- **Content.** The framing is modest. There is no text, watermark or border.
- **The exported files** match the master: the master downscaled to 2400 against the game file differs by a mean of 1.75 levels, and the thumbnail by 3.4.

**Problems:**
- **P11. (Should fix, cheap.) A second "tear" floats in the air.** There is a white droplet with an outline, about 12×20 px, at (1092, 505) in the 2400-px CG. That is level with her far eye and about 120 px out from her face, on the side she is falling away from, so it reads as a tear flung from that eye. It contradicts "One tear" (c2_0194). It looks like a survivor of the Oct 24 clean-up of the drops "at her far eye".
  - Smallest fix: code. Inpaint it on the master and re-export the game file and thumbnail. Then paste the same patch through a small feathered mask into anim frames 55–73 and re-encode the mp4 and webm, so the clip and the hold still match.
- **P12. The room isn't the plate's room.**
  - `bg_dojo_evening`: side walls of tall vertical-slat lattice windows with transom panes, and armour stands and shinai racks along them.
  - CG: a solid vertical-plank wall, a band of clear sash windows at the top and low slatted vents at the floor.
  - prompts.md calls this "the dojo's side wall", but it doesn't match either side wall of the plate. The light, the time of day, the wet floor and the props all carry over, so the effect is mild.
  - Smallest fix: accept it and log it as [P]. No text change is needed, since "high windows" (c2_0184) matches the CG. Repainting the wall is possible but risks the figures.
- **P10. (Continuity across the insert and the CG) Natsuki's hakama changes shade.**
  - Insert: faded blue-grey, with median RGB 78/86/103 in p1-1, 72/78/97 in p1-3, 60/67/80 in p2-5, 66/71/87 in p3-2, and up to 90/99/110 and 111/114/122 in p2-1 and p3-1.
  - CG and the kendo sprites: dark navy (42/47/64 and 48/50/68).
  - The insert follows `bogu-natsuki` (63/77/97) and c2_0074 ("faded indigo keikogi and hakama"). The sprites and CG don't.
  - Within the insert, p3-1's hakama is nearly as light as her gi.
  - Smallest fix: one [P] decision in the log, saying which shade governs. Then either accept the difference, or apply a boxed lightness and hue pull (as `hue_shift.py` already does) to bring the insert's hakama toward the sprite's value, starting with p2-1 and p3-1.

**Note (not counted):** her gi in the CG samples at hue 250° against 228° on the sprite, so it reads a little lavender. Kōhei's navy shifts by the same amount in the CG (232° → 250°), so the evening light explains it. It isn't a palette error.

---

## Summary of failures (12)

| # | Image | Problem | How measured | Smallest fix | Priority |
|---|---|---|---|---|---|
| P5 | p2-1 | Kote lands on the tsuba and fist, not the wrist; her blade passes about 60 px above his wrist | blade line through 1:1 crop points | Edit pass: lower her blade onto his right glove cuff and recentre the spark | Should fix |
| P7 | p2-5 | Static kamae drawn as wide lunges (feet ≈ 2′11″–3′0″ apart) and the blades crossed at 0.86 of a blade length | grid points and feet-to-height ratios | Reroll p2-5: upright chudan, narrow stance, only the tips crossing | Should fix |
| P11 | CG and anim | A floating droplet at (1092, 505) reads as a second tear ("One tear") | 1:1 and 4× crops; the anim from frame about 55 | Inpaint on the master, re-export, patch anim frames 55–73 and re-encode | Should fix (cheap) |
| P1 | p1-1 | Shinai cross at mid-blade; tsuba 0.73 of a blade apart (about 2.6× too close for tips crossing) | 1:1 crop coordinates | Accept as [P], or reroll wider | Minor |
| P2 | p1-2 | Kamidana behind Kōhei: the dojo is rotated 90° against p1-1 and p2-2 | panel comparison | Accept, or edit the back wall to the side wall | Minor |
| P3 | p1-1, p1-2, p2-2, p3-1, p3-2 | Pseudo-kanji on the plaques and zekken, some Latin-like ("Hb") | 2× zoom | Code: soften the glyphs into marks, or accept (matches `bg_dojo`) | Minor |
| P4 | p1-3 → p2-1 | His fists go from above his head (p1-3) down to chin height (p2-1) in the next beat | y of the fists against y of the men top | Accept, or edit p1-3's arms down to forehead height | Minor |
| P6 | p2-1 | Kōhei's tare is maroon (69/37/46) where it is navy (38/38/55) elsewhere; a red/blue seam on the men rim; an orange speck | box medians and a 2× zoom | Code: boxed hue shift on the tare, touch up the rim and speck | Minor |
| P9 | p3-2 | No kamidana behind Kirishima and light from the right, where p1-1 has light from the left | panel comparison | Accept as [P] | Minor |
| P10 | insert and CG | Natsuki's hakama is faded in the insert (60–111 RGB) and dark navy in the CG and sprites (42–48) | box medians | Log a [P] choice; optionally pull the insert's hakama darker (p2-1, p3-1 first) | Minor |
| P12 | CG | The wall isn't `bg_dojo_evening`'s side wall (plank wall and sash windows instead of lattice) | side-by-side with the plate | Accept and log as [P] | Minor |
| P14 | anim | Her head turns toward the camera for about 0.7 s (frames 19–36) and her face goes off-model | frame crops at 1, 24, 28 and 73 | Accept, or one Kling retake (about $0.42) | Minor |

**Checked and passing:**
- On-model colours for all three characters against the swatches and the sprites.
- Scale, against the lineup target of 0.913: 0.904 in p2-5 and 0.965 in p3-2 (marginal, explained by posture); the CG head measures are in range.
- Men on in every match panel.
- Screen direction and Kirishima's arm direction in p2-2 and p3-2.
- p3-1's left foot forward.
- p2-4's face A.
- Kōhei's haircut in the CG.
- The tear's timing in the anim, and the anim's end frame against the hold.
- No baked-in frame lines (the raw p2-2 top row and p2-4's white side bars are cropped out by the compositor).
- Modest framing throughout.
