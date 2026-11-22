# Matcher: which author items did the harness raise? (scoring step 3)

One fresh agent per build. It sees the author's items for that build and every report the harness wrote on it, and nothing else. Keep this prompt fixed between scoring runs so the counts stay comparable.

**Prompt:**
> You are scoring a review harness against the author's own notes on the same build. Be strict and literal; when in doubt, it's a miss. Read only the files below.
>
> **The author's items:** the entries with `"build": "{BUILD}"` in `{GROUND_TRUTH}` (both `items` and `liked`). Score only items with `"scored": true`; ignore the rest.
> **The harness reports on this build** (all in `{RUN_DIR}` unless absolute): `continuity.md`, `diagnosis.md`, `onmodel.md`, `build.md`, the three cold readers' notes `{READER_NOTES}`, and the lint output `{LINT}`. If a report is missing, say so and treat that check as having raised nothing. The build's scripts are in `{SCRIPTS}` if you need to look up a line ID or its text.
>
> **Step 1, findings.** List every distinct problem each check raised, one row per problem (merge repeats within the same check). A problem is anything the check presents as wrong, weak, confusing, heavy-handed, off-model or broken, including a cold reader's flat lines, heavy-handed hints, confusions and text/art mismatches. Not a finding: praise, the readers' percentages, guesses about the plot, "found fine." For the dialogue diagnosis, every FLAT or CUT verdict is a finding, plus each scene-level problem and each top fix. For each row give the check, where (line ID, scene or element), a short summary, and which author items it matches (by id; usually none).
>
> **Step 2, items.** For each scored author item, decide:
> - **hit:** at least one finding points at the same line or element (or a passage that plainly contains it) and names the same problem, or a problem whose obvious fix is the author's fix.
> - **partial:** a finding touches the same element but names a different or much vaguer problem, or names the same problem only for the chapter in general without pointing anywhere near the element.
> - **miss:** nothing does.
> Quote the finding (check name and its words) for every hit and partial. An item can be raised by several checks; list each with its own verdict.
>
> **Step 3, liked items.** For each `liked` entry, did any finding call it a problem? Quote it if so.
>
> Write a JSON file to `{OUT}` with this shape, and nothing else in it:
> ```
> {"build": "...", "missing_reports": [],
>  "findings": [{"check": "diagnosis", "where": "c3_0080", "summary": "...", "matches": ["A56"]}],
>  "items": [{"id": "A56", "verdict": "hit", "by": [{"check": "diagnosis", "verdict": "hit", "quote": "..."}], "why": "one line"}],
>  "liked": [{"id": "L02", "flagged": true, "by": [{"check": "reader2", "quote": "..."}]}]}
> ```
> Checks are named `continuity`, `diagnosis`, `onmodel`, `build`, `lint`, `reader1`, `reader2`, `reader3`. Reply with one line: "done", the number of findings, and the number of hits.
