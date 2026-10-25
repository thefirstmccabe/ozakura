# Ch2 build review (Oct 25)

## Round 1: whole chapter before handover (v2-ch2 @ b0c3ff2)
Fresh agent (`production/pipeline/review/build-review.md`), iPad 1180×820 at normal and fast tap speeds, phone 844×390, desktop 1440×900, network throttling for load timing.

### Must-fix
1. **The catch: the empty dojo flashes between the video and the CG** (c2_mop, after c2_0186): about 0.35 s on localhost, 0.13–0.6 s at 40–8 Mbps. `cg_catch.webp` was never preloaded (the look-ahead only handled `bg`/`cg`), and `animDone` cut to the CG and faded the video before the image had loaded.
2. **The insert opens on a blank dark screen** (c2_match, tap on c2_0138): page 1 appeared 1.7 s / 3.0 s / 7.1 s after the tap at 40 / 20 / 8 Mbps; the pages only started loading when the insert began.
3. **Sprites re-entering at a new position slide across the stage while fading in** (Natsuki c2_0071, c2_0091, c2_0154, c2_0176; Takatsuki c2_0078, c2_0115, c2_0164 — he glides through Natsuki; Rika c2_0084). `showSpr` set `left` on a hidden element that still had the `left .45s` transition. Also in Ch1 (c1_0054, c1_0102, c1_0186, c1_0206, c1_0237).
4. **A fast second tap skips the animated moment** (tap c2_0186, then again within 0.1–0.3 s).
5. **p3-2 "Yame! …That's time."** clear of her men now, but its top spikes were cut flat against the panel border.

