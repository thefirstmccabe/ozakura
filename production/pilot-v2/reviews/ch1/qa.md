# Ch1 revision: automated QA and visual regression (§9 step 6), Oct 18

**Playthroughs:** `qa_play.py http://127.0.0.1:8765/ <dir> --every` on the revised build, at 1180×820 and 820×1180. They ran just before the last five-line text fix (c1_0075, c1_0206, c1_0207, c1_0224, c1_0236); the build review covers those lines in the live build.

| | Landscape | Portrait |
|---|---|---|
| Lines seen | 259/259 (160 spoken + 99 narration), none missed | same |
| Voiced lines that decode | 159/159 | same |
| Bad requests | 0 | 0 |
| Script errors | none (one console error: Google Fonts blocked in the sandbox, `ERR_TUNNEL_CONNECTION_FAILED`) | same |
| Shots | 261 | 261 |

**Voice levels** (`voice_levels.py v2/voice`): 159 lines, median speech RMS −20.4 dB. Two flags: p_0007 and p_0010 (the dream, Despina with the echo) sit at about −6 dB, as in the Oct 17 build. Whether that's the intended softness is to be checked by ear.

**Visual regression** (`snapshot_diff.py` against the Oct 17 baseline, landscape): base 273 frames, new 259. 32 frames changed, 77 new or reworded, 91 removed or reworded. The big changes are the intended art: the intro CG and its falter (12–14% of pixels), the dream CG (7.8%), and the intro and night scene starts. The rest are small changes of 0.2–0.5% on lines next to rewritten ones. The removed frames are the old prologue scene and every reworded or cut line. The sheets stay in the session scratchpad (not committed, about 1 GB of shots); to regenerate them, see `baseline.md`.
