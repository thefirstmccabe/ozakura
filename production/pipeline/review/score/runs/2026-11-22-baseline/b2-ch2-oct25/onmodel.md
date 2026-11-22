# On-model image check (§9 step 4): Ch2, build b2-ch2-oct25

**Scope.** `production/pilot-v2/script/ch02.ozs` shows three pieces of art. Line 187 is the manga insert `ins_match` (3 pages, 10 panels, `v2/img/ins/ins_match/page1–3.webp` plus `ins_match.json`). Line 263 is the animated moment `@anim cg_catch` (`v2/img/anim/cg_catch.mp4` and `.webm`), which then holds the CG `v2/img/bg/cg_catch.webp`. The `@cg -` at line 273 only clears the CG. There are no other `@cg`, `@anim` or `@insert` lines.

**Method.** I compared each piece against style guide §1a–§2, the Ch2 entries in `art/prompts.md`, the sprites (`v2/img/ch/natsuki_kendo_*`, `kirishima_kendo_calm`), Kōhei's references (`refs/design-oct10/r3/kohei-short-A.png`, `r4/faces/02-neutral.png`, `refs/inventory/full-kohei.png`, `bogu-kohei.png`, the `kohei_kendo_*` face windows), and the plates `bg_dojo` and `bg_dojo_evening`. I took every measurement on gridded crops at full resolution (PIL/numpy). Colors are medians over boxes I checked by eye. Video frames came out of ffmpeg (73 frames at 24 fps in both files), and I tested camera lock with OpenCV phase correlation. No Ch2 layout sketch exists: `art/layout/` holds only `cg_collar_layout.jpg`, so the multi-character pieces were checked without one.

**Result: 6 problems, all minor (1 in the CG, 5 in the insert). The animation passes.**

---

## 1. `cg_catch` (CG held after the catch; c2_0188–c2_0196): FAIL, 1 minor problem

Surrounding text: the mop race in the evening light on a wet floor. Then "One arm behind her back, my other hand around her forearm", "the sweat at her hairline, a strand of hair stuck to her cheek, the moment she breathes in", and "One tear, sliding from the corner of her eye down her cheek. Her eyes are wide and confused." Her line about his ears follows after the CG.

| Check | Result | How checked |
|---|---|---|
| On model: Natsuki | Pass | Face A (round, large green eyes, strong lash line, hatched blush) matches `natsuki_kendo_tears` side by side. Hair is copper: CG #b65934 vs swatch #b55e36. She has the high ponytail and dark tie. |
| On model: Kōhei | Pass | Short dark-brown hair, ear and nape showing, fringe above the brows (the seed 493 fix holds). Warm brown eyes. Hair #45302d–#4c322e, L 0.22–0.24, vs swatch #3d3232 (L 0.22). Navy keikogi and hakama, L 0.15–0.20. |
| Swatch: her gi | Pass, see note | Her gi measures #736e85 (hue 253°) vs the sprite's #737c97 (225°), so it reads lavender-gray. The cause is the orange light: her hakama moves from sprite 232° to CG 244° under the same light, which predicts about 242° for the gi. The remaining 10° is noise. |
| Scale | Pass | Eye-line midpoint to chin: her 154 px, him 159 px, ratio 0.97. Target is about 0.95 for heads at 5′3″/5′9″. The poses make full height unmeasurable. |
| Matches the text | Pass except problem C1 | His right hand cups her back from behind and his left hand grips just above her wrist. Sweat bead at her hairline, a side lock along her far cheek, lips parted. One tear from the eye's corner down her cheek. Eyes wide, brows raised and drawn together. His ear is red. There is a bucket and a zōkin on a wet, shining floor, and the light is long and orange through high windows. |
| Location and light | Pass, see note | The sun comes from the upper left, as on `bg_dojo_evening` (shafts fall left to right). No mirroring. |
| Canon and content | Pass | Modest framing: her own arm covers her chest and his hands are on her back and wrist. No text, watermark or frame line. Hands: she has 5 digits; his gripping hand reads correctly; his back hand shows thumb plus 4 fingers. |
| Craft | Problem C1 | See below. |

