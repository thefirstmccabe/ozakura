# Ch2 punch list (author, Oct 25)

The author played Ch2 on his iPad and sent this list (discussion first, then "go"). Applied as one batch on branch `ch2-punch-oct25` (style guide §9, punch-list batch).

| # | Author's item | Done |
|---|---|---|
| 1 | The container line at the end of the restaurant part (c2_0299) is confusing: cut it or make it a text | Cut. Nanoha's food and the "Again." ritual now happen in person in the new Wednesday-morning scene (item 14). The walk home now shows the night street (`bg_houses_night`) instead of the restaurant, and "the light's on in Nanoha's window" shows her lit window (`bg_houses_night_lit`) instead of the bridge |
| 2 | c2_0076 needs the tap-for-a-note glosses | `{suburi|practice swings}`, `{Bogu|armor}` |
| 3 | c2_0090 needs a name: "she" read as Rika | "Two minutes later Mizuno has wiped…" (Kōhei's narration uses the name he says aloud, §3c), and Natsuki's teach sprite now appears with the line |
| 4 | A CG of the finished drawing in the kendo lesson | `cg_whiteboard`: the board with her stick figure and the four targets, shown after "So be afraid." (c2_0325, new narration). Wordless art, labels lettered in code (`art/ch2/whiteboard_letter.py`) |
| 5 | Glosses on every use of a Japanese term, not just the first | Every use in Ch2 (27 added) and Ch1 (kinpira, fusuma); the insert pages got four more gloss captions; the drawn-out calls open the base term's note (`{Kote-e-e!|Wrist!|kote}`); notes added for kote, dō, debana. Lines that explain their own word and honorifics stay bare (style guide §5) |
| 6 | Manga inserts: don't show the full page before panel by panel | The insert opens on its first panel; page turns open on the next page's first panel (style guide §4a updated) |
| 7 | "The floor belongs to whoever stays after practice" is confusing | "Until the first-years join, whoever stays after practice cleans the floor. It's usually me." |
| 8 | Switch the music after practice (the practice cue is battle music) | The practice cue fades out at the bow that ends practice (start of the debrief); the debrief and the mop race play without music; `memory` comes in at the catch, as before |
| 9 | The catch animation doesn't show her falling and being caught | Rebuilt: a new start frame with her heel slipping and him a step away, a Kling shot of the fall and catch with a push-in, joined on the held catch to the approved settle into the CG (5.4 s; `art/prompts.md`) |
| 10 | c2_0215: his face flashed embarrassed, then normal (first time only) | A real bug: the face window kept the previous face until the new one loaded (so only on a cold cache). Face windows now wait for their image, and upcoming faces load ahead |
| 11 | "Mostly vending machines" doesn't work | "Sapporo is four hundred pictures of snow." (re-voiced) |
| 12 | c2_0259: the same face flash (Kōhei's face before Natsuki's) | Same fix as 10 |
| 13 | Texts need a "tap to continue" note | A small pulsing "Tap to continue ▾" ("Click…" on a desktop mouse) under the chat while a text is up |
| 14 | c2_0282–0283 are cryptic | Rewritten (author approved the draft; the writing check then changed the end of c2_0282, which repeated the text message two lines later): "Natsuki liked her, and not the first-week way, where you like everyone." / "Nanoha lived next door to Fujisawa. Natsuki decided that was none of her business, and didn't quite believe herself." |
| 15 | A little Nanoha in Ch2 (the author's call; "whatever you recommend" for the shape) | New scene `c2_morning`, Wednesday morning in his kitchen (c2_0303–c2_0324, 15 voiced lines): she brings the food ("Again."), hears that his voice is rough, learns Mizuno stayed till close, gives his new face a number she'll tell him later, leaves a throat lozenge "for the talking," and is quiet a little too long on the walk. No new art |
| — | Natsuki's voice slightly too high (Audio thread: +0.5 semitone); Ch2 only for now | Ch2's Natsuki lines re-pitched from the kept takes at +0.5 (`voice_pack.py`); Ch1 stays at +1 until the author says otherwise |

## Checks
- **Writing check** (fresh agent; continuity, speech sheets, Japanese pass, glosses) on every new or changed line: three must-fix items applied (the whiteboard CG moved after Rika's punchline; c2_0315 "looks at me properly"; c2_0282's ending), plus c2_0174 "cleans", c2_0313 ("after karaoke, with some girls from class"; 連中 was dismissive), c2_0316 "That one's new.", and zanshin glossed "staying alert after the strike" where Takatsuki uses it. Kept on purpose: two girls reading Kōhei's face in one chapter (§3b lists it as a tic; here one notices a physical detail and the other keeps a catalogue). For Story: c2_0324's change of subject resembles Ch3's window talk; "Chibi" (c1_0256) has no gloss (a nickname; the author's call).
- **Voices:** 15 new takes transcript-checked (Wizper; 15 of 15 match); levels within the usual range (only the two known dream lines flag).
- (cold read, on-model check, playthrough, snapshot diff and the independent check: below as they finish)
