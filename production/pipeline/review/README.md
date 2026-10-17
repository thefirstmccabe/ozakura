# Reviewer prompts for chapter production (style guide §9)

Each check in §9 is run by a **fresh agent that hasn't seen the work being made**. These files are the standard prompts, so every thread runs the same checks the same way. Copy the prompt, fill the `{PLACEHOLDERS}`, and launch it as a separate agent. Give reviewers file paths, not pasted text, and tell them what not to open.

| §9 step | Prompt | Tools |
|---|---|---|
| 3a Continuity | `continuity.md` | — |
| 3b Lint (automatic, before the reviewers) | — | `production/pipeline/vn/script_lint.py --chapter N` |
| 3c Dialogue diagnosis → rewrite → overcorrection check | `dialogue-diagnosis.md`, `dialogue-rewrite.md`, `overcorrection-check.md` | — |
| 3d Japanese pass | `japanese-pass.md` | — |
| 3e Cold readers ×3 | `cold-reader.md` | `production/pipeline/vn/reader_view.py` |
| 4 On-model image check | `on-model-image.md` | `production/pipeline/vn/cg_layout.py` (for the layout sketch) |
| 5 Voice levels (automatic) | — | `production/pipeline/vn/voice_levels.py` |
| 6 Technical QA and visual regression (automatic) | — | `qa_play.py --every`, then `snapshot_diff.py` |
| 7, 9 Build review (whole build, or one fix round's diff) | `build-review.md` | the snapshot-diff contact sheets |

**Order inside step 3:** continuity, then lint, then dialogue (diagnosis, rewrite, overcorrection check), then the Japanese pass on the final English, then cold readers on the result. Fix between steps. Keep each reviewer's report in `production/<deliverable>/reviews/<chapter>/` so the next round can see what was found.

**Reference run:** `production/tests/oct17-dialogue-coldread/` (the first cold reads and dialogue pass, Ch1).
