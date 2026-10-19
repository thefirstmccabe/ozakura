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

## Fix-round check (fresh agent, on d4b395f)
All seven fixes pass:
- **Portrait fills:** frame-by-frame, each fill tracks its own image.
- **Cold open holds:** the hold ends at 16.1 s whether untouched or tapped; no snapped fades; skip mode works.
- **Solid screens:** behave as intended.
- **Saves:** same-build saves are unchanged; old-build saves resume by line, then scene, then from the top.
- **Labels and script:** only the expected five command changes; `qa_play` is clean.

New findings and what was done:
| # | Finding | Done |
|---|---|---|
| 1 | The flash let the dream CG show back through for about 0.3 s: three fades at different speeds | The CG and the background cut to white under the flash |
| 2 | The Load panel's preview for a save from another build came from the saved index | The preview comes from the line ID, else the scene title, else "Older version: starts over" |
| 3 | The dev strip went stale after Begin from the title | `devUpdate()` at the end of every jump |
| 4 | v2 shared the pilot's `ozk.dev` flag (and the prefs) | The dev flag is v2's own. Volume and text-speed prefs stay shared on purpose |
| 5 | A jump out of the dream's white screen left white under later backgrounds | Every jump resets the solid layer to black |
| 6 | The flash fired in skip mode | Guarded |
| 7 | The cold open couldn't be skipped at all (16 s on every Begin) | It plays through the first time. After that, a tap cuts to its end and the chapter card |
| 8 | Tooling: `@hold` with no argument crashed the compiler; the default visual-diff threshold missed a portrait expression change | `@hold` defaults to on. The README notes `--threshold 0.05` for fix rounds |

Confirmed as intended: 2.6 s of empty black between c1_0264 and the dream.
