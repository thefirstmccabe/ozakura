# Ch1 punch-list batch, Oct 20 (§9 "punch-list batch")

## The author's items, and what was done
| Item (author, Oct 20) | Done |
|---|---|
| "Natsuki has a new look (Oct 20)… install it before anything else. You'll have to edit any references to shoulder length." | The design pass's seven school sprites and face windows are in `v2/img/ch/` and `v2/img/face/` (same names, same crop; her crown now sits at the sprite's top edge and isn't clipped in play). Redrawn with her long, soft waves and green eyes, each pasted back only around her so nothing else moves: the arrival CG, its falter (eyes toward the window side) and the title art. A new title living still, with the three figures held on its first frame. New thumbnails. c1_0139 no longer says shoulder length. |
| "I never want to actually mention hair color… It's just there." | Ch1's only mention was c1_0139. Now: "Her hair falls long and softly waved, brushed until it shines." [P]. Style guide §1a updated; canon §2 and the speech sheets go to the Story thread (`../../handoff-story-oct20.md`). |
| "Completely remove the cold intro for now. We'll add it back in later." | Out of the build: Ch1 opens on its title card, then the 5:40 alarm. The scene is kept in `script/cold_open.ozs` (with how to restore it); its images stay in `v2/img/` and `art/masters/`. The chapter menu starts at `c1_morning`; the dev chart numbers that scene 1.1. |

Flagged to the author: the cold open carried canon §1's "genre promised from the start"; without it, the dream at the end is Ch1's only uncanny beat (for the Story thread's Ch2–4 outline).

No voiced line changed. Spend about $1.46 (`../../ledger.md`).

## Checks
- **Automatic:** `script_lint.py` (only the dream's kept "says it like" ×2); `qa_play.py` at iPad landscape (256 of 256 lines, every voiced line decodes, no bad requests) and the phone (844×390) and desktop (1440×900) spot checks (same).
- **Snapshot diff** against today's handed-over build (iPad landscape, every line): 77 frames changed, every one with Natsuki on screen; c1_0139 reworded; nothing else.
- **Independent batch check:** below.
