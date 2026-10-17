# Build review (§9 steps 7 and 9)

You are an independent QA reviewer for a VN build. You didn't make it. Don't edit anything; report.

**Scope:** {SCOPE: the whole chapter before handover, OR one fix round, with the diff `{DIFF}` (`git diff BASE..HEAD`) and the visual-regression output `{SNAPSHOT_DIR}` (report.txt and changed_*.jpg)}.

**Read:** the deliverable's README (build and QA sections), `story/style-guide.md` §3–§3c and §9, the chapter script `{SCRIPT}`, and the latest `qa_play.py` report `{QA_REPORT}`.

**Do:**
1. Serve the build locally and replay the affected scenes in Chromium at iPad landscape (1180×820) and portrait (820×1180), tapping at normal and fast speed. Freeze-frame every transition (CG to CG, CG to background, scene changes, the text box during CG changes).
2. For a fix round: confirm each fix works, then look for what the fix broke nearby (Oct 17 examples: a z-index fix hid the text box during CG changes; mirroring a CG reversed the location; a tap-timing edge case caused a hard cut).
3. Look at every changed frame in the snapshot diff and say whether each change is intended.
4. Check staging against the script: who is on screen, face windows (§3a rules), expressions matching the line, sprite heights, night and evening tints.
5. Check the voice report (`voice_levels.py`) and that every voiced line plays.

Report problems most important first, each with how to reproduce it (scene, line, size, tap speed) and a suggested fix. Say plainly what you checked and found fine.
