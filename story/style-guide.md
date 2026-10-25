# Ōzakura — Style Guide

How Ōzakura looks and sounds, and how to generate it. Read this before any art, audio or lettering work. Rebuilt 2026-10-05; updated 2026-10-08 with the Akane and Natsuki redesigns, the house layout and the voice re-cast.

---

## 1. Reference hierarchy
1. **The written designs in `ozakura/canon.md` §8.** They govern wherever an image disagrees.
2. **Approved redesign references** (Oct 6), in the repo:
   - **Akane:** `production/refs/akane-v2/`.
     - `01-lavender-base.png`: the approved hair color and face direction. She reads slightly too old here.
     - `02-sailor-uniform.png`: **the age and proportion target**, and her school-day uniform.
     - `03-bedroom-plushies.png`: her room and at-home clothes. She reads slightly too young here, and her hair drifted gray.
     - `x-rejected-*`: the color options that weren't chosen.
   - **Natsuki (Oct 20):** everything is in `production/design/natsuki-oct20/` (the author chose the look from `options.jpg` there): long, soft brushed-out waves and green eyes. **Her school sprite set governs hair length, hair color and the face:** since Oct 24 the face is **face A** (`production/design/natsuki-oct24/`: the installed set, and the 2K base master `master/natsuki-school-base-faceA.png`, which new Natsuki images start from); hair, body and scale are still the Oct 20 set's (`sprites/`, `faces/`, `master/` there). `natsuki-lock-uniform.png` is the full-body reference for pose, build and scale; its hair runs a little shorter and darker than the sprites', so follow the sprites. Her legs still run a bit long for 5′3″. Method and pitfalls: that folder's README.
     - `production/refs/natsuki-v2/01-restyle-uniform.png` (Oct 6): pose and styling direction only; its shoulder-length hair and amber eyes are retired.
     - `02-restyle-casual.png`: the styling idea only. **Do not use** its outfit, which reads as a twenty-something.
3. **The author's concept references** (`production/refs/handoff/`):
   - **Nanoha:**
     - `Nanoha-School-Braid.png` is the primary face and uniform reference.
     - `Nanoha-School-Loose.png` shows her hair down at home.
     - `Nanoha-Pajamas-Bun.png` shows the top bun. Make the scrunchie puffier.
   - **Natsuki:** `Natsuki-Options.png` (center option B only, for face; its hair and eyes are superseded, Oct 20) and `Natsuki-Athletics-Ponytail.png` (the athletic look).
   - **Rule:** these are concept art. **Never copy their elongated legs and torsos.**
4. **The ChatGPT lineup and style anchor** (`production/refs/vn-original/`), especially for Kōhei, who has no approved image.
5. **The shipped VN sprites** (`img/ch/*.webp`): the model sheet for the supporting cast only. For the leads they're superseded where canon differs. Akane's are entirely superseded.

**Raw repo URLs work directly as `image_urls`:** `https://raw.githubusercontent.com/thefirstmccabe/ozakura/main/<path>`

