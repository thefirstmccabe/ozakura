# Baseline: today's harness against the author's Ch1–3 punch lists (Nov 22)

**Run:** today's prompts (continuity, dialogue diagnosis, three cold readers, on-model, build review, plus lint),
each a fresh Opus 5.5 agent, on the four builds the author reacted to (`../../builds.json`), with each build's own
docs. 28 checks, then one matcher per build (`../../matcher.md`), then an independent check of every verdict
(`verify-matching.md`: one change, A45 hit → partial, and L01 unflagged). Table: `results.md`.

## The numbers
| | Items | Strict (hit) | Lenient (hit or partial) |
|---|---|---|---|
| All scored items | 46 | **12 (26%)** | 31 (67%) |
| Without the one hindsight catch (A23, lint check 6, built from that item) | 46 | 11 (24%) | 30 (65%) |
| Catchable from the text | 32 | 10 (31%) | 23 (72%) |
| Catchable from the screen | 13 | 2 (15%) | 8 (62%) |

- **Findings: 689; 72 matched an author item (10%).** About nine unmatched findings per match. Not all are wrong
  (he doesn't flag everything), but that's what a punch list built from these checks would bury his items in.
- **Partials are mostly "right line, wrong problem."** 19 items were touched without being named: c3_0351 flagged as
  a repeated laugh beat, not as edgy; the rain dodge flagged for something else; the kendo glosses flagged as too
  many when his complaint was too few.
- **Liked items:** reader 1 called Genji's "The tree doesn't mind" (L02) "a stock wise grandpa." The steps scene
  (L01) got line notes only.

## Where it's strong and where it's blind (strict)
- **Strong:** explains itself or on the nose, 4 of 6 (c3_0080, the camera beat, the interlude's c2_0277–0279);
  untranslated terms, 2 of 4; the "she" at c2_0090 (all six checks).
- **Blind:** flat or doesn't land, 0 of 3 (the jacket line, the class banter, "mostly vending machines"); tone,
  0 of 2; overplayed beats, 0 of 2; **callbacks, 0 of 2** (readers with perfect recall can't miss a callback);
  staging, 1 of 8, and that one is the hindsight lint catch (the back-of-the-wrist cut was missed even though today's
  on-model prompt names "which wrist"); engine and layout, 1 of 6 (the face flash, the full insert page before panels, tap to continue).
- **By check (strict):** the dialogue diagnosis 4, with the most findings (176); cold readers 4, 2 and 4; the build
  review 2; continuity 1; lint 1 (hindsight); on-model 0.

## History: what the harness said while these chapters were made
From the reports that existed when he got each build (`*/history.json`; Ch1 Oct 18, Ch2, Ch3).
- **It raised 8 of his 40 items at the time, and every one still reached him.** The overcorrection check restored
  two flagged lines (A19 the jacket line; A55 the camera exchange); two were rewritten three times and still
  explained themselves (A48, A49); the lunch text was changed to match the CG instead of the reverse (A66); A38 (more
  Nanoha) went to the author as a question.
- **At least three items were made by fixes for a reviewer:** glosses removed after readers said there were too
  many left c2_0076 bare (A25, A45); the dialogue pass cut c2_0089, the line that made "she" in c2_0090 mean Mizuno
  (A26); "six" was trimmed at c2_0071, leaving c2_0257 as the third use (A51).
- **The checks praised four lines he flagged:** the class banter (A21, "they work"; all three readers called it
  lively), "It's mostly vending machines" (A34), "It lands somewhere I wasn't guarding" (A56), the rain dodge
  (A64, "one of the best moments"). **And pushed the other way on two:** readers wanted more height in the collar
  CG (A12), and the build review switched another line to the deadpan face (A23).

## What it means for step 3 (§4 of the handoff)
1. **Taste is the gap, not effort.** The checks find problems, but not his problems, and sometimes praise exactly
   what he cuts. The taste judge (§4.3) built from his punch lists and likes is the lever; more fault-finding of the
   same kind would add findings, not hits.
2. **Triage loses what detection finds.** A line flagged by a check and then restored, or rewritten more than once,
   should go to a fresh reader (or the judge) before it ships. Fixes need a fresh read of the lines around them.
3. **Lossy-memory and screen-seeing readers (§4.1) are needed** for the two kinds at zero.
4. **Metric of record: the strict count [P].** The handoff's test for one handover per arc ("about two-thirds of his
   Ch1–3 items") is met already on the lenient count by vague neighbors, so it has to be strict. Report findings
   and the matched share alongside it.
5. **Noise, measured the same evening** (`../2026-11-22-run2/`, `rematch/`). A second identical run of all 28
   checks: strict 10 (vs 12), lenient 24 (vs 31); **only 6 items were caught both times, 16 at least once, and 20
   of the 46 verdicts changed.** A56 flipped again: flagged FLAT in run 1, praised in run 2. A second matcher on run
   1's reports gave the same counts (12 and 31) with 4 verdicts different, all borderline (A45 and A57 among them),
   so the matcher is steady and **the swing comes from the checks.**
   - **Scoring rule from now on [P]:** a candidate gets at least two runs; report the mean strict count and the
     count caught in both runs; a gain smaller than about 3 items is within the baseline's own swing.
   - **What the author gets is partly luck:** which of his problems reach a punch list depends on the draw. Running
     each check twice and keeping the union lifts strict catches from about 11 to 16, but doubles the findings too;
     a judge that filters them is what would make that usable (step 3).
