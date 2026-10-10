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
   - **Natsuki:** `production/refs/natsuki-v2/01-restyle-uniform.png` **locks the direction.** Her hair should end at the shoulders (it runs slightly long in this image), and her legs are still a bit long for 5′3″.
     - `02-restyle-casual.png`: the styling idea only. **Do not use** its outfit, which reads as a twenty-something.
3. **The author's concept references** (`production/refs/handoff/`):
   - **Nanoha:**
     - `Nanoha-School-Braid.png` is the primary face and uniform reference.
     - `Nanoha-School-Loose.png` shows her hair down at home.
     - `Nanoha-Pajamas-Bun.png` shows the top bun. Make the scrunchie puffier.
   - **Natsuki:** `Natsuki-Options.png` (center option B only, for face and color) and `Natsuki-Athletics-Ponytail.png` (the athletic look).
   - **Rule:** these are concept art. **Never copy their elongated legs and torsos.**
4. **The ChatGPT lineup and style anchor** (`production/refs/vn-original/`), especially for Kōhei, who has no approved image.
5. **The shipped VN sprites** (`img/ch/*.webp`): the model sheet for the supporting cast only. For the leads they're superseded where canon differs. Akane's are entirely superseded.

**Raw repo URLs work directly as `image_urls`:** `https://raw.githubusercontent.com/thefirstmccabe/ozakura/main/<path>`

**Design rules:**
- **Proportions:** natural, compact and age-appropriate.
- **Appeal:** comes from personality, expression, styling and presence. **Never design or frame the school-age cast for figure or sex appeal.**
- **Hair color:** a medium convention, never commented on in-world.

## 1a. Design lock, Oct 10 (humans APPROVED by the author; the beast is approved for scale, with an ethereal tweak pending)
All files are in `production/refs/design-oct10/`. They outrank every older image for these characters.

| Who | Reference | Notes |
|---|---|---|
| Kōhei | `r3/kohei-short-A.png` | Shorter, slightly unruly dark-brown hair, fringe above the brows, warm. |
| Kōhei face set | `r4/faces/01–10` | Warm smile, neutral, grin, deadpan, surprised, flustered, annoyed, serious, the stillness (shadow over the eyes), sad. Used for his face window on every spoken line. |
| Akane | `r3/akane-teen-uniform.png`, `r3/akane-teen-home.png` | Teen proportions. **Method:** the pilot sprite `img/ch/akane_home_smile.webp` is the face, age and proportion anchor, with lavender-silver hair and a sweet expression on top. Earlier `akane-v2` images read too young; use them only for hair color. |
| Akane with Kōhei | `r4/akane-kohei-height-2.png` | Scale check: her head reaches about his shoulder, and her head is smaller than his. |
| Natsuki casual | `natsuki-casual-A.png` (main), `natsuki-casual-B.png` | Hair runs slightly past the shoulders in both; correct to shoulder length in the sprites. School look: `natsuki-v2/01-restyle-uniform.png`. |
| Kirishima (male) | `r3/kirishima-masc-A.png` | Crew cut, square jaw, broad shoulders, deadpan. Replaces the female sprite set. |
| Fairy | `r3/fairy-shoulder.png`, `r3/fairy-desk.png` | **Scale method:** always show her next to a person or a known object (shoulder, pencil, mug); alone, the model draws her full-size. Rounded ears, no wings, petal robes. |
| Beast | `inventory/beast-size-reference-v2.png` (**current, Oct 10**), `inventory/beast-ethereal-town.png` | **Size rule (raised Oct 10):** back at a man's belt line (about 3′4″ at the shoulder), ear tips at his chest (about 4′3″). A really big dog, not a giant. The model gets size wrong; pass `beast-size-reference-v2.png` as image 1 in every beast prompt, and fix in post if needed. The older `r4/beast-size-reference.png` is superseded. `beast-scene-past-2.png` is a mood concept only; the wolf is still too large. |