**Design rules:**
- **Proportions:** natural, compact and age-appropriate.
- **Appeal:** comes from personality, expression, styling and presence. **Never design or frame the school-age cast for figure or sex appeal.**
- **Hair color:** a medium convention, and never mentioned in story text at all, in narration or dialogue, for any character (author, Oct 20; it's just there). Length, cut and style can be described. Art prompts still name colors.

## 1a. Design lock, Oct 10 (humans APPROVED by the author; the beast is approved for scale, with an ethereal tweak pending)
All files are in `production/refs/design-oct10/`. They outrank every older image for these characters.

| Who | Reference | Notes |
|---|---|---|
| Kōhei | `r3/kohei-short-A.png` | Shorter, slightly unruly dark-brown hair, fringe above the brows, warm. |
| Kōhei face set | `r4/faces/01–10` | Warm smile, neutral, grin, deadpan, surprised, flustered, annoyed, serious, the stillness (shadow over the eyes), sad. Used for his face window on every spoken line. |
| Akane | `r3/akane-teen-uniform.png`, `r3/akane-teen-home.png` | Teen proportions. **Method:** the pilot sprite `img/ch/akane_home_smile.webp` is the face, age and proportion anchor, with lavender-silver hair and a sweet expression on top. Earlier `akane-v2` images read too young; use them only for hair color. |
| Akane with Kōhei | `r4/akane-kohei-height-2.png` | Scale check: her head reaches about his shoulder, and her head is smaller than his. |
| Natsuki casual | `natsuki-casual-A.png` (main), `natsuki-casual-B.png` | Outfit references only: their hair and eyes predate Oct 20, so correct both to the Oct 20 look (§1). School look: `production/design/natsuki-oct20/`. |
| Kirishima (male) | `r3/kirishima-masc-A.png` | Crew cut, square jaw, broad shoulders, deadpan. Replaces the female sprite set. |
| Fairy | `r3/fairy-shoulder.png`, `r3/fairy-desk.png` | **Scale method:** always show her next to a person or a known object (shoulder, pencil, mug); alone, the model draws her full-size. Rounded ears, no wings, petal robes. |
| Beast | `inventory/beast-size-reference-v2.png` (**current, Oct 10**), `inventory/beast-ethereal-town.png` | **Size rule (raised Oct 10):** back at a man's belt line (about 3′4″ at the shoulder), ear tips at his chest (about 4′3″). A really big dog, not a giant. The model gets size wrong; pass `beast-size-reference-v2.png` as image 1 in every beast prompt, and fix in post if needed. The older `r4/beast-size-reference.png` is superseded. `beast-scene-past-2.png` is a mood concept only; the wolf is still too large. |

**Draft color swatches** (sampled from the references above; verify in the sprite pass):
| Character | Hair | Skin | Eyes | Key colors |
|---|---|---|---|---|
| Kōhei | #3d3232 (highlight #5b4747) | #efccbb | warm brown | blazer #3f4050, tie burgundy |
| Nanoha | #51423d (highlight #6d615e) | #eddace | brown | same uniform; ribbon burgundy |
| Natsuki | #b55e36 (shadow #6c3c2f) | #f5dbca | **green**, jade (sprite sample about #6a8867; light #8eaf85, dark #294030) [P shade], Oct 20 | same uniform |
| Akane | #d0c2d5 (shadow #a89cb0) | #f7ebe6 | gray-violet | sailor navy #454c64, scarf red, cardigan cream #f1e6d4 |
| Kirishima | #08080a | #d7c1b4 | dark | keikogi #e5ded8, hakama #242632 |
| Fairy | #252330 | pale | dark | robes pale pink and white, faint warm glow |
| Beast | fur #1f1f21 (light #565452) | — | glowing gold | mask #d2cbbe, mist #aca59a |

## 1b. Visual inventory, Oct 10 (self-reviewed by Claude; awaiting the author's review)
Everything is in `production/refs/`. Review boards are listed in the production log archive (`story/archive/production-log-to-oct14.md`, 10-10 rows). **[P]** marks a choice Claude made that the author hasn't confirmed.

**Scale lineups** (`lineup/lineup-1-school.png`, `lineup/lineup-2-family-past.png`): composited in code from the full-body references, bottom-aligned on a 6-inch grid (code: `production/pipeline/layout/lineup.py`). **Units: imperial only** (author's rule, Oct 10). Heights: Kōhei 5′9″, Nanoha 4′11″, Natsuki 5′3″ and Akane 5′0″ are set; all others are **[P]**: Ryōsuke 5′7″, Rika 5′1″, Takatsuki 5′8″, Kirishima 5′11″, Yuzu 5′1″, Ōno 6′0″, adviser 5′6″, manager 5′5″, Kazuo 6′0″, Emi 5′2″, Sōta 4′0″, Genji 5′2″ (stooped), Kōhei's mom 5′2″, his dad 5′8″, the rōnin 5′9″, past Natsuki 5′2″, her father 5′5″, thug 5′10″, tournament opponent 5′8″. Beast: 4′3″ to the ear tips.

| Group | Files (`inventory/` unless noted) | Notes |
|---|---|---|
| Nanoha's family | `kazuo-B.png` (**chosen Oct 10**), `kazuo-A.png` (alternate), `full-emi.png`, `full-sota.png`, `genji.png` | Kazuo B is the off-duty mentor (training mitts); A is the work look. |
| Kōhei's parents | `kohei-mom-grief.png`, `kohei-mom-recover.png`, `kohei-dad-healthy.png`, `kohei-dad-ill.png` | Mom's two states track her recovery arc. Dad appears only in flashbacks. |
| School adults | `adviser.png`, `full-ono.png`, `full-manager.png` | |
| Supporting cast, full body | `full-kohei`, `full-nanoha`, `full-akane`, `full-kirishima`, `full-takatsuki`, `full-ryosuke`, `full-rika`, `full-yuzu` | Natsuki's full-body reference is `production/design/natsuki-oct20/natsuki-lock-uniform.png` (Oct 20). |
| Past life | `ronin-B.png` (chosen; **wears two swords**, katana and wakizashi, Oct 10), `ronin-A.png`, `past-natsuki-B.png` (outing: shawl, green kimono), `past-natsuki-A.png` (everyday), `past-father.png` | |
| One-scene antagonists | `thug.png`, `opponent.png` | Opponent: **bleached-blonde hair** (author, Oct 10). Thug: black undercut [P], changed from blonde so the opponent's hair stays distinctive. |
| Seasonal outfits | `out-{kohei,nanoha,natsuki,akane}-{summer,yukata,winter}.png` | Natsuki's outfits only: her hair and eyes in these predate Oct 20; correct them to the lock (§1). |
| Kendo armor | `bogu-kohei.png`, `bogu-natsuki.png`, `bogu-takatsuki.png` | |
| Fairy seasons | `fairy-summer.png`, `fairy-autumn.png`, `fairy-winter.png`, `fairy-bloom.png` | Each shown over a hand for scale (§1a method). |
| Beast, ethereal tweak | `beast-size-reference-v2.png`, `beast-ethereal-town.png` | **Approved Oct 10.** Ink-black fur with a faint shifting multicolor sheen, at the raised size (§1a). `beast-ethereal-size.png` shows the old, smaller scale; don't use it for size. |
| Turnarounds (animation) | `turnarounds/{kohei,nanoha,natsuki,akane,ronin,past-natsuki,beast,fairy}.png` | Front, side, back at one scale; the beast sheet adds mask and paw details. Known nit: Akane's bag is on the wrong side in her side view. Natsuki's sheet predates her Oct 20 look (shoulder-length hair); redo it from the lock before animation work. The rōnin sheet shows both swords. |
| Locations | `locations/houses-street.png`, `window-night-from-kohei.png`, `window-day-from-nanoha.png`, `nanoha-room-day.png` | The houses about three feet apart with no path between them, and the facing windows both ways (fixes 18 and 31). Built from layout sketches in `locations/sketches/` (code: `production/pipeline/layout/house_sketches.py`). |
| The Great Cherry | `locations/tree-{summer,autumn,winter}.png`, `tree-newyear-bloom.png` | Season edits of `img/bg/bg_shrine_tree_day.webp` (the spring view), so the site stays identical. New Year: snow, out-of-season bloom, lanterns. |
| Past era | `locations/past-tree-site.png`, `past-tree-bloom.png`, `past-mist-path.png`, `past-village.png` | Same tree and boulder, no shrine buildings, shimenawa and a stone marker, thatched village below. **Winter** (canon §5, Oct 10): light snow, frost and mist, so the bloom plate shows blossoms falling on snow. The village is an autumn establishing shot. |

**Known issue for the final sprite pass:** Nanoha's skin renders too pale or gray in some images (lineup, turnaround). Check every Nanoha sprite against her skin swatch (§1a); the author doesn't need these redone now.

**Not made yet (per chapter, when needed):** ordinary backgrounds, event CGs, the old grave or memorial (canon: Open), the Tachibana and Fujisawa interiors beyond what's shipped, the town map.

## 2. Character visual sheet
| Character | Hair | Eyes / face | Height | Outfits | B&W rendering |
|---|---|---|---|---|---|
| Kōhei | **Dark brown**, somewhat unruly, uneven fringe leaving the eyes visible. Black or spiky hair is drift | Brown, expressive; youthful, handsome; warm, easy smiles, no permanent scowl | **5′9″** | Navy blazer (gold buttons, open), white shirt, burgundy striped tie loosened, charcoal trousers. Kendo: navy keikogi and hakama. Work [P, Ch2 Oct 24]: white T-shirt and a brown bib apron (a cartoon chef on the pocket), tied like a hakama (was: white shirt, dark waist apron) | Solid black with white highlights |
| Nanoha | Natural dark brown, below the shoulder blades when down. **School/outings:** loose side braid. **Home:** long and loose. **Bed:** loose bun on *top* of her head with a BIG SOFT scrunchie. **Clip:** a small hair clip on her left side, as the sprites and the collar CG draw it (approved by the author Oct 20) | Brown eyes, soft oval face; deadpan is her key expression | Petite, about 4′11″; head reaches Kōhei's chin | Navy blazer, white shirt, burgundy ribbon, **charcoal plaid pleated skirt**, dark socks, brown loafers. Pale-blue pajamas with a small cat detail | Dark tone (nearly black), glossy highlights |
| Natsuki | Bright burnished copper. **Long** (in front, nearly to her waist; match the sprites), **soft brushed-out waves**, side-swept fringe, **polished and glossy, never tousled or windswept** (Oct 20). **Drift risk:** the model makes the waves longer, bigger and messier; check every image against her sprite. **Athletics:** ponytail (longer now [P]) | **Green** (jade [P shade], Oct 20) with expressive brows; **warm, quietly confident, slightly knowing smile**; poised posture. Not a tomboy grin. **Face A (author, Oct 24):** rounder, larger eyes with a stronger lash line and a light hatched blush, drawn closer to Nanoha's sprite; her body, hair and scale are unchanged (`production/design/natsuki-oct24/`; base master `master/natsuki-school-base-faceA.png`, which new Natsuki images start from) | **5′3″**, athletic; exact build Open | Same uniform as Nanoha, worn neatly. Kendo: faded, much-washed indigo keikogi. Casual: put-together and fashionable but **age-appropriate** (short cardigan, casual skirt or jeans, sneakers), camera on a strap. Athletic: navy track shirt and dark sweats | Medium-gray tone, clearly lighter than the dark-haired cast, bright highlights |
| Akane | **Pale lavender-silver**, soft and wispy, shoulder length, small side clip | **Gray-violet**, big and soft; round, soft face with fuller cheeks; slightly pale with a faint blush; sweet expressions. Clearly younger than the high-schoolers | Small and slight, compact (about 14) | **School:** sailor uniform (navy collar with white stripes, white body, red scarf, navy pleated skirt below the knee, white socks, loafers; plush-rabbit bag charm). **Home:** cute and youthful (cream cardigan, pink bunny-ear hoodie, lavender lounge pants, fuzzy socks). Room full of plushies | Light tone (pale hair) with soft highlights |
| Past-life Natsuki | Copper, tied back with a plain cord | **Face hidden in the manga** | — | **A real kimono, simple and everyday**, as worn by a modestly propertied family. Not elaborate, not peasant work clothes | Medium-gray tone |
| Rika | Black, two low pigtails, novelty clips (strawberry, star, frog with a crown) | Big and expressive | — | Uniform with a cream cardigan under the blazer | — |
| Ryōsuke | Neat black | Rectangular glasses; composed, smug | — | Uniform, striped tie | — |
| Yuzu | Light honey-brown, shoulder length, red clip | Cheeky grin | — | White blouse with name badge, burgundy waist apron, black skirt | — |
| Kirishima | **Male (Oct 10):** black crew cut, square jaw, broad shoulders | Calm, unreadable, deadpan | 5′11″ [P] | White keikogi, navy hakama | — |
| Takatsuki | Swept-back, **deep slate blue** (blue-black with steel-blue highlights) [P], Oct 10, for readability against the dark-haired cast | Sharp; **precise and composed, not sneering** (redesign) | — | Navy keikogi and hakama | — (prone to drift; always pass his sprite) |
| Emi | Dark hair, low bun | Warm | — | Light-blue shirt, mustard-yellow apron | — |
| Mio, Nanoha's little sister (was Sōta) | **Locked Oct 13: design D** (`production/refs/inventory/sister-D.png`): dark-brown bob with blunt bangs and one small side braid | Gap-toothed grin; smug, arms crossed; the bossy gremlin | about 4′0″ | Mint T-shirt with a star print, tiered plaid skirt over bike shorts, mismatched socks, sneakers, bandage on her elbow; a generic controller (no logos) | — |
| Ōno-sensei | Slightly messy | Droopy and tired; 40s, tall and thin | — | Knit cardigan over shirt and tie | — |

**Color swatches (to lock in the design pass):** manga inserts are full color in the VN style (Oct 10), so each character needs locked hex values for hair, eyes, skin and key outfit colors, checked against every insert panel. The B&W rendering column above applies only to the legacy Vol. 1 manga.

**High-school uniform** (proposed, not a settled school identity; no invented insignia): navy blazer with gold buttons, white shirt, burgundy ribbon or tie, charcoal **plaid** pleated skirt (trousers for boys), dark socks, brown loafers.

**The two houses:**
- Built almost touching, **about three feet between the walls**. Upstairs bedroom windows face each other within arm's reach (Muv-Luv Extra). No alley or stairs between them.
- The shipped `bg_street_houses` and `cg_window_night` are wrong (pilot-notes fix 18). Replacements: `production/refs/locations/houses-street.png` and the two window views (§1b).
- **Method for layout-critical backgrounds:** see §6.

## 3. VN art (color)
**Sprites:**
- **Format:** thigh-up, front three-quarter view, 2:3, 2K, plain white background. Cut out with `fal-ai/bria/background/remove`. Stored as `.webp`, named `{char}_{outfit}_{expr}`.
- **Bases:** `fal-ai/nano-banana-2/edit` with [character reference + style anchor] as `image_urls`. Prompt: "Keep him/her exactly as in image 1: …" + the full appearance spec + the style line + framing + "Background: plain solid pure white, no shadow, no text, no border. Single character only."
- **Expressions:** an edit of the base sprite with only that image as input: *"Edit image 1: change ONLY her facial expression to {expression}. Keep everything else exactly identical: same pose, same hands, same body, same hair, same clothing, same framing, same size and position in the image, same art style and colors, same plain white background."*
- **Style line:** "detailed expressive ink linework with natural soft painted color, Japanese manga illustration, delicate hatching texture on fabric."
- **Using expressions in scripts (author, Oct 24):** a deadpan (Nanoha) or a smirk (Natsuki) plays its punchline and, at most, the one line that answers it, then the sprite changes back to a warm face. Held through ordinary talk, they make relaxed conversations read tense. Natsuki's smirk is for competitive beats (sizing someone up, a challenge); her questions use `curious`. Nanoha's `dry` face (a deadpan joke with a hidden smile) is for her affectionate bits; plain `deadpan` stays for the flat punchline. `script_lint.py` check 6 flags a deadpan or smirk still on screen two lines after it was set.
- **Age cue for Akane:** "clearly younger than a high-schooler; compact proportions with a slightly larger head relative to the body; rounder, softer face with fuller cheeks; larger eyes."

**Backgrounds and CGs:** `fal-ai/nano-banana-pro/edit` (higher fidelity), 16:9. Pass the relevant sprites and the style anchor for CGs. **Screens:** landscape only (canon §2); no portrait layout.

**Current inventory:** 74 sprites (14 outfit sets; Oct 24 added Nanoha's `dry` and Natsuki's `curious`), 16 backgrounds, 9 CGs (title, hands and strap, Natsuki intro, jigeiko, the catch, Yuzu at the counter, window night, shrine meeting, past life).

**Short animations and living stills** (canon §2): living stills are Kling v3 Pro loops (start frame = end frame). For the few short animated moments (the Ch2 catch first): animate between approved stills, Kling for restrained moments (it stayed wide and on-model in the Oct 10 `cg_catch` test; MiniMax H3 Max pushed in and cropped), and give every shot its own approved start frame, because in-generation cuts drift (Oct 12). Tests: `production/cutscene-test/`.

## 3a. VN presentation: face windows and dialogue colors (locked Oct 10)
**Face windows** (bottom left, beside the text box, Baldr Sky style). A face window stands in for a sprite that isn't on screen.
1. **Kōhei: a window on every spoken line,** with the expression matching the line. He's the POV and never on stage. Narration and inner thoughts get no window.
2. **Everyone else: a window only when they speak and their sprite isn't on screen** (offscreen voice, next room, behind him, a crowded scene, or a CG that doesn't show them). If the sprite is on stage, no window.
3. **Interludes:** the interlude's POV character takes Kōhei's place: a face window on her spoken lines, never a sprite (author, Oct 17). Everyone else follows rule 2, and if Kōhei appears in an interlude he's on stage like anyone else.
4. **Never:** phone texts (chat UI), speakers with no sprite (the manager), "???", or past-life scenes (her face stays hidden). Ōno-sensei has a sprite since Pilot v2 (Oct 17), so he follows rule 2.

**Assets:**
- **Kōhei:** a dedicated face set of about 10 expressions: neutral, warm smile, grin, deadpan, surprised, flustered, annoyed, serious, the frightening stillness, sad.
- **Everyone else:** windows are crops of their existing sprite expressions, at no art cost. Akane, Natsuki and the male Kirishima get theirs from their new sprites.

**Dialogue colors:**
- **Name tags** in the full character color.
- **Dialogue text** in a pale tint of the same hue, almost white at a glance.
- **Narration** stays neutral off-white.
- **The backlog** uses the same colors.
- **Why:** it separates Kōhei's spoken lines from his first-person narration, and it makes fast banter easy to follow.
- **Readability:** every tint must pass a contrast check on the text box. Build a test screen and approve it on iPad before rollout.

| Character | Hue |
|---|---|
| Kōhei | warm light brown |
| Nanoha | soft pale blue |
| Natsuki | copper / amber |
| Akane | lavender |
| Ryōsuke | teal |
| Rika | strawberry pink |
| Takatsuki | steel blue-gray |
| Kirishima | indigo |
| Yuzu | cherry red |
| Emi | mustard yellow |
| Sōta | dinosaur green |
| Past-life Natsuki ("???") | faded gold |
| Others | neutral (no tint) |

## 3b. Character speech sheets (Oct 17; owned by the Story thread, PROVISIONAL)
Speech rules, not personality summaries; personalities are in canon §8. Address forms and Japanese pronouns are in §3c. Drafts and dialogue passes use these (§9). The author doesn't approve them line by line; his punch lists tune them. Built after the Oct 17 cold reads found that one dry deadpan voice (Nanoha's) had become everyone's: Akane read as a younger Nanoha, Natsuki sounded like Nanoha whenever she joked, and Ryōsuke's bits ran on the same rhythm.