**C1 (minor): a stray drop floats in mid-air beside her face.** It is a white teardrop shape about 10×24 px at (1090–1100, 498–522) on the 2400×1340 CG, or about (1250–1261, 571–599) on the 2752×1536 master. It sits between her far cheek and his chest. Next to "One tear" it reads as a second tear flicking off. The round-1 fix removed the drops on her cheek and at her far eye but missed this one. The clip carries it too: it fades in over frames 52–59 and holds to frame 73 (patch max luminance 149 → 247).
*Fix (edit pass, code):* paint it out of the CG master and the webp, using the same inpaint as the round-1 drops. Then patch the same spot in frames 52–73 of both encodes. The camera is locked (below), so one fixed background patch works. Without the video patch, the drop pops off at the handoff from clip to still.

Notes (not counted):
- His crown is cut by the top edge: hair tips touch y = 0 across x ≈ 1170–1260. It reads as a tight crop, not an error.
- The CG has a few more flyaway strands at her crown than her sprite (style guide: "never tousled"). After practice and a race this is mild.
- Her ponytail tie sits a little lower on the head than the sprite's crown ponytail: tie to ear is about 0.49 head-lengths in the CG vs about 0.6 on the sprite. The head is tilted back, so this is inconclusive.
- The back wall's clear four-pane windows over plain wainscot differ from the plate's tall slatted windows. `prompts.md` already logs it as "the dojo's side wall". At this crop nobody will place it.

---

## 2. `@anim cg_catch` (`anim/cg_catch.mp4` and `.webm`, 3.04 s): PASS

| Check | Result | How checked |
|---|---|---|
| Handoff to the CG | Pass | Frame 73 against the CG resized to 1920×1072: mean absolute difference 5.3/255, 99th percentile 25. The difference map shows only edges and encoding, and the tear and drops sit where the still has them. Frames 60–73 hold. |
| Camera lock | Pass | Phase correlation on three background patches, frame 1 vs frames 20, 36, 50 and 73: every shift is under 0.35 px. |
| Encodes | Pass | webm vs mp4 at frames 1, 36 and 73: mean difference 1.5–2.3/255, same content. |
| On model across the clip | Pass | Both faces, hair and outfits hold. Mid-clip (frames about 18–34) her brows draw together and her lids lower, but face A and the lash line stay. His eyes close for one frame around frame 22, a blink. |
| Anatomy and canon | Pass | Two arms each in every sampled frame. His right arm never crosses in front of her. No kiss framing. |
| Matches the text | Pass | Her "heel goes out" happens on the sprite before the clip. The clip shows him taking her weight and closing on her forearm. The tear forms late, as a small drop from about frame 30 and a full tear by frame 60. |

Notes: his grip smears for about 1 frame (frame 13). The ponytail whips out horizontally during frames 28–40, already accepted in `prompts.md`. At frame 1 his back hand already touches her, so the catch reads as him taking her weight more than closing a gap. Neither contradicts the text. C1's drop shows from frame 52 (see above).

---

## 3. `ins_match` page 1 (`page1.webp`, 3200×4544; panels from `ins_match.json`)

**p1-1** (wide, 2.33: crouched at the line, tips crossed, Kirishima behind as referee, club kneeling along the wall): pass on model, with problems I1 (scale, borderline here), I2 and I5 visible.
- Kōhei: navy, dark-red dō, red men rim. Natsuki: paler blue keikogi and hakama (hakama hue 220°), black dō, copper ponytail from the back of her men. Both wear men. Kirishima: crew cut, square jaw, white keikogi, navy hakama, hand raised. He matches `kirishima_kendo_calm` and `kirishima-masc-A`.
- Scale (kneeling): men top to the lowest foot contact is 880 px for Kōhei (308 → 1188) and 859 px for Natsuki (319 → 1178), ratio 0.976. Target is 0.913. He leans forward about 20° and she sits upright, so the true ratio is probably about 0.93–0.95. That is borderline here and goes in the same direction as I1. Men widths are 193 vs 186 px; front kote are about 85 px each.
- Location: kamidana centred on the back wall, name plaques, shinai rack at the left, windows on the side walls. This is `bg_dojo`, and the light comes from the left.
- Note: the shinai cross mid-blade in a wide X, each tip reaching the other fighter's hands, where the text says "tips crossed". Both fighters kneel on one knee instead of sonkyo (already logged as "full sonkyo still not drawn"). Kendo readers would notice. Most readers will read "crouched, swords crossed". The bystanders' zekken carry pseudo-letter scribbles, and their kote show bare fingertips, both tiny.