**Draft color swatches** (sampled from the references above; verify in the sprite pass):
| Character | Hair | Skin | Eyes | Key colors |
|---|---|---|---|---|
| Kōhei | #3d3232 (highlight #5b4747) | #efccbb | warm brown | blazer #3f4050, tie burgundy |
| Nanoha | #51423d (highlight #6d615e) | #eddace | brown | same uniform; ribbon burgundy |
| Natsuki | #b55e36 (shadow #6c3c2f) | #f5dbca | amber-brown | same uniform |
| Akane | #d0c2d5 (shadow #a89cb0) | #f7ebe6 | gray-violet | sailor navy #454c64, scarf red, cardigan cream #f1e6d4 |
| Kirishima | #08080a | #d7c1b4 | dark | keikogi #e5ded8, hakama #242632 |
| Fairy | #252330 | pale | dark | robes pale pink and white, faint warm glow |
| Beast | fur #1f1f21 (light #565452) | — | glowing gold | mask #d2cbbe, mist #aca59a |

## 1b. Visual inventory, Oct 10 (self-reviewed by Claude; awaiting the author's review)
Everything is in `production/refs/`. Review boards are listed in the production log. **[P]** marks a choice Claude made that the author hasn't confirmed.

**Scale lineups** (`lineup/lineup-1-school.png`, `lineup/lineup-2-family-past.png`): composited in code from the full-body references, bottom-aligned on a 6-inch grid (code: `production/pipeline/layout/lineup.py`). **Units: imperial only** (author's rule, Oct 10). Heights: Kōhei 5′9″, Nanoha 4′11″, Natsuki 5′3″ and Akane 5′0″ are set; all others are **[P]**: Ryōsuke 5′7″, Rika 5′1″, Takatsuki 5′8″, Kirishima 5′11″, Yuzu 5′1″, Ōno 6′0″, adviser 5′6″, manager 5′5″, Kazuo 6′0″, Emi 5′2″, Sōta 4′0″, Genji 5′2″ (stooped), Kōhei's mom 5′2″, his dad 5′8″, the rōnin 5′9″, past Natsuki 5′2″, her father 5′5″, thug 5′10″, tournament opponent 5′8″. Beast: 4′3″ to the ear tips.

| Group | Files (`inventory/` unless noted) | Notes |
|---|---|---|
| Nanoha's family | `kazuo-B.png` (**chosen Oct 10**), `kazuo-A.png` (alternate), `full-emi.png`, `full-sota.png`, `genji.png` | Kazuo B is the off-duty mentor (training mitts); A is the work look. |
| Kōhei's parents | `kohei-mom-grief.png`, `kohei-mom-recover.png`, `kohei-dad-healthy.png`, `kohei-dad-ill.png` | Mom's two states track her recovery arc. Dad appears only in flashbacks. |
| School adults | `adviser.png`, `full-ono.png`, `full-manager.png` | |
| Supporting cast, full body | `full-kohei`, `full-nanoha`, `full-akane`, `full-kirishima`, `full-takatsuki`, `full-ryosuke`, `full-rika`, `full-yuzu` | Natsuki's full-body reference stays `natsuki-v2/01-restyle-uniform.png`. |
| Past life | `ronin-B.png` (chosen; **wears two swords**, katana and wakizashi, Oct 10), `ronin-A.png`, `past-natsuki-B.png` (outing: shawl, green kimono), `past-natsuki-A.png` (everyday), `past-father.png` | |
| One-scene antagonists | `thug.png`, `opponent.png` | Opponent: **bleached-blonde hair** (author, Oct 10). Thug: black undercut [P], changed from blonde so the opponent's hair stays distinctive. |
| Seasonal outfits | `out-{kohei,nanoha,natsuki,akane}-{summer,yukata,winter}.png` | Natsuki's hair runs long in these; keep it shoulder-length in sprites (§2). |
| Kendo armor | `bogu-kohei.png`, `bogu-natsuki.png`, `bogu-takatsuki.png` | |
| Fairy seasons | `fairy-summer.png`, `fairy-autumn.png`, `fairy-winter.png`, `fairy-bloom.png` | Each shown over a hand for scale (§1a method). |
| Beast, ethereal tweak | `beast-size-reference-v2.png`, `beast-ethereal-town.png` | **Approved Oct 10.** Ink-black fur with a faint shifting multicolor sheen, at the raised size (§1a). `beast-ethereal-size.png` shows the old, smaller scale; don't use it for size. |
| Turnarounds (animation) | `turnarounds/{kohei,nanoha,natsuki,akane,ronin,past-natsuki,beast,fairy}.png` | Front, side, back at one scale; the beast sheet adds mask and paw details. Known nit: Akane's bag is on the wrong side in her side view. The rōnin sheet shows both swords. |
| Locations | `locations/houses-street.png`, `window-night-from-kohei.png`, `window-day-from-nanoha.png`, `nanoha-room-day.png` | The houses about three feet apart with no path between them, and the facing windows both ways (fixes 18 and 31). Built from layout sketches in `locations/sketches/` (code: `production/pipeline/layout/house_sketches.py`). |
| The Great Cherry | `locations/tree-{summer,autumn,winter}.png`, `tree-newyear-bloom.png` | Season edits of `img/bg/bg_shrine_tree_day.webp` (the spring view), so the site stays identical. New Year: snow, out-of-season bloom, lanterns. |
| Past era | `locations/past-tree-site.png`, `past-tree-bloom.png`, `past-mist-path.png`, `past-village.png` | Same tree and boulder, no shrine buildings, shimenawa and a stone marker, thatched village below. **Winter** (canon §5, Oct 10): light snow, frost and mist, so the bloom plate shows blossoms falling on snow. The village is an autumn establishing shot. |

**Known issue for the final sprite pass:** Nanoha's skin renders too pale or gray in some images (lineup, turnaround). Check every Nanoha sprite against her skin swatch (§1a); the author doesn't need these redone now.

**Not made yet (per chapter, when needed):** ordinary backgrounds, event CGs, the old grave or memorial (canon: Open), the Tachibana and Fujisawa interiors beyond what's shipped, the town map.

## 2. Character visual sheet
| Character | Hair | Eyes / face | Height | Outfits | B&W rendering |
|---|---|---|---|---|---|
| Kōhei | **Dark brown**, somewhat unruly, uneven fringe leaving the eyes visible. Black or spiky hair is drift | Brown, expressive; youthful, handsome; warm, easy smiles, no permanent scowl | **5′9″** | Navy blazer (gold buttons, open), white shirt, burgundy striped tie loosened, charcoal trousers. Kendo: navy keikogi and hakama. Work: white shirt, dark waist apron | Solid black with white highlights |
| Nanoha | Natural dark brown, below the shoulder blades when down. **School/outings:** loose side braid. **Home:** long and loose. **Bed:** loose bun on *top* of her head with a BIG SOFT scrunchie | Brown eyes, soft oval face; deadpan is her key expression | Petite, about 4′11″; head reaches Kōhei's chin | Navy blazer, white shirt, burgundy ribbon, **charcoal plaid pleated skirt**, dark socks, brown loafers. Pale-blue pajamas with a small cat detail | Dark tone (nearly black), glossy highlights |
| Natsuki | Bright burnished copper. **Shoulder-length** layered cut, side-swept fringe, **styled soft and neat** (tucked behind an ear, glossy, not tousled). **Athletics:** short ponytail | Amber-brown with expressive brows; **warm, quietly confident, slightly knowing smile**; poised posture. Not a tomboy grin | **5′3″**, athletic; exact build Open | Same uniform as Nanoha, worn neatly. Kendo: faded, much-washed indigo keikogi. Casual: put-together and fashionable but **age-appropriate** (short cardigan, casual skirt or jeans, sneakers), camera on a strap. Athletic: navy track shirt and dark sweats | Medium-gray tone, clearly lighter than the dark-haired cast, bright highlights |
| Akane | **Pale lavender-silver**, soft and wispy, shoulder length, small side clip | **Gray-violet**, big and soft; round, soft face with fuller cheeks; slightly pale with a faint blush; sweet expressions. Clearly younger than the high-schoolers | Small and slight, compact (about 14) | **School:** sailor uniform (navy collar with white stripes, white body, red scarf, navy pleated skirt below the knee, white socks, loafers; plush-rabbit bag charm). **Home:** cute and youthful (cream cardigan, pink bunny-ear hoodie, lavender lounge pants, fuzzy socks). Room full of plushies | Light tone (pale hair) with soft highlights |
| Past-life Natsuki | Copper, tied back with a plain cord | **Face hidden in the manga** | — | **A real kimono, simple and everyday**, as worn by a modestly propertied family. Not elaborate, not peasant work clothes | Medium-gray tone |
| Rika | Black, two low pigtails, novelty clips (strawberry, star, frog with a crown) | Big and expressive | — | Uniform with a cream cardigan under the blazer | — |
| Ryōsuke | Neat black | Rectangular glasses; composed, smug | — | Uniform, striped tie | — |
| Yuzu | Light honey-brown, shoulder length, red clip | Cheeky grin | — | White blouse with name badge, burgundy waist apron, black skirt | — |
| Kirishima | **Male (Oct 10):** black crew cut, square jaw, broad shoulders | Calm, unreadable, deadpan | 5′11″ [P] | White keikogi, navy hakama | — |
| Takatsuki | Swept-back, **deep slate blue** (blue-black with steel-blue highlights) [P], Oct 10, for readability against the dark-haired cast | Sharp; **precise and composed, not sneering** (redesign) | — | Navy keikogi and hakama | — (prone to drift; always pass his sprite) |
| Emi | Dark hair, low bun | Warm | — | Light-blue shirt, mustard-yellow apron | — |
| Sōta | Messy dark hair, bandage on his cheek | Gap-toothed grin | Age 7 | Green dinosaur T-shirt, navy shorts, game controller | — |
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
- **Age cue for Akane:** "clearly younger than a high-schooler; compact proportions with a slightly larger head relative to the body; rounder, softer face with fuller cheeks; larger eyes."

**Backgrounds and CGs:** `fal-ai/nano-banana-pro/edit` (higher fidelity), 16:9. Pass the relevant sprites and the style anchor for CGs.

**Current inventory:** 72 sprites (14 outfit sets), 16 backgrounds, 9 CGs (title, hands and strap, Natsuki intro, jigeiko, the catch, Yuzu at the counter, window night, shrine meeting, past life).

## 3a. VN presentation: face windows and dialogue colors (locked Oct 10)
**Face windows** (bottom left, beside the text box, Baldr Sky style). A face window stands in for a sprite that isn't on screen.
1. **Kōhei: a window on every spoken line,** with the expression matching the line. He's the POV and never on stage. Narration and inner thoughts get no window.
2. **Everyone else: a window only when they speak and their sprite isn't on screen** (offscreen voice, next room, behind him, a crowded scene, or a CG that doesn't show them). If the sprite is on stage, no window.
3. **Interludes:** the same rule. If Kōhei appears in an interlude, he's on stage like anyone else.
4. **Never:** phone texts (chat UI), speakers with no sprite (Ōno-sensei, the manager), "???", or past-life scenes (her face stays hidden).

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