**Rules for all dialogue:**
- Translated-manga feel: natural modern English, contractions, honorifics kept.
- Not every exchange ends on a punchline. Lines can trail off, get interrupted, get ignored or miss.
- People rarely say what they feel. They deflect, change the subject, act, or say something adjacent.
- Restraint (Blue Box): quiet moments stay quiet; nobody gets wittier just to be lively.
- No line explains its own joke; no one narrates their feelings in therapy language; no manga self-reference.
- **Japanese words** (Oct 19): name foods and things freely; Production glosses them with translator's notes (style guide §5). Nobody explains their own culture to each other.
- **Nanoha's height** (Oct 19): one light height beat per chapter at most (Ch1's: the kitchen joke, plus "Chibi"), and never a height claim in a beat a CG shows unless the art shows it.
- **Narration** (Oct 19): don't repeat a sentence as its own line for emphasis.
- **Tics to avoid** (found in Ch1): the deadpan "I'm very X" joke across characters (keep "very" rare); narration's "She says it like…" and "the way you…" more than once a chapter; two girls reading Kōhei's face in the same chapter; American-internet bits that break the translated feel (the hot-dog-is-a-sandwich debate, "sub roll").

| Character | Rhythm | Humor | Dodges feelings by | Never |
|---|---|---|---|---|
| **Kōhei** | Short; one sentence, often a fragment | The straight man: literal answers, understatement, mock seriousness; plays along with bits rather than topping them | Going practical (schedules, food), "It's fine," changing the subject; sincere flirting makes him go shorter, not cleverer | Matching a flirt with an equally polished line; speeches about himself; admitting he's tired |
| **Nanoha (private)** | Measured, precise vocabulary | Committed deadpan bits and elaborate straight-faced theories; keeps score | Hiding inside the bit (Ch1: "If they split us up, I'd have to make new friends. Nobody wants that." / "Least of all the new friends."); a quiet "Mm"; a very specific practical detail | Saying what she wants about Kōhei |
| **Nanoha (public)** | Gentle, polite, a little formal; small hesitations ("Um—", "If you'd like…") | At most one dry understatement | Formality (bravery looks like politeness) | Snark; teasing someone she just met; loud enthusiasm |
| **Natsuki** | Easy and fast; questions, "Hey," "So," uses names early | Outward: pokes, challenges, teasing by noticing physical details (calluses, posture, which stair squeaks). She asks; Nanoha states | Getting *more* entertaining when hurt; making big invitations sound casual; a laugh to close a moment. When sincere, she goes short and quiet (Ch1: "Six new schools. Every dojo bows the same way."), then closes it with a laugh | Verdicts and self-labels ("you're fun," "I'm pushy"); Nanoha's dry deadpan; practiced-sounding flirting |
| **Akane** | Sing-song, younger, exaggerates | Sibling teasing; resists being managed with pouting and cheerful defiance ("Onii-chan, you're hovering again") | A quiet sincere line under the teasing; forced brightness on bad days | Nanoha's mock-formal deadpan; adult wit; sniping |
| **Mio** | Bossy, little-kid bluntness | A tiny princess giving Kōhei orders ("Kō-nii, sit there"); trash talk and sore losing at fighting games | Changing the game | Sounding older than about 7 |
| **Rika** | Exclamations, run-ons, topic jumps, nicknames | Enthusiasm and non-sequitur; schemes she thinks are subtle | More volume | Dry understatement (and let her have more than volume: specific obsessions, like the hair clips) |
| **Ryōsuke** | Measured, complete sentences, structured arguments | Pedantry about trivia, argued with total seriousness, on topics a Japanese teen would pick (his Ch1 entrance: whether you eat a taiyaki head or tail first) | Retreating into trivia | Emotional speeches; enthusiasm |
| **Takatsuki** | Complete, correct sentences; few contractions; exact kendo vocabulary | Unintentional: dead serious and literal about rules and form. Unlike Kōhei's short, plain straight man, he is formal and complete | Citing form and rules; precise criticism instead of feelings; going quiet. When he finally says something personal it's short and blunt ("You scared her. You scared me too.") | Mocking Kōhei's missed practices; slang; sarcasm |
| **Kirishima** (captain) | Terse; coaching in single sentences ("You stopped for half a second. Don't.") | Deadpan that lands a beat late; nobody laughs, and he doesn't wait for it | Changing the drill | Speeches; shouting |
| **Emi** (Nanoha's mother) | Warm, brisk, runs on food | Cheerful bluntness; embarrassing teasing ("Competition, is it?") | Feeding people | Wallowing; lecturing Kōhei. When serious she's blunt and loving ("Your kids just want their mom back.") |
| **Kazuo** (Nanoha's father, the mentor) | Big and quiet; few words, plain and practical; asks questions | Very dry, rare | Telling a concrete story from his own life (the karate club) | Therapy language; abstract lectures (his one image, "be more like the tree," grows out of a story); letting Kōhei off the hook |
| **Kōhei's mom** | Early on, few words, quiet and apologetic; later, small, slightly rusty attempts at ordinary mom-talk | Barely any at first; it returns as she does | Apologizing; going back behind the fusuma | Melodrama; naming or explaining her condition |
| **Genji** (Nanoha's grandfather) | Easygoing old man | Cheerful evasions (his very convenient back) | Changing the subject to the weather or the tree | Oracle speeches; folk knowledge comes out as gossip and habit, not lore dumps |
| **Ōno-sensei** | Weary, dry; refers to himself as "Sensei" | Bureaucratic understatement ("through channels I'd like to know more about") | Paperwork | Enthusiasm |
| **Yuzu** (work kōhai) | Cheeky, sing-song "Senpai~"; switches to a flawless customer-service register on cue | Scoring points out loud ("Point to Shiina"); bold verbal flirting | Going short and flustered when someone is sincerely nice to her | Serious romance talk; real meanness to Nanoha or Natsuki |
| **The manager** | Harried | "You're a lifesaver" about nine times a shift (one-note on purpose) | More shifts | Depth |
| **Chie** (mostly texts; a phone call at Christmas) | Short texts | A blunt best friend who sees through Natsuki's cheerfulness and asks the real question | Sending zunda mochi | Long messages |
| **Past-life Natsuki** | Gentle, polite Japanese (desu/masu); few words; a grown woman, warmer and slower than a teen | Scolding with love ("You're late." "Hurt again.") | Tending his hurt | Modern phrasing; saying his name |
| **The fairy** | Short exclamations, old-fashioned turns of phrase | Old but childlike: curious, a little vain, food-motivated, mischievous with Nanoha; remembers what she cared about (cookies), not what's useful | Wandering off the subject | Exposition without personality; knowing everything |

## 3c. Address and pronouns (decided Oct 17; Claude's choices, delegated by the author)
Canon §2: honorifics and changes in address matter. This sheet supersedes pilot-notes §4. Japanese lines (the voiced column) follow the pronouns and forms here exactly. **English** keeps honorifics, sibling terms and Japanese nicknames ("-san," "Onii-chan," "Kō-chan," "Chibi"), but translates parent, grandparent and neighbor-adult terms (Mom, Grandpa, Auntie, Uncle). **Kōhei's narration** uses the name he uses aloud ("Tokiwa," "Mizuno"), except that Nanoha is always "Nanoha" in narration. Interludes follow their POV character.

**Self and "you" (Japanese):**
| Character | "I" | "You" / how they address people |
|---|---|---|
| Kōhei | ore | *omae* to Nanoha, Akane, Ryōsuke, Takatsuki; Natsuki by surname only, never *omae*; casual with the Tachibana adults, polite with teachers and strangers |
| Nanoha | watashi | Names, never *anata* or *anta*; polite *desu/masu* with strangers |
| Natsuki | watashi | *kimi* to Kōhei (her signature); names for everyone else |
| Akane | watashi | Names; "Onii-chan" |
| Mio | refers to herself as "Mio" (third person) | Orders, names, "Kō-nii" |
| Rika | atashi | Nicknames |
| Ryōsuke | ore | Surnames |
| Takatsuki | boku | Surnames, avoids "you"; one register break to *omae* when he confronts Kōhei about going to the adviser together (Ch20) |
| Kirishima | ore | Bare surnames |
| Emi | watashi | Affectionate names |
| Kazuo | ore (with Kōhei) | "Kōhei" |
| Genji | washi | Bare given names |
| Ōno-sensei | "Sensei" | Bare surnames |
| Yuzu | watashi | "Senpai" |
| Past-life Natsuki | watashi (polite speech) | *anata*; never his name |
| Past-life Kōhei (the rōnin) | ore | *omae* to his wife (a contrast with his never using *omae* to Natsuki now) |
| The fairy | watashi, in old-fashioned plain speech | Bare given names |

**Who calls whom what (at the start of the story):**
| From → To | Form |
|---|---|
| Kōhei → Nanoha | Usually no name at all (*omae*, the way close people talk); when he teases her, **"Chibi"** ("shorty"), his nickname for her since middle school, playing on her height. It means *little kid*, and he doesn't hear it that way (see the shifts below) |
| Nanoha → Kōhei | "Kōhei" by default; **"Kō-chan"** at private teasing or tender moments ("Kō-chan. Your collar." "Good night, Kō-chan."), never in front of the class |
| Kōhei ↔ Natsuki | "Mizuno" / "Fujisawa" (she adds *kimi*; a bare surname, where she says "-kun" to other boys). Natsuki asks Nanoha to call her Natsuki on day one, with him sitting right there, and never asks him |
| Nanoha → Natsuki | "Mizuno-san" → "Natsuki-san" on day one ("I'm working up to it") |
| Natsuki → Nanoha | "Nanoha" from day one, and she never changes it |
| Natsuki → Ryōsuke / Takatsuki / Rika / Akane / Mio | "Tokiwa-kun" / "Takatsuki-kun" / "Rika" / "Akane-chan" / "Mio-chan" |
| Classmates → Natsuki | **"Nacchan"** by her second day (scene outline 2.1), except Kōhei, Ryōsuke and Takatsuki, who use "Mizuno" |
| Akane → Kōhei / Nanoha / Natsuki | "Onii-chan" / "Nanoha-chan" / "Natsuki-san" |
| Kōhei → Akane / Mio / Rika | "Akane" / "Mio" / "Hoshikawa" |
| Nanoha → Rika / Akane / Ryōsuke / Takatsuki | "Rika-chan" / "Akane-chan" / "Tokiwa-kun" / "Takatsuki-kun" |
| Mio → Kōhei / Nanoha / Akane / Natsuki | "Kō-nii" / "Onee-chan" / "Akane-nee" / "Natsuki-nee" |
| Rika → Nanoha / Kōhei / Natsuki / Ryōsuke | "Nano-chan" / "Fujisawa-kun" / "Nacchan" / "Tokiwa-kun" |
| Kōhei ↔ Ryōsuke | "Tokiwa" / "Fujisawa" |
| Ryōsuke → Nanoha / Natsuki / Rika | "Tachibana" / "Mizuno" / "Hoshikawa" |
| Kōhei ↔ Takatsuki | "Takatsuki" / "Fujisawa" (throughout; their change is in tone, not names) |
| Takatsuki → Nanoha / Natsuki | "Tachibana-san" / "Mizuno" |
| Club → Kirishima | "Captain" (*shushō*) at practice; "Kirishima-senpai" off the floor |
| Kirishima → members | Bare surnames |
| Kōhei → Emi / Kazuo / Genji | "Oba-san" / "Oji-san" / "Ojii-san" |
| Emi / Kazuo / Genji → Kōhei | "Kōhei-kun" (as in the shipped pilot scene the author liked) / "Kōhei" / "Kōhei" |
| Emi / Kazuo → Nanoha | "Nanoha" |
| Nanoha → Genji | "Ojii-chan" |
| Kōhei ↔ his mom | "Kaa-san" / "Kōhei" |
| Mom → Nanoha | "Nanoha-chan" |
| Emi → Kōhei's mom | Her given name, as old friends (the name is Open) |
| Ōno-sensei → students | Bare surnames |
| Yuzu → Kōhei / Kōhei → Yuzu | "Senpai" / "Shiina" (she'd like more; he doesn't take the hint) |
| Manager ↔ Kōhei | "Fujisawa-kun" / "Tenchō" (Manager) |
| Chie → Natsuki | "Natsuki" (often in capitals, as in the kept Ch2 texts) |
| Fairy → everyone | Bare given names; at the bloom, to Kōhei and Natsuki: "You two. Again." |

**Childhood flashbacks (FB1–FB6; added Oct 17 [P]):** before middle school Kōhei calls her "Nanoha" (FB1, FB2, FB4, and FB3 if it's set in childhood; its age is Open, canon §6). At the start of middle school he shoots past her and the other boys start teasing him about her, so he drops her given name and "Chibi" takes over (FB5 can show it in passing). His "Nanoha" in Ch25 really is the first time in years. As a child she calls him "Kō-chan" in front of anyone; from middle school it's "Kōhei" in public and "Kō-chan" in private. Child Kōhei says *boku* until middle school, then *ore*; child Nanoha says *watashi*.

**Planned shifts (story beats; placed in the chapter map's running threads):**
1. **Kōhei → Nanoha: "Chibi" → "Nanoha."** Plant "Chibi" early (the Ch1 revision: "Night, Chibi," おやすみ、チビ, answering her "Good night, Kō-chan"; Ch1 already has her "short-person direction" bit). **Ch11** is the nickname that suddenly hurts (scene bank 6): with the dueling lunches and the scorekeeping, he waves it off with something like "Come on. It's Chibi. It's like eating at home," and she hears that he still sees a little kid. **Ch25**, when they start dating, he calls her "Nanoha" to her face, on purpose, for the first time in years, and she notices. After that, "Chibi" when he's teasing, "Nanoha" when he means it (and in Ch39's "I love you"). ("Nano" was considered and dropped: なの is also a sentence ending, so a voiced "Nano" sounds like cutesy speech, not a name.)
2. **Nanoha → Kōhei: one cold "Fujisawa-kun."** In **Ch20**, when she faces him about the kiss, the girl who has called him "Kōhei" and "Kō-chan" all her life calls him "Fujisawa-kun." "Kōhei" comes back by Ch22, and "Kō-chan" by Ch25.
3. **Kōhei ↔ Natsuki: surnames until January.** **Ch14** (summer festival): Rika teases the asymmetry: the whole class calls her Nacchan and she made Nano-chan call her Natsuki on day one, so why is Fujisawa-kun still on "Mizuno"? (Tokiwa-kun doesn't count; he surnames everyone.) Neither of them answers. **Ch19:** her one voiced line in the kiss sequence opens with his name, the first time she says it: "Kōhei… Let me be the one to tell her." **Ch20–30:** she goes back to "Fujisawa" (distance). **Ch31**, at the farewell to their past selves (if that scene is used; canon 21a is a Proposal), she finally asks: "Everyone calls me Natsuki. You too. Mine, not hers." He does, which reads as him joining her friends, not a step toward romance. Given names on both sides from then on, and his narration switches to "Natsuki" too. **Ch32:** Nanoha notices the change.
4. **Nanoha → Natsuki: "-san" → "-chan" → "-san" → bare.** "Natsuki-chan" at the pact (**Ch10**); back to a cool "Natsuki-san" after Natsuki tells her (**Ch20**); "Natsuki-chan" again as the friendship is repaired (**Ch26**); plain "Natsuki" when the girls talk privately in January (**Ch33**). Natsuki says "Nanoha" through all of it.
5. **Akane → Natsuki: "Natsuki-san" → "Natsuki-chan"** in **Ch15**, when she hides her in her room ("I'm Team Nanoha-chan… because I like you too").
6. **Takatsuki's register break:** *boku* and surnames always, except one *omae* in **Ch20**, when he tells Kōhei he'd rather they go to the adviser together ("You scared her. You scared me too.").

## 4a. Manga inserts (color, from Oct 12): workflow
**Which scenes become manga (working rule of thumb):** sequence-dependent beats (sparring, the street fight, the beast, the near-wordless kiss, montages, the full-page Nanoha moment); dialogue stays with sprites; emotional peaks get CGs.

**No storyboard step** (author, Oct 12): Vol. 1 was made from scratch and came out well. Claude builds each insert straight from the script and **presents only finished pages** that have passed the self-review below. The author's review time is the constraint, not cost.

1. **Script** the insert (`production/<insert>/insert-script.md`): pages, panels, shot, dialogue, SFX.
2. **Layout spec** (`insert-spec.json`): panel boxes and balloon positions, decided before generation. `compose.py --name` can render it as a quick layout proof for Claude's own check; the author doesn't review it.
3. **Generate** each panel in color at its box's exact aspect ratio, with the locked references, and **reserve the balloon area in the prompt** ("keep the upper right empty for a speech balloon; no faces there"). Vol. 1's biggest flaw was dialogue covering faces.
4. **Self-review, every panel** (redo until it passes):
   - On model against the references: face, hair, eye color, outfit, swatches, height relationships.
   - Canon and setting: the beast's bone-white mask; kendo panels wear men (no bare faces); props and location consistent within a scene.
   - No baked-in text, watermarks or frame lines; hands and anatomy sound.
5. **Letter and self-review every page:** no balloon covers a face or a key action; reading order right to left is unambiguous; SFX sit inside their panel; text is legible at phone size.
6. **Independent check before delivery:** a separate reviewer agent, which hasn't seen the production, checks the finished pages against the script, canon and references. Fix what it finds.
7. **Deliver** the finished pages with a short note of any known compromises.

**Presentation in the VN (Decided Oct 13, locked as tested; the author said "don't change a thing"):** panel by panel, as built in `production/insert-presentation-test/index.html`. That file is the reference implementation; port it into the VN as is.
- The insert opens on the whole page fitted to the screen (an establishing look), then each tap zooms to the next panel in reading order (right to left, top to bottom).
- The current panel fills the screen with about 4% padding. The rest of the page stays visible around it, dimmed under the night-ink overlay (`rgba(16,19,31,.86)`), with about 24 px of page-space margin so SFX that break the border stay lit.
- Zoom moves are animated (0.55 s ease). Pages cross-fade between each other and into and out of the VN scene.
- Panel boxes come from the insert's `insert-spec.json`, so lettering and the zoom share one source.

**Design every insert for panel-by-panel reading (Oct 13).** Guided view on ordinary comics is clumsy because those pages were drawn for print. Ours are drawn for this view from the start; apply these rules at the script and layout steps (1–2):
- **Every panel stands alone.** Each panel gets its own full screen, so it must read without its neighbors: all its balloons inside its own border (the compositor already clips lettering per panel); no figure, balloon or caption spanning two panels; no inset or overlapping panels. SFX may break the border by a little (inside the 24 px lit margin).
- **One beat per panel, one tap per beat.** The tap is the pacing: a reaction or a pause gets its own panel. Aim for about 4–6 panels per page; more just means more taps.
- **Shape panels for a landscape screen.** Wide panels (21:9 to 4:3) fill the screen; square ones are fine; tall panels (2:3, 9:16) show with big dark side margins, so keep them for real vertical motion (a fall, a downward strike, full-height figures).
- **Surprises go on a new page.** The establishing look and the dimmed neighbors show the whole page before you reach each panel, so a reveal placed mid-page is seen early. Put a reveal at the start of a new page, ideally as a half- or full-page image (which plays as one step).
- **Pages still look like manga** in the establishing view: conventional right-to-left layouts with clear gutters, no layouts that only make sense zoomed.
- **Lettering size:** 38 px balloon text on the 1600 px page reads at about 22 px on a phone in landscape for a full-width panel and larger for smaller panels, so keep the base sizes in §5 and avoid any panel narrower than about a third of the page width with more than a few words.
- **Resolution (to do before the first real insert):** a zoomed panel is shown up to about 2.5× its page-master size on a Retina iPad, so 1600 px masters look soft when zoomed. Compose VN pages at 2× (3200 × 4544) from the 2K panel art; the look and behavior don't change.

**Lessons from the jigeiko test (Oct 12):** state "wearing the men helmet, no bare faces" for every kendo panel; say "absolutely no text" or the model letters SFX itself; kendo bows normally happen with men on; one style anchor and one location plate per scene keep panels consistent.

## 4. Manga art (black and white; legacy Vol. 1)
Moved to `story/archive/style-guide-legacy.md` (Oct 19). Current inserts are full color (§4a).

## 5. Lettering
| Use | Font |
|---|---|
| Dialogue | Kalam Bold |
| Narration | Kalam Regular |
| Impact SFX | Dela Gothic One |
| Titles | Shippori Mincho / Cormorant |

**Base sizes (1600 px page):** say 33, shout 38, small 27, think 31, dream 33, narration 29, free 34.

**Balloons:** drawn by code with 2× supersampling.

**Phone chats:** rendered as a chat UI.

**QA:** an overlap-detection pass plus a gridded proof sheet (`adjust.json`).

**Kendo terms (Oct 12):** the author doesn't know kendo vocabulary, so every kendo call and term appears in Japanese with English. In VN text: the Japanese in the line, the English right after it in a smaller or paler span on first use in a scene (for example, "Men! (Head!)", "Kote ari! (Point: wrist!)", "Hajime! (Begin!)", "Yame! (Stop!)", "Shōbu ari! (Match decided!)"). Natsuki's explainer scene (canon 13f) introduces the core set. In manga inserts, the same pairing in a small caption beside the sound.

**Translator's notes (Oct 19, the author's Ch1 punch list):** the author didn't know some of the Japanese foods, and wanted "a little more information." Any Japanese word an English reader may not know (food, household things, kendo ranks, customs) is written `{term|gloss}` on its first use in a chapter, with a short gloss, and gets a line in the deliverable's `script/notes.txt` (`term | note`). In the game the term is underlined; a tap opens the note without advancing the text, and Settings → Notes lists every note the reader has met (all of them in developer mode). Notes are one or two plain sentences in a translator's voice, explain only the word, never the story, and never sit on a planted clue (so 水 on Natsuki's wrist keeps its gloss and gets no note). Words the line itself explains, honorifics (canon §2) and English food words (miso soup, rice) get nothing. Cold-reader material (`reader_view.py`) shows each note once in brackets.

## 6. Failure modes and fixes
- **"Leave blank space for balloons"** makes the model draw literal blank boxes. Ask instead for "generous open background (wall, sky, trees or soft tone) above and beside the heads; keep faces out of the top fifth," or name the regions to keep simple, then crop.
- **Heads cropped at the top edge:** add "a natural cinematic composition with some background visible around the characters (do not crop heads at the top edge); the illustration must still fill the whole canvas with no blank bands."
- **Stray inner frame lines:** keep "no panel borders or frames" in the prompt and check every panel.
- **Garbled kanji on props:** avoid legible text in the art, or cover it with lettering.
- **Side characters drift** (Takatsuki most): always pass the sprite.
- **Continuity slips in chibi panels:** state the outfit explicitly.
- **The model won't hold specific geometry from text** (Oct 6). Four text-only attempts at the close spacing either kept the alley or produced nonsense, and editing the old background anchored the old layout. **Fix:** draw a simple layout sketch in code (blocking shapes for the walls, the gap and the windows in perspective) and pass it as the structure reference, with the style anchor for rendering.
- **Refs must be pushed before submitting a job** (Oct 10, twice): a raw GitHub URL that isn't on `main` yet fails the job with a 422 (uncharged). Push, check the raw URL returns 200, then submit.
- **Grayscale drift** (Oct 10): NB2 sometimes returns monochrome from color refs. Every prompt says "FULL NATURAL COLOR … absolutely not grayscale".
- **Age drift:** prompts for a 14-year-old came back looking 16–17 (Akane, first pass). Spell out the age cues in §3, and check against `akane-v2/02-sailor-uniform.png`.
- **Concept-art proportions leak in** (long legs): always state "natural realistic proportions for a {height} teen" and name what to correct.
- **Content filter:** if a panel is refused (heavy blood, or teens kissing), reframe with silhouettes, a cropped close-up, implied impact or heavier ink, or try another model. Tell the author rather than quietly watering the scene down.
- **Kiss and closeness images (Oct 13 test, `production/tests/kiss-oct13/`; none refused):** spell out modest clothes (one image drifted to a camisole and short shorts); keep compositions on faces (one framed his lap); match faces tightly to the designs. Video models are still untested for the kiss.
- **QA cost:** review cropped or downscaled previews; open full size only where something looks wrong.

## 7. Audio
**Music:** **ElevenLabs Music v2.5 only from Oct 11 (author's preference).** The pilot tracks were MiniMax Music 3 with ElevenLabs extensions. All eight pilot BGM tracks were prompted instrumental-only and loop with a crossfade (`memory` has a wordless choir pad by design). Both models can also sing: MiniMax takes lyrics, and ElevenLabs drops vocals only with `force_instrumental`.

| Track | Used for | Author review (Oct 11) |
|---|---|---|
| title | Title, finale | **Keep** |
| daily | Everyday scenes | Maybe (59 s loop; extend if kept) |
| nanoha | Nanoha's theme (river walk, shrine) | **Keep** |
| natsuki | Natsuki's theme (intro, bridge) | **Replaced Oct 14** by take G, built from the author's own guitar melody |
| kendo → practice | Dojo, practice, sparring | **Replaced Oct 14** by tribal-percussion take F. Take E saved for intense fight scenes |
| night | Tender nights, the window scenes | **Keep; extend** (43 s loop) |
| memory | Dream and past-life | Maybe |
| comedy | Hoshino Kitchen | **Replace**, in the feel of the Muv-Luv main theme (not needed until Yuzu, Ch8) |
| childhood | Shared-past flashbacks (FB1–FB6) | **New Oct 14:** take A (nylon guitar, toy piano, celesta) |

**Music plan (approved Oct 11; on hold since that evening, kept for reference).** Pilot music was closed Oct 16: the four short loops stay as they are (production log). The Oct 11 (eve) pause is in the log archive.
- **House sound:** piano-led with strings, soft and warm. Every cue keeps piano or a string section at its core (the link between `title`, `nanoha`, `night` and the author's reference, Steins;Gate's "Gate of Steiner"). Each cue changes the mood and adds one color, never the whole band.
- **Colors by story area:** everyday and romance add flute, glockenspiel and light acoustic guitar. Energy cues (Natsuki, practice, comedy) add light live drums and bass, acoustic, no synths. Sad and emotional cues strip back to solo piano and slow strings. The tree and the past life add koto (Japanese zither), shakuhachi (bamboo flute) and a wordless voice. Strangeness, then danger, add Steins;Gate-style electronic textures and pulses, plus Japanese drums for the beast, over the same piano and strings.
- **Vocals:** no lyrics under voiced scenes. Vocal songs only for the opening theme, the kiss and the ending, which may use a different style. (No cutscenes since Oct 12; these play over stills and CGs.)
- **Generation:** ElevenLabs v2.5 and MiniMax Music 3. MiniMax was re-approved Oct 13 because most of the kept pilot tracks (`title`, `daily`, `night`, `memory`) were made with it; `nanoha` is an ElevenLabs build on a MiniMax original. Lyria dropped Oct 11. Style references must stay light: a `nanoha` reference at medium strength made Natsuki's theme sound like Nanoha's. Give each character theme its own lead instrument within the house palette (Nanoha: felt piano with flute and glockenspiel) [P].
- **Finishing:** every track leveled to −19 LUFS, extended to 2–3 minutes, looped with a clean seam.
- **First-chapters cue list:** keep `title`, `nanoha`, `night` (extend). `daily` stays unless a referenced version beats it. New, one cue at a time: Natsuki, comedy, practice (replaces `kendo`), sad, memory. About $2 per cue (two takes).

**Kiss scene candidate (Oct 17):** take B of the author's hummed melody (violin and cello duet), `production/music/kiss-hum/`. Kept in mind, not final.

**Wanted:** an original vocal song for the kiss scene, in the feel of the author's reference (canon §2). The first BGM thread to use vocals.

**SFX:** door_slide, notif, slip, steps.

**Voice:** Japanese, Gemini 3.8 Flash TTS. Narration is unvoiced. **The author picks voices by ear** from audition sheets: the same 2–3 in-character lines per candidate, numbered.

**Oct 10 audition:** every voice not yet approved (20 characters, including the new families, past life, antagonists and the fairy), 3–6 candidates each, on an audition page (artifact "Ōzakura Voice Auditions"; source and clips in `production/voice-auditions/oct10/`, spec in `oct10-spec.py`). Nanoha and Akane also offer a "+2 semitones" post-processed variant; if picked, apply it to every line for that character. The table below updates when the author picks.

| Character | Voice | Direction (style instruction in `production/voice-auditions/oct10-spec.py`) | Status |
|---|---|---|---|
| Kōhei | Puck | calm, grounded, a little tired, dry; let warmth through | OK (author) |
| Nanoha | **Erinome, +2 semitones** | 16; soft, relaxed, deadpan; "anime heroine" youth direction | **Picked Oct 11** |
| Natsuki | **Zephyr, brighter direction, +1 semitone** | young, light, clear; bright, sunny, quietly confident; playful and teasing, a smile in every line (exact instruction in `production/voice-auditions/oct24-natsuki/handoff-production.md`) | **Picked Oct 24** (audition `production/voice-auditions/oct24-natsuki/`, option 6). Was plain Zephyr |
| Natsuki (past life), the dream woman | **Despina** (+ the game's dream echo) | a young Edo-era wife, mid-twenties; warm, gentle, a little lower and slower than a teen; scolding with love | **Picked Oct 18** (audition `production/voice-auditions/oct18-dream/`, candidate 2). Recast from Zephyr so the dream doesn't settle who she is (canon §5) |
| Akane | **Aoede, +2 semitones** | 14; sweet, soft, playful, a little frail | **Picked Oct 11** |
| Kirishima (male) | Charon | calm, low, quiet authority; bone-dry jokes | **Picked Oct 11** |
| Ryōsuke | Achird | precise, a little smug, dry | **Picked Oct 11** |
| Rika | **Laomedeia, +2 semitones** (was +4; the author lowered it Oct 17 after hearing Pilot v2) | genki, loud | **Picked Oct 11** |
| Yuzu | **Autonoe, +2 semitones** | cheeky, sly kōhai | **Picked Oct 11** |
| Mio (was Sōta) | **Kore, +4 semitones** | 7-year-old girl; bossy tiny-princess orders, cheeky, sore loser | **Picked Oct 13** |
| The fairy | **Leda, +4 semitones** | small-girl voice, airy, ancient | **Picked Oct 11** |
| Emi | Achernar | warm, bubbly mother | OK (author, Oct 8) |
| Takatsuki | Fenrir | **precise, reserved, dry** (was "curt, abrasive") | OK (author, Oct 8) |
| Ōno-sensei | Schedar | tired teacher | **Picked Oct 11** |
| Manager | Enceladus | harried, upbeat, kind | **Picked Oct 11** |
| Club adviser | Iapetus | steady, stern but fair | **Picked Oct 11** |
| Kazuo | Charon | big, quiet, few words | **Picked Oct 11** |
| Genji | Algenib | creaky, warm, twinkly | **Picked Oct 11** |
| Kōhei's mom | Sulafat | quiet, fragile, tender | **Picked Oct 11** |
| Kōhei's dad | Umbriel | kind, good-humored | **Picked Oct 11** |
| Rōnin (past life) | Orus | low, calm, gentle | **Picked Oct 11** |
| Her father (past life) | Alnilam | grave, formal, proud | **Picked Oct 11** |
| Thug | Algenib | sneering, rough | **Picked Oct 11** |
| Tournament opponent | Zubenelgenubi | cocky, mocking | **Picked Oct 11** |

**Pitch shift:** "+2 semitones" means every generated line is post-processed with `ffmpeg -af "asetrate=24000*1.1225,aresample=24000,atempo=0.8909"` (raises pitch and formants, keeps timing); "+4" uses 1.2599 / 0.7937; "+1" uses 1.0595 / 0.9439.
**Shared voices:** Charon (Kirishima, Kazuo) and Algenib (Genji, the thug) are each used twice; Leda is the fairy at +4. Those pairs rarely share a scene; if they do, add a slight pitch offset to one of them.

## 8. fal workflow notes
**Pages for the author** (auditions, listening and review pages) go on the public site as plain web pages via GitHub Pages; the artifact player doesn't work for him (Oct 13).

**Uploads:**
1. Call `mcp__fal__upload_file` with `prepare_upload=true` to get a presigned URL.
2. Send `curl -X PUT -H "Content-Type: image/jpeg"` (or the matching type) to that URL.

Raw repo URLs often make uploading unnecessary.

**Approximate unit costs:**
| Endpoint | Cost |
|---|---|
| NB2 edit (1K) | ~$0.08/image |
| NB Pro (VN) | ~$0.15/image |
| NB Pro 2K (manga) | ~$0.15/image |
| bria background removal | ~$0.018/image |
| music | ~$0.25/track |

**Bulk jobs:** use `submit_job` with `check_job`/`get_job_result`, and keep a manifest (name → URL) and a spend ledger.

**Save keepers to the repo** (`production/refs/…`) right away. fal URLs expire and workspaces get wiped.

## 9. Chapter production process (decided Oct 17; applies from Pilot v2 Ch2)
The goal is to spend the author's review time on taste, not on finding errors. In Ch1, the author's first punch list was mostly continuity, wording and staging, and the Oct 17 cold reads found flat dialogue, heavy-handed clues and art/text mismatches that no technical check looks for. Every check below is run by a **fresh agent that hasn't seen the work being made**; self-review alone missed real problems in every Ch1 round. **Standard prompts for every check are in `production/pipeline/review/`** (its README maps them to these steps); the tools are in `production/pipeline/vn/`.

**Match the checks to the size of the change (Oct 19).** The full process below is for new chapters, new engine features and new art sets. Most work after a handover is smaller, and running every check on it costs hours for little gain (Ch1's punch-list round 1 went through four diff-check rounds, the last two on desktop-keyboard and short-phone edge cases).
- **Tiny change** (a typo, a word or two, one line reworded, a single retake, no layout change): the automatic checks only (`script_lint.py`, `qa_play.py`, `voice_levels.py` for retakes). No reviewer agent. Mention it in the next handover note.
- **Punch-list batch** (the usual case after a handover): fix the whole list in one pass, run the automatic checks and the snapshot diff, then **one** independent check at the end, scoped to the batch's diff. Changed Japanese lines get the Japanese pass in the same review.
- **Full process** (steps 1–10): a new chapter, a new engine feature or a new set of CGs.
- **Stop rule for any review:** reviewers sort findings into **must-fix** (something a reader hits in normal play on the target screens, landscape, judged at iPad size; anything off-canon or off-model; anything that loses progress) and **backlog** (edge cases, dev-only paths, hand-edited saves, desktop-keyboard quirks, spot-check sizes). Fix the must-fix items and re-check only those; backlog items go on the status board's carry list for the next engine pass. At most two check rounds per batch unless a must-fix item remains.

1. **Outline (Story thread; the author approves, as now).** A scene list plus the CGs, inserts, living stills and backgrounds needed, **plus a reader-knowledge target**: what the reader should *suspect* and *know* by the end of the chapter (the Ch1 cold reads showed this has to be decided on purpose).
2. **Draft** against canon, the chapter map, pilot-notes and the speech sheets (§3b). Write stable line IDs into the script source so edits never renumber lines.
3. **Writing gates, before any art or voices** (in this order, fixing between steps):
   - **Canon and continuity check** (`review/continuity.md`): heights, dates, names, rules, earlier chapters, the address sheet. It also lists every [P] detail the draft invents.
   - **Lint** (`script_lint.py --chapter N`): tics, Japanese pronouns per §3c, name timing, retired forms. Automatic; it flags, a person or reviewer decides.
   - **Dialogue** (`review/dialogue-diagnosis.md`, `dialogue-rewrite.md`, `overcorrection-check.md`): a diagnosis pass (line-by-line verdicts, a blind voice test), then a rewrite, then an independent overcorrection check that compares before and after. Whole chapter.
   - **Japanese pass** (`review/japanese-pass.md`): the voiced column is checked for natural speech, register, §3c pronouns and address, meaning against the English, and anything a listener could mishear ("Nano" sounded like the なの sentence ending). The author can't read Japanese, so this is the only check it gets.
   - **Three cold readers** (`review/cold-reader.md`; material from `reader_view.py`): casual, manga reader, genre-savvy. **At every checkpoint they give three numbers (canon §5, Oct 18):** who Kōhei ends up with, who they want him to end up with, and who the dream woman is, each with confidence. **Those three are judged over windows of about 3–4 chapters, not per chapter** (single chapters can swing); per checkpoint, only that no reader is sure (70%+). So each round's readers read from Ch1 through the chapter under test, not just the new chapter. They get only what a reader sees, in parts with checkpoints, and report what they infer (compared against the reader-knowledge target afterward), plus flat, confusing or heavy-handed lines and text/art mismatches. Fix here, while changes are free.
4. **Art:** shot list from the final script; a true-height layout sketch (`production/pipeline/vn/cg_layout.py`) for every multi-character CG, planning one edit pass; **an on-model check of every image** (`review/on-model-image.md`) against the locked references *and* the script text around it (hair length, which wrist, who stretches to reach), with proportions measured; every piece logged in the deliverable's `art/prompts.md`.
5. **Voices** as in the Pilot v2 README (transcript-checked cuts), plus `voice_levels.py` (speech level, clipping, too short, mostly silent). Its first run flagged the two dream lines at about 6 dB under the rest; whether that's intended softness is checked by ear.
6. **Build and technical QA:** `qa_play.py` at iPad landscape (1180×820), with spot checks of scene starts at phone landscape and a desktop Chrome window (no portrait; canon §2), plus a **visual snapshot of every line** (`qa_play.py --every`) compared against the last approved build with `snapshot_diff.py`, so reviewers look only at what changed. The baseline is rebuilt from the last approval tag (step 10).
7. **Independent review of the whole build** (`review/build-review.md`). After each fix: a check scoped to the diff, plus the regression run (step 6). Fix rounds introduced new bugs in Ch1, so this is mandatory.
8. **Handover:** a playable link and one short note: the [P] inventions, known compromises and spend. The author plays on his iPad (nothing here can test Safari or listen by ear) and flags only what doesn't work.
9. **Punch-list rounds:** each gets a diff-scoped independent check plus the regression run. **Dialogue and voice items from the author's punch lists also go to the Story thread**, which updates the speech and address sheets (§3b–§3c) so later chapters learn from them.
10. **Approval:** when the author approves a chapter, tag the commit `v2-chN-approved` (for later deliverables, `<deliverable>-chN-approved`) and update the status board. The tag is the regression baseline for any later fix: rebuild its shots with `qa_play.py --every` from that commit; don't commit screenshots.

**Standing rules:**
- **Spending inside an approved cap:** no item-by-item check-ins. Report spend at handover; ask first only if a single item would cost more than about $5 or the total would pass the cap. If Claude tells the author something is "your call," it waits for his answer.
- **[P] details invented in production** go in the handover note and pilot-notes; the author judges them by playing, and the Story thread folds them into canon afterward. No pre-review.
- **Measure, don't eyeball:** proportions and ratios are measured on a pixel grid.
- **Record prompts** for every generated piece, and commit pipeline code as you go.
- **Status board:** update the production log's status board (§0) at the end of every work session.
- **Handoffs:** write them as a file in the deliverable's folder; once the receiving thread has acted on one, move it to that folder's `archive/` so no one mistakes it for current instructions.
- **Reference test:** `production/tests/oct17-dialogue-coldread/` (the first cold reads and dialogue pass, with the materials to rerun them).
