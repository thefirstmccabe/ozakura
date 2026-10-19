# Ch1 revision: independent build review (§9 step 7), Oct 18

Fresh agent; prompt `production/pipeline/review/build-review.md`. The whole chapter was replayed in Chromium at 1180×820 and 820×1180, with timed frame captures of the cold open, tap-speed tests and a line-by-line staging check against `script.json`. The reviewer edited nothing.

| # | Finding | Done (commit d4b395f) |
|---|---|---|
| 1 | **Portrait:** the blurred bands above and below a CG switched instantly at the start of every CG-to-CG crossfade (one shared fill layer). Missed by QA, which only captures at lines | Each CG image has its own blurred fill that fades with it |
| 2 | **Old saves resume in the wrong place.** They store a command index, and the shipped pilot and v2 shared the same storage keys | v2 saves use their own keys and carry the build fingerprint and the line ID. A save from another build resumes at its line, else its scene, else from the top |
| 3 | **A tap skipped the cold open's holds**, and fast taps snapped its crossfades | `@hold on` / `@hold off` around the cold open: taps are ignored there (skip mode still fast-forwards) |
| 4 | **The dream's white flash never fired**, because solid backgrounds returned before the flash. "Slow" had no effect on solid colors, and the last line stayed in the box through the fade to black | The flash fires. Solid-color changes honor cut and slow. The text box hides on a change to a solid screen |
| 5 | c1_0260 "a pink cloud caught on the hillside" from the river path, but the river background has green hills | "…so big that from the bridge it looks like a pink cloud…" [P] |
| 6 | c1_0071 "stays there": the petal is in the collar CG but not on her sprite before or after | "One lands on her braid." |
| 7 | Small issues: the title subtitle still said "Prologue"; the P.0 scene detail said "Prologue"; the dev strip read "P.0 · 1/0"; c1_0249 showed Nanoha's tease sprite for "drops her chin and narrows her eyes"; the portrait text box grows to 6 lines on c1_0038 and c1_0204 (predates this round) | Labels fixed; deadpan sprite before c1_0249. The 6-line box is left as is |

**Checked and fine:**
- The cold open's order, timing, silence and hidden text box; it plays first from Begin and from the chapter menu.
- The dream's "???" with no face window.
- The scene chart (COLD OPEN P.0, then 1.1–1.8, all thumbnails).
- Fresh saves.
- The interlude's face windows.
- All 259 lines' staging at both sizes against the script (face-window rules, sprite expressions, CGs, tints).
- The five late text fixes and their new audio.
- Voice levels (only the two known dream lines flagged).
- Every changed frame in the visual diff explained.
- Living-still alignment and loop seams (tested with a WebM copy).

**Not checkable here:** Safari on the iPad, H.264 playback on the device, listening by ear.
