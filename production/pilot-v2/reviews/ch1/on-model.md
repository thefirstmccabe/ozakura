# Ch1 on-model image checks (§9 step 4), Oct 18

Fresh agent; prompt `production/pipeline/review/on-model-image.md`. Each image was checked separately on 2400×1340 frames; the loops on 1920×1072. Measurements used pixel grids, Lab color, frame diffs and optical flow. The intro CG and its falter were checked before the cold-read round 2 fixes (classmate and a stronger falter; see `art/prompts.md`).

| Image | Verdict | Findings | Done |
|---|---|---|---|
| cg_cold_mirror | PASS | Every hard rule met; nobody in frame; the plate on the pole is blank. Distinct treatment: saturation 20, against 39 for the river and 36 for the dream. Nits: a notch on the mirror rim; a junction more than a bend | — |
| cg_cold_hand | PASS | One male hand in a modern zip-jacket sleeve on a wrapped grip; five digits; no blade or face. Which hand is ambiguous; no rule needs either. Mist matches the mirror image (ΔE 2.8) | — |
| cg_cold_mist + loop | PASS | Nothing in the mist; the camera is locked (phase correlation 0,0); the loop is seamless (the last frame is 1.2/255 off the first). **Optional:** the mist was ΔE 13 darker and greener than the mirror image | Graded to match (see `art/prompts.md`) |
| cg_dream + loop | PASS | Inside-wrist cut, on his left hand, matching the callus line; strip of cloth; five digits on each hand; her face and hair out of frame. In the loop, his hand moves at most 0.1 px median and the stain stays put | — |
| cg_natsuki_intro | PASS | Hair ends at the shoulders and is tucked behind her left ear; four distinct classmates. Height fits 5′3″ against the lectern and chalk tray. Head-to-waist 2.43 heads (sprite 2.44). Skirt about 8% shorter than the sprite, within the design | Later edit: the boy in profile is replaced (two cold readers took him for Kōhei) |
| cg_natsuki_intro_falter | PASS | Outside the face, nothing differs beyond compression noise | Later redone stronger (the cold readers didn't see the falter) |
| cg_collar | FAIL (minor) | The petal c1_0071 puts on her braid wasn't drawn. Optional: "Nanoha walks on the river side," but in the CG Kōhei is on the river side ("she's stopped in front of me" covers it). Head ratio 0.79 crown to chin, 0.96 eye to chin; her crown 6–8 inches below his, right for 4′11″ on her toes against 5′9″ | Petal added by a local edit. River side left. **The hair clip** (§2 has none; the sprites and this CG draw one) is a question for the author |
