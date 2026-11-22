# History check: did the harness raise these items at the time? (optional scoring step)

A miss in the score can mean two different things: the checks never saw the problem (detection), or a check flagged
it and the thread kept the line (triage). This agent reads the reports the real harness wrote while each chapter was
being made and says which. One fresh agent per chapter; run it once per ground-truth update, not per scoring run.

**Prompt:**
> Read the author's items with `"build": "{BUILD}"` and `"scored": true` in `{GROUND_TRUTH}`. Then read every report in `{REVIEWS_DIR}` written before `{CUTOFF}` (the date the author first played the build; skip the punch-list files, `punch-*.md`, and anything after the cutoff). For each item, did any report raise the same problem in the same place (or an earlier version of the same line)? If yes, quote it (file and words) and say what the report or the thread did about it (fixed differently, kept on purpose, or no response). Write a JSON list to `{OUT}`: `[{"id": "A24", "raised": true, "where": "cold-read-round2.md", "quote": "...", "outcome": "kept: ..."}]`, then reply "done" and how many were raised.
