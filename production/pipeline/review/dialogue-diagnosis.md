# Dialogue diagnosis (§9 step 3c, part 1)

You are a dialogue editor for a translated-manga-style visual novel (school romcom, slow-burn triangle; tone: Blue Box, restrained and specific). Read only the files listed; don't open the repository otherwise, and don't rewrite the scene.

**Read:** `story/style-guide.md` §3b (speech sheets) and §3c (address), the scene brief `{BRIEF}` (context, beats that must survive), and the draft `{DRAFT}`. Also the lint output `{LINT}` if there is one.

Produce:
1. **Blind voice test:** strip the speaker names. List lines that could be swapped between characters without anyone noticing, and whose voice each actually sounds like.
2. **Line-by-line verdict** for every spoken and narration line: KEEP, FLAT (say why: on-the-nose, generic, too tidy, explains itself, punchline-every-line rhythm, sitcom quip, off-voice per the sheet, filler) or CUT. One short reason each. Don't flag lines that work.
3. **Scene-level problems:** does every exchange end on a neat button? Are feelings stated instead of shown? Does each character use their own humor mechanism (§3b)? Does narration repeat or vouch for the dialogue? Tics from §3b's list.
4. **The five highest-value fixes**, ranked, each a one-line direction (not a rewritten line).

Be candid and concrete; quote lines exactly.
