# Scoring the review harness against the author (Planning, Nov 22)

How many of the author's punch-list items would the review harness have raised before he saw the build? This kit
runs today's reviewer prompts on the builds he reacted to and counts. Every new reader, judge or prompt gets scored
the same way. **Keep a change only if the count goes up without burying it in false alarms** (report both).
Handoff: `production/pilot-v2/handoff-planning-nov22.md` §3.

## Files
- `ground-truth.json`: every author item in the Ch1–3 punch lists and the Oct 17 round, tagged by kind and by what
  could have caught it (text, screen, script, neither) [P tags]. `scored: false` items (decisions, design and
  casting, audio by ear, withdrawn, or not in the scored build) are left out of the count. `liked` items count
  against a check that flags them.
- `builds.json`: the four builds he reacted to, verified against git (see its `_about`).
- `setup.sh SCRATCH`: sparse worktrees at those commits (old review reports left out), cold-reader packets made with
  each build's own `reader_view.py` (names and glosses show as they did then), the dialogue briefs, today's lint.
- `make_prompts.py SCRATCH`: fills today's prompts from `production/pipeline/review/` for each build: continuity,
  diagnosis, three cold readers, on-model, build review. Docs are the build's own (canon, map, style guide as of that
  commit). The only change to the standard prompts is where output goes (a file, plus a one-line reply).
- `matcher.md`: the fixed prompt for the agent that matches findings to items (one per build).
- `score.py RUN_DIR`: the table (`RUN_DIR/results.md`).
- `runs/`: each scoring run's reports, matches and results.

## Running a score
1. `./setup.sh $SCRATCH` then `python3 make_prompts.py $SCRATCH` (change the prompt under test in
   `production/pipeline/review/` first, or point `make_prompts.py` at a candidate).
2. Launch one fresh agent per file in `$SCRATCH/prompts/<build>/`: "Your instructions are in FILE. Read it and
   follow it exactly." (28 agents; at most 20 run at once.) Reports land in `$SCRATCH/runs/<build>/`, reader
   notes in `$SCRATCH/readers/<build>/rN/`.
3. One matcher per build (`matcher.md`), writing `$SCRATCH/runs/<build>/match.json`.
4. `python3 score.py $SCRATCH/runs`; copy reports, matches and results into `runs/<date>-<name>/`.
5. **Run every candidate at least twice** (the checks are noisy: two identical baseline runs caught 12 and 10 strictly,
   only 6 items both times; the matcher itself is steady). `python3 compare.py RUN_A RUN_B` gives both counts, the
   items caught in both, and the verdicts that moved. A gain under about 3 items is within the baseline's swing.

**Metric of record:** the strict count (mean over runs, plus the count caught in every run), reported with the total
findings and the share that matched an item. The lenient count is shown but not used for decisions.

## Rules
- **Hindsight:** a few of today's checks were built from these very items (lint check 6 from A23, held
  expressions; the on-model prompt's "which wrist" from the Oct 17 round). Their catches are marked in the results;
  don't count them as evidence that the harness works.
- **The Japanese pass isn't scored:** the author can't read Japanese, so none of his items can test it.
- **Same model throughout so far** (Opus 5.5 for writer, reviewers, readers and matcher). Say which model ran each
  check when that changes.
- New punch lists add ground truth: append items with the build they reacted to, and add the build to
  `builds.json`.