## 4. Manga art (black and white)
**Engine:** `fal-ai/nano-banana-pro/edit` at `resolution: '2K'`. Pro gave real screentone; NB2 gave a gray wash. Use `fal-ai/nano-banana-pro` (no `/edit`) for panels with no characters.

**Base prompt (verbatim, prepended to every panel):**
> Draw a single panel for a black-and-white Japanese manga, at the quality of a professionally published romance/drama tankōbon. Clean, confident G-pen inking with varied line weight; screentone shading (dot tones and gradient tones); spotted solid blacks for contrast; white highlights in hair; backgrounds drawn with fine ruled lines in correct perspective. Strictly black ink, white paper and gray screentone — absolutely no color. Anatomically correct hands and faces; expressive manga acting. No text of any kind: no speech bubbles, no captions, no sound-effect lettering, no signature, no watermark, no panel borders or frames. The art fills the entire image edge to edge.

**Then the prompt structure:**
- `Characters:` one line per character: descriptor; wearing {outfit}; {B&W rendering}; "(match the face, hairstyle and proportions in Image N)".
- `Setting:` the location + "Image N shows this location — keep its architecture and props consistent, redrawn in black-and-white manga ink with screentone."
- `Scene:` the acting.
- `Framing:` see §6.

**References per panel:** the character sprites plus a background crop, ordered to match "Image N."

