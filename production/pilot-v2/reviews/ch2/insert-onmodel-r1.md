# Ch2 manga insert (`ins_match`): on-model check, round 1 (Oct 24)

Fresh agent, no prior context; checked the three 2× pages against the spec boxes, the 2K source panels, the style guide and the Ch2 script. Hue measurements over masked regions, with Kōhei's hakama in the same panel as the lighting control.

## Fails
1. **p2-1 (the kote): reroll.** Kōhei has one hand on a shinai pointing backward over his shoulder and the other arm raised as an empty fist: impossible in kendo, and the hit doesn't read as the right wrist (the chapter has just taught "Kote. The wrist. Usually the right one."). Reroll with both his hands on his shinai, raised as in p1-3, right hand forward; her tip lands on top of his right forearm just behind the glove cuff. Lettering: move the "Kote-e-e!" tail from [0.74, 0.20] to about [0.58, 0.24].
2. **p1-1 (opening): reroll.** Dō colors swapped (his black, hers red-brown; p1-2 has them right). Not in sonkyo (the script says "We crouch at the line"; the art shows deep lunges). Natsuki's uniform is violet (hakama hue 261° vs 214° on her reference). A black frame line is baked in (double border).
3. **p2-3 (Kōhei's eyes): crop.** White band in source columns 0–114 of 1696 shows as a 31 px bar. Crop to x 115–1696. Minor: move the caption from [0.5, 0.89] to about [0.5, 0.08].
4. **p2-4 (Natsuki laughing): face-A edit pass (judgment call).** The Oct 12 face with only the eyes recolored; next to the face-A windows the eyes are almond-shaped with a heavy lower lash line and the face reads older. It's her only face shot in the insert. Drops on both lower lids can read as tears and blunt the single tear in the catch. Fix: one edit with `production/design/natsuki-oct24/refs/faceA-head-crop.png` as image 2, plus "no tears, no drops on the eyelids."
5. **p2-5: lettering only.** "(Second point!)" covers the top of her men. Move the shout to about [0.63, 0.10] and the gloss to [0.60, 0.245].

## Minor
- p3-2 lettering: "Yame! …That's time." covers ~12 px of her men (y 0.12 → 0.10); "Dō ari!" and "(Point: body!)" touch Kōhei's grille (x 0.66 → 0.63).
- Natsuki's uniform drifts violet (259–270°) in p1-1, p2-1, p2-5, p3-1 (reference 214°; other panels 227–237°). Likely cause: every new panel was anchored on Oct 12 p1-1, which carries the violet and the lunges. Don't anchor rerolls on p1-1; a masked hue shift is enough for p3-1 and p2-5.
- Wide lunge stances in p2-5 (and p1-1, p2-1) are wrong for kamae ("left heel just off the floor"); acceptable for p2-5's reset beat.
- Gloss text 24 px is below the §5 minimum of 27 for small text (~14 px on a phone). Consider 27.
- Kendo nits: p1-2 he raises the sword upright with feet together, her tip at his chest not throat; p1-3 his top fist touches the border; p2-2 Kirishima points a finger rather than an open hand; p3-1 the dō lands near the guard and she's fully airborne.
- Dojo geography (shrine shelf side, Kirishima's backdrop, masked/unmasked club) shifts between panels; readers unlikely to notice.

## Passes
Men on in every kendo panel; sides consistent (Kōhei left, Natsuki right, swapped after the pass in p3-2); Kirishima's arm points at the scorer both times; right hand forward wherever readable (except p2-1); the debrief lines are supported (Kōhei's left foot forward in p3-1, on a close look); scale Natsuki ÷ Kōhei 0.89 / 0.89 / 0.94 (target 0.913); right-to-left order unambiguous; every panel stands alone; SFX inside panels; both reveals open a new page.

## Production response
See `insert-onmodel-r2.md` (fixes applied and re-check).