### Backlog
- No controls during the insert or the text messages (Log, Save, Menu, Auto live in the hidden text box); a save made mid-insert reloads at page 1 and its slot label is blank.
- Animation encode 1920×1068 vs the CG's aspect (≤2 CSS px at the edges in the cross-fade); webm had become 4:4:4 at 3.4 MB.
- Phone 844×390: the text-message panel covers the "— Interlude: Natsuki —" label from c2_0262.
- Chapters menu: Chapter 2's thumbnail was the catch CG (gives away the peak).
- Staging taste calls: the restaurant background stays up for the walk home and his kitchen (c2_0056, c2_0057, c2_0299); the bridge stays up for "the light's on in Nanoha's window" (c2_0301; `bg_houses_night_lit` exists); long expression holds (Natsuki's laugh c2_0042→0049 incl. the reflective c2_0046; Rika surprised c2_0113→0121; Natsuki surprised c2_0154→0158); c2_0118 says Takatsuki "settles into kamae" while his sprite rests the shinai on his shoulder.
- Handover note listed "my bow is excellent", which isn't in the script.
- Not testable here: H.264 (this Chromium plays the webm) and Ch1's living stills.
- Snapshot diff: the 10 changed Ch1 frames (c1_0186–0195) are Nanoha ≈0.25–0.45 CSS px left after her c→l re-entry slide; harmless, and fix 3 should remove it.

### Checked and fine
Insert (13 steps, right-to-left, framing at all sizes, 7 voiced lines start 380–420 ms after their panel, backlog once each in order, fast taps never stick, Skip/Auto, resize re-fits); animated catch plays once and holds, Skip cuts to the CG, save/load at c2_0188 restores the CG without replay; HEADROOM sprites at scale 1.000 on the same floor, expression swaps change no geometry, heights survive resize; face windows on every Ch2 line (outfits switch at c2_0006 work, c2_0063 kendo, c2_0215 school; Kirishima's off-stage lines; none for on-stage speakers, Natsuki inside the CG, narration or texts; interlude POV window at c2_0259); text messages at all sizes; dojo-evening and bridge-dusk tints; chapter, date and end cards ("END OF CHAPTER 2", "Chapter 3, 'Windows,' comes next."); Chapters menu entry; all 145 + 7 voiced Ch2 lines start their clip, levels −20 ± 0.4 dB, no clipping; no errors at any size (Google Fonts blocked by the sandbox only). The five pre-review fixes (catch ghost, p2-1 green, p2-5 hue, p2-3 border, p3-2 overlap) confirmed.

### Production response (Oct 25)
1–2. Look-ahead preloads `@anim` (the CG and the video) and insert pages; `animDone` holds the video's last frame until the CG has decoded; inserts fade in only after page 1 decodes (taps meanwhile are ignored).
3. `showSpr`: a sprite entering (not on stage) gets its new `left` with the transition off and a reflow, so it appears in place; on-stage moves still slide.
4. Taps are ignored until the video has been visible 0.6 s.
5. Balloon 40 → 36 px at y 0.09: clear of the border and of her men.
Backlog done: the animation re-encoded at 1920×1072, both files 4:2:0 (mp4 1.8 MB, webm 1.1 MB); Chapter 2's thumbnail is now `bg_dojo`; the stale [P] item removed. The rest stays on the backlog (status board carry list).

Verified with a scripted run at iPad size under 8 Mbps throttling (`scratchpad/ch2/verify_fix.py`): the catch shows video then CG with no frame of the bare room in between; a tap 150 ms after the catch starts doesn't skip it; the insert never shows before page 1 has loaded; Takatsuki's re-entry at c2_0164 holds one x position (590 px) while fading in. Then the full regression run against the approved Ch1 (round 2 below).

## Round 2: the fix round (e713f9a)
- **Regression run** against the approved Ch1 (`qa_play.py --every` both builds, `snapshot_diff.py`): all 262 Ch1 frames compared; 13 differ, all by sub-pixel sprite position after a re-entry (c1_0054–0056 and c1_0186–0195: 0.35–0.45 CSS px, from setting `left` without the transition); nothing else changed. The new run's screenshot capture failed once at c2_0232 (a Chromium capture error after ~470 shots); the tail from c2_0229 to the end card was re-run separately: 65 lines, no errors, no failed requests.
- **Scoped independent check:** see below.
- **Scoped independent check (fresh agent) of e713f9a:** fixes 1–4 PASS. The catch: no bare-room frame in any run (localhost; cold cache at 4/8/20 Mbps; normal reading at 8 Mbps), the preload serves the video from cache (shows 0.27 s after the tap at 8 Mbps), Skip and save/load fine; double taps at +100–700 ms ignored, a tap at +1.0 s finishes it; never stuck when the video is blocked, never answers, is truncated or the network drops. Inserts: never shown before page 1, 46 taps during a 12.5 s load ignored safely, Skip logs all 12 lines. Sprites: all 13 re-entries hold one x (the pre-fix build slid in 7 of 13 when played through, which production's own check missed by starting at the line before); on-stage moves still slide; expression swaps unchanged. **Fix 5 FAIL:** the balloon cleared the border but its lower notch rested on her men. Backlog: no timeout on the insert's page-1 wait (stuck forever if the request never answers); taps ignored before a cold-cache catch video appears (1.3–4.5 s); a blink on a fast same-spot re-show (c2_0020 → c2_0022 → c2_0023). Test-environment note: the sandbox disk was full, and Playwright's `--disable-dev-shm-usage` put Chromium's shared memory there (the likely cause of the capture failure at c2_0232).
- **Production response:** the "Yame!" balloon moved right (x 0.38, 34 px, y 0.10): about 20 px (2×) below the border and 55 px above her men, right of her helmet. The insert's page-1 wait now opens anyway after 5 s (checked: a page-1 request that never answers opens at 5.3 s and taps through to the next scene). A same-spot re-show keeps the transition, so the fade reverses instead of blinking. `qa_play.py` launches Chromium with shared memory in /dev/shm, and the scratch disk was cleared. The cold-cache tap delay before the catch video stays on the backlog (normal play preloads it).