**Page geometry:**
- **Page:** B6 tankōbon, page master 1600×2272 px.
- **Panel aspect ratio:** computed from the layout, then snapped to an accepted ratio: 21:9, 16:9, 3:2, 4:3, 5:4, 1:1, 4:5, 3:4, 2:3, 9:16.

**Color pages:** used sparingly at chapter openers and key beats. Dream pages are in color.

**Reading order:** right to left; the reader defaults to single page.

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
- **QA cost:** review cropped or downscaled previews; open full size only where something looks wrong.

## 7. Audio
**Music:** MiniMax Music 3, with extensions from ElevenLabs Music v2.5. All eight pilot BGM tracks were prompted instrumental-only and loop with a crossfade (`memory` has a wordless choir pad by design). Both models can also sing: MiniMax takes lyrics, and ElevenLabs drops vocals only with `force_instrumental`.

| Track | Used for |
|---|---|
| title | Title, finale |
| daily | Everyday scenes |
| nanoha | Nanoha's theme (river walk, shrine) |
| natsuki | Natsuki's theme (intro, bridge) |
| kendo | Dojo |
| night | Night scenes, interludes |
| memory | Dream and past-life |
| comedy | Hoshino Kitchen |

**Wanted:** an original vocal song for the kiss scene, in the feel of the author's reference (canon §2). The first BGM thread to use vocals.

