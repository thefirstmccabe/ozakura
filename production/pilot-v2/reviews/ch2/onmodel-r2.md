# Ch2 on-model check, round 2 (Oct 25): the round-1 fixes

Fresh agent; verified every round-1 fail on the current files against the references, measured, and compared with the round-1 versions (commit 93ee18c). Production's response follows each area.

## Sprites and face windows: PASS
- Natsuki kendo (9): row 0 now has 0 opaque px (was 110); the tied tuft is drawn above the tie. Jaw ghost gone (semi-transparent px in the jaw box 3600 → 1427, normal anti-aliasing). HEADROOM .035: figure scale 0.9991–1.0020 of before at 1024×768, 1366×1024, 844×390 and 1920×1080; eye line moves ≤0.7 px.
- Teach: ponytail top now at y 242 (was a 121 px straight edge at y 290–292); jaw haze gone.
- Kōhei kendo windows: gi #2e3144 (233°) in all 10 (was #5a5c77); CG navy #2b2939. Grin mouths restored (diff to the school grin 1.0/255 and 0.85/255, were ~16).
- Takatsuki calm: wedge matches the frown sprite; brow untouched.
- §2 work outfit updated [P].
- Not addressed (minors): blush forehead drop, the tear during the wipe; Takatsuki calm irises and smirk (unused in Ch2).
- New, zoom-only: the kendo ponytail strands end in soft unlined blurs at the old cut line; the teach sprites have a faint 2-row alpha dip across the ponytail at y 291–292.

## Backgrounds, CG and animation: FAIL until one fix (then PASS)
- Animation: his right arm stays behind her back n0–n72; nothing crosses her chest; her right hand stays on his chest; tear forms at n29 and holds into the CG (no flicker); end frames static, mean diff 4.4/255 to the CG. PARTIAL: Natsuki's head swings toward the camera n18–n33 and her face drifts for about 0.6 s. A small flying droplet in the CG is missing from the video and pops in at the cut.
- `cg_catch`: hair reads as `kohei-short-A` (crown still runs off the top edge, partly from his head tilt); cheek drops gone, one tear kept; a ~10 px smudge at her far-eye corner reads as hair.
- **New:** faint ghost wisps of the old fringe and a dark smear at the outer corner of Kōhei's near eye (x ≈1030–1110, y ≈290–340 at 2400 px), from the feathered paste; also in the video's end frames.
- `bg_bridge_dusk`: tree ~82 px wide (nearer cherry ~125 px), soft, wires straight in front, no ghost of the old tree; changes confined to x 1518–1681, y 340–439.
- c2_0289 matches the balcony view and is compiled.

## Insert: not yet a pass (7 of 9)
- p2-1: both his hands on his own shinai; her shinai meets his right fist with the burst there; his men navy (234°); her uniform 207–211°. Caveat: contact is on his fist and guard rather than behind the cuff; the call carries it. **New:** a green rim on the cream inner edge of his men and a green "T" on the window frame behind him (recolour leftovers).
- p1-1: dō colours right, crouched at the line (one knee; not true sonkyo), her gi 221°/hakama 224°, no baked frame line.
- p2-3: white band gone. **New (minor):** left border about 19 px at 2× (10 elsewhere) from a dark line in source columns 1–7.
- p2-4: reads close to face A, eyelid drops gone.
- p2-5 lettering clear; glosses render at 54 px (2×).
- PARTIAL: p3-2 "Yame! …That's time." still overlaps the top of her men by 2–24 px (2×).
- PARTIAL: p2-5 hakama fixed (219–224°) but her keikogi still 247–258°.
- p3-1: gi 221°, hakama 228°.
- Observation: Kōhei's navy gi is close to the face window's own background, so his shoulders blend (outlines carry the shape).

## Production response (Oct 25)
- `cg_catch` ghost: the hair edit re-pasted with the exclusion box tightened to Natsuki's hair (x <262, y >415 in the head crop) and a smaller feather, so the old fringe no longer blends in beside his eye. The video's frames from n50 take the new CG in the changed area (and the flying droplet) over 8 frames, then the encode was redone.
- p2-1: recoloured in RGB instead of interpolating hue (the green came from blending 10° → 232° through green), red-only mask (saturation > 0.28).
- p2-5: her uniform hue set toward 218° (keeping a quarter of the shading variation) in a feathered box over her figure, from the original panel: top 219°, hakama 216°; Kōhei untouched (230°).
- p2-3: re-cropped at x 123.
- p3-2: "Yame!" balloon raised to y 0.075 and its gloss to 0.245; clear of her men.
- Backlog (zoom-only): the ponytail seam blurs and the teach alpha dip; Natsuki's face drift n18–n33 (noted in the handover); Kōhei's navy against the window background.