**p1-2** (16:9: Kōhei past Natsuki's shoulder, sword lifted; her tip on his throat): pass.
- Her shinai line, extended from the tsuba (880, 630) through the tip (728, 432) in view coords, reaches his centre line at y ≈ 285. His throat or men chin is at about 300–320, so the tip is on his throat at this scale. Her gi hue is 224°. Background is the kamidana wall, the rack, and the armor stands at the right, matching the plate.
- Part of I2: the left-wall alcove is empty, though p1-1 put two kneeling members on that side.

**p1-3** (wide: Kōhei's arms going up for men; her sword moving to his wrist): pass.
- His arms are overhead and her blade angles up toward his raised wrists. Scale is about 0.92 (men top to feet in view coords, both in wide stances), close to target. Gi hue 223°.
- Note: his shinai blade leaves the top edge, so only the tsuka shows, and both stances are wider than real kendo footwork. Neither contradicts the text.

## 4. `ins_match` page 2

**p2-1** (large: her strike lands on his right wrist as his arms come up): pass on the beat, with problems I4 and I5.
- His front (right) hand is at chin height on the rising shinai. Her blade crosses at his front kote, and the impact star centres on his right wrist. There is a fumikomi flash at her front foot. Scale: 740 vs 675 px (men top to feet, view), ratio 0.912. Screen direction holds (Kōhei left, Natsuki right).
- **I4 (minor): Kōhei's men rim is two colors.** The box recolor that turned the maroon men navy (hue → 232°) turned most of the leather face-ring blue-violet. The far edge outside the box stayed red, so the rim shows a hard blue/red split at about page (1016–1089, 432–578). In every other panel his rim is red or maroon (p1-1, p1-3, p2-3, p2-5, p3-1).
*Fix (edit pass, code):* restore the red on the rim inside the recolor box: mask the ring and re-apply the original hue.

**p2-2** (4:3: Kirishima's arm raised toward Natsuki's side): pass on model, with problems I2 and I3.
- He points with his left arm toward viewer-right. In p1-1, p2-1 and p2-5 Natsuki is on viewer-right, so the direction is right. Background is the kamidana wall, consistent with the plate. All eight background faces differ (no clones).
- **I3 (minor): a Natsuki look-alike kneels among the bystanders.** Second from the left (about page 1599, 2512) is a girl with copper hair in a bun, #bb714e, hue 19°. Natsuki's swatch is #b55e36, hue 19°. Her gi is pale: L 0.44, against L 0.27 for her neighbour and 0.35–0.49 for Natsuki's insert gi. On the "Kote ari!" panel, readers may take her for Natsuki. A second copper-haired bystander appears in p3-2 (see page 3). The style guide keeps Natsuki's hair distinctive; the opponent and thug hair rule exists for the same reason.
*Fix (edit pass, code):* boxed recolor. Make both bystanders' hair dark brown or black, and make the p2-2 girl's gi the club navy (the same `hue_shift.py` approach).

**p2-3** (4:5: Kōhei's eyes behind his grille, bead of sweat): pass.
- Dark-brown fringe, warm brown eyes, sweat on brow and cheek, white tenugui, red rim. Note: a full fringe shows below the tenugui, which c2_0292 says is "tied tight over my hair". It is a readability liberty also used on Natsuki, so not counted.

**p2-4** (1:1: Natsuki laughing behind her grille, out of breath): pass.
- Face A: large round green eyes, strong lash line, hatched blush. Open laugh, sweat drop, no tears (the seed 525 fix holds). Red rim, matching her other panels.

**p2-5** (3:2, built at 1.42: back at the line, tips crossed): pass, with I5 visible.
- Scale: Kōhei 852 px (men top 230 → front sole 1082), Natsuki 762–776 px (306 → 1068 and 1082), ratio 0.89–0.91, on target. Gi hue 231°. Shiai line on the floor. Same X-crossing note as p1-1.

## 5. `ins_match` page 3

**p3-1** (large: she comes in for men; he drops under, low, **left foot forward**, cutting across her body): pass.
- Foot check: his back foot points toward the camera with the big toe on the image-right side of the foot, which makes it his right foot. His front foot shows its arch side and big toe, consistent with a left foot pointing right. So the left foot is forward, as c2_0170 later needs.
- Her shinai is raised for men. His cut lands on her black dō as they pass. Both wear men. Her gi hue is 213°. The kamidana wall matches the plate.

**p3-2** (wide: past each other; Kirishima's arm toward Kōhei's side): beat passes; problems I1, I2, I3 and I5.
- They have swapped sides (Natsuki left, Kōhei right) and turned to face each other in zanshin. Kirishima's arm points toward Kōhei. Kirishima is on model.
- **I1 (minor): Natsuki is drawn too tall.** Measured in panel px on the 2920-wide crop:

  | | Men top (y) | Front sole (y) | Back sole (y) |
  |---|---|---|---|
  | Kōhei | 173 | 1156 | 1178 |
  | Natsuki | 204 | 1166 | 1150 |

  Front to front: Natsuki 962 vs Kōhei 983 px, ratio 0.979. Back to back: 946 vs 1005 px, ratio 0.941. The mean is about 0.96, against a target of 0.913 (5′3″/5′9″). Their feet are within 9 px in depth, so perspective doesn't explain it. She reads about 5′6″, against 0.89–0.91 in p2-5 and 0.91 in p2-1. p1-1 leans the same way (0.976 kneeling, posture-confounded).
*Fix (edit pass, code):* scale her figure in p3-2 to about 0.95 about her front foot. She stands clear of the other figures against the back wall, so fill the gap from the surrounding wall and floor. Optionally check p1-1 the same way after a posture-matched measurement. Reroll only if the edit shows.
- **I2 (minor): the bystanders change between panels.** In p1-1 four members kneel along the side walls, all in full bogu with men on. In p1-2 the left side is empty. In p2-2 eight members kneel along the back (kamidana) wall, none wearing men. In p3-2 eight kneel along the back wall, five with men on and three without (one of them the copper bob, I3). All of this happens within one short match.
*Fix:* one edit on p2-2 putting men on the seated members brings p2-2 in line with p1-1 and most of p3-2. The wall positions can stay (p2-2 and p3-2 agree with each other). Or accept and log it.
- I3's second look-alike: far right, about page (2750, 3791), hair #b6734f, hue 21°.

**I5 (minor, pages 1–3): Natsuki's hakama doesn't match her sprites and CG.** In the insert her hakama is the same pale faded blue as her gi: L 0.30–0.39, hue 215–222° (p1-1, p2-1, p3-1, p3-2). Her nine kendo sprites have a dark-navy hakama (#323548, L 0.24), and so does the catch CG (#21202e). She appears in the two-tone sprite just before the insert (c2_lesson) and after it (c2_debrief), so the outfit changes and changes back. The text ("a faded indigo keikogi and hakama", c2_0074) supports either. The insert brief asked for a pale hakama and the sprite brief asked for dark navy. Style guide §2 specifies only the keikogi.
*Fix:* the author or Production picks one and logs it [P]. The cheaper direction is a boxed darkening of her hakama in the insert panels (L ×0.7 toward the sprite's #323548), since 10 images (nine kendo sprites and the catch CG) already use the dark hakama. Her insert gi colors are fine: hue 199–231°, no violet, so the round-1 hue fix holds.

---

## Summary of failures

| # | Image | Problem | Check | Severity | Smallest fix |
|---|---|---|---|---|---|
| C1 | `cg_catch` (+ clip frames 52–73) | Stray mid-air drop beside her face reads as a second tear ("One tear") | Matches text / craft | Minor | Code paint-out on the CG master and webp, plus a fixed patch in frames 52–73 of the mp4 and webm |
| I1 | `ins_match` p3-2 (p1-1 borderline) | Natsuki at about 0.96 of Kōhei's height (target 0.913), reads about 5′6″ | Scale | Minor | Code rescale of her figure to about 0.95 about her front foot, then inpaint |
| I2 | `ins_match` p1-1, p1-2, p2-2, p3-2 | Bystanders jump between side and back walls and between men on, off and mixed | Continuity | Minor | One NB Pro edit on p2-2 (men on), or accept and log |
| I3 | `ins_match` p2-2, p3-2 | Two copper-haired bystanders (one in a pale gi) read as Natsuki | On model / craft | Minor | Code recolor: hair dark, the p2-2 girl's gi navy |
| I4 | `ins_match` p2-1 | Kōhei's men rim split blue/red at the recolor-box edge; red in every other panel | Continuity / craft | Minor | Code: restore the red rim inside the recolor box |
| I5 | `ins_match` (all panels with her hakama) vs sprites and CG | Natsuki's hakama pale in the insert, dark navy in the sprites and CG | Swatch / continuity | Minor | Pick one and log [P]; cheapest is to darken the insert hakama in code |

Logged but not counted: shinai crossing mid-blade and the one-knee kneel at the line (p1-1, p2-5), his crown touching the CG's top edge, mild flyaways at her crown in the CG, the CG's window style, the fringe showing under the tenugui (p2-3, p2-4), and the zekken scribbles and bare-fingertip kote on the p1-1 bystanders.