**SFX:** door_slide, notif, slip, steps.

**Voice:** Japanese, Gemini 3.8 Flash TTS. Narration is unvoiced. **The author picks voices by ear** from audition sheets: the same 2–3 in-character lines per candidate, numbered.

**Oct 10 audition:** every voice not yet approved (20 characters, including the new families, past life, antagonists and the fairy), 3–6 candidates each, on an audition page (artifact "Ōzakura Voice Auditions"; source and clips in `production/voice-auditions/oct10/`, spec in `oct10-spec.py`). Nanoha and Akane also offer a "+2 semitones" post-processed variant; if picked, apply it to every line for that character. The table below updates when the author picks.

| Character | Voice | Direction | Status |
|---|---|---|---|
| Kōhei | Puck | calm, grounded, a little tired, dry; let warmth through | OK (author) |
| Nanoha | ~~Vindemiatrix~~ | soft, relaxed, deadpan; **must sound 16** | **Re-cast:** sounded much older |
| Natsuki | Zephyr | bright, warm, confident (no longer "tomboyish") | OK (author) |
| Past-life Natsuki | Zephyr + echo | softer, warmer, dream | — |
| Akane | ~~Leda~~ | **sweet, soft, a little playful; must sound 14** | **Re-cast:** sounded much older |
| Yuzu | Autonoe | cheeky, sly kōhai | Not reviewed |
| Rika | Laomedeia | genki, loud | Not reviewed |
| Kirishima | Despina | cool, quiet authority | Not reviewed |
| Sōta | Aoede | 7-year-old boy | Not reviewed |
| Emi | Achernar | warm, bubbly mother | OK (author, Oct 8) |
| Ryōsuke | Achird | precise, smug | Not reviewed |
| Takatsuki | Fenrir | **precise, reserved, dry** (was "curt, abrasive") | OK (author, Oct 8) |
| Ōno-sensei | Schedar | tired teacher | Not reviewed |
| Manager | Sadachbia | upbeat, harried | Not reviewed |

## 8. fal workflow notes
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
