# Ch2 sprites and face windows: on-model check, round 1 (Oct 24)

Fresh agent, no prior context; measured the installed files in `v2/img/ch/` and `v2/img/face/` against the references, the style guide and the Ch2 script; composited on `bg_dojo` at iPad retina size.

| Asset | Verdict |
|---|---|
| `natsuki_kendo_*` (9) | **FAIL**: ponytail cut flat at the top of the frame; a ghost of the school hair beside her jaw |
| `natsuki_teach_smile`, `teach_point` | **FAIL**: the same flat ponytail cut, visible in the empty headroom (head size passes) |
| `face_kohei_kendo_*` (10) | **FAIL**: his gi is Natsuki's faded indigo, not navy; `kendo_grin` lost the lower half of its mouth |
| `face_kohei_work_grin` | **FAIL**: lower half of the mouth missing (the other 9 work windows pass) |
| `face_natsuki_kendo_*` (9) | Framing passes; inherit the jaw ghost, rebuild after the sprite fix |
| `face_natsuki_teach_*` | PASS |
| Kirishima calm and stern, plus windows | PASS |
| Takatsuki (4), plus windows | PASS, small issues |

## Fails
1. **Natsuki kendo set.**
   - Flat-cut ponytail: row 0 of every sprite has 108 opaque px (x 542–649); the school sprites touch the edge with 17 px. The engine puts her top at 83% of stage height, so it shows. Cause: the seed 301 base ran the ponytail off the master's top edge and `outfit_sprite.py` crops from there. Fix: outpaint the ponytail top on `natsuki-kendo-301-cut`, keep only the new margin, rebuild with `--headroom ≈0.04`, add the nine to `HEADROOM`, move the window crop down by the same amount.
   - Ghost of the school hair beside her left jaw (x ~400–480, y ~340–430): semi-transparent, near-black in eight expressions, whitish haze in `tears`. Comes from `outfit_sprite.py` step 3, `o[...,3] = oa*(1-m) + la*m`, which copies the school sprite's opaque hair through the feathered oval. Fix: keep the outfit's alpha and multiply the mask by `oa/255`.
   - Passes: faces are pixel copies of the approved school set (mean diff 1.8–2.2/255 inside the oval), same scale (eye spacing 123.8 vs 123.4); faded indigo gi lapped left over right, navy hakama, long high ponytail; c2_0074 and c2_0159 match; `tears` fits c2_0194–0198 (tear from her left eye, as in `cg_catch`).
   - Minor: `surprised` bangs redder inside the oval; `blush` loses the school version's forehead sweat drop; the tear is still on her cheek when c2_0197 says she wipes her face (reads as mid-wipe).
2. **Natsuki teach.** Rows 0–291 empty, then a 121 px straight edge at y 292: the most visible problem in the set. Fix: outpaint the ponytail top into the headroom, paste the same pixels into `point`. A fainter jaw haze too. Head size passes (template scale 0.9975–1.0025; eye spacing 122.0–123.2; head/sprite 0.2317 = the kendo set). One shinai, two arms, the same hand; shinai inside the frame; glasses match c2_0090.
3. **Kōhei kendo windows: gi colour.** Collar #575a77, Natsuki's faded indigo. §2 says navy; `cg_catch` draws him navy (#2c2c3b); the seed 361 prompt asked for "faded indigo", which is where it drifted. Fix: recolour the outfit area in code toward the CG navy, keep the line art, rebuild the windows.
4. **Kōhei `kendo_grin` and `work_grin`.** The head ellipse (centre 185,150, radii 120×128) ends ~y 274 and cuts the open grin; the outfit edit's closed chin replaces the lower lip. Not on screen in Ch2. Fix: rebuild with vertical radius ~150.

## Passes
- **Kirishima:** on model with `kirishima-masc-A` (crew cut, deadpan, folded arms; younger jaw suits 17). 5.7 heads tall, matching Takatsuki (5.7) and Ryōsuke (5.8). `stern` changes only face pixels. Windows centred.
- **Takatsuki:** slate-blue hair (#1b2a3b), navy gi; `calm` paste kept the frown sprite's alpha. Small: a pale gray-blue wedge at his right temple on `calm` (x ~494–579, y ~172–259; clone the frown's pixels); `calm` irises slightly cooler; pilot `smirk` reads close to a sneer (unused in Ch2).
- **Natsuki windows:** 450 px crops from the sprite top at the school windows' face position; the teach windows start below the cut.
- **Kōhei work windows (other 9):** same crop as the school windows, no seam. Doc mismatch: §2 says "white shirt, dark waist apron"; these show a T-shirt and a bib apron (marked [P] in `prompts.md`). Update §2 or log it.

## Production response
See `sprites-onmodel-r2.md`.
