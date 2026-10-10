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
   - **Natsuki:** `production/refs/natsuki-v2/01-restyle-uniform.png` **locks the direction.** Her hair should end at the shoulders (it runs slightly long in this image), and her legs are still a bit long for 160 cm.
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

## 2. Character visual sheet
| Character | Hair | Eyes / face | Height | Outfits | B&W rendering |
|---|---|---|---|---|---|
| Kōhei | **Dark brown**, somewhat unruly, uneven fringe leaving the eyes visible. Black or spiky hair is drift | Brown, expressive; youthful, handsome; warm, easy smiles, no permanent scowl | **175 cm** | Navy blazer (gold buttons, open), white shirt, burgundy striped tie loosened, charcoal trousers. Kendo: navy keikogi and hakama. Work: white shirt, dark waist apron | Solid black with white highlights |
| Nanoha | Natural dark brown, below the shoulder blades when down. **School/outings:** loose side braid. **Home:** long and loose. **Bed:** loose bun on *top* of her head with a BIG SOFT scrunchie | Brown eyes, soft oval face; deadpan is her key expression | Petite, about 150 cm; head reaches Kōhei's chin | Navy blazer, white shirt, burgundy ribbon, **charcoal plaid pleated skirt**, dark socks, brown loafers. Pale-blue pajamas with a small cat detail | Dark tone (nearly black), glossy highlights |
| Natsuki | Bright burnished copper. **Shoulder-length** layered cut, side-swept fringe, **styled soft and neat** (tucked behind an ear, glossy, not tousled). **Athletics:** short ponytail | Amber-brown with expressive brows; **warm, quietly confident, slightly knowing smile**; poised posture. Not a tomboy grin | **160 cm**, athletic; exact build Open | Same uniform as Nanoha, worn neatly. Kendo: faded, much-washed indigo keikogi. Casual: put-together and fashionable but **age-appropriate** (short cardigan, casual skirt or jeans, sneakers), camera on a strap. Athletic: navy track shirt and dark sweats | Medium-gray tone, clearly lighter than the dark-haired cast, bright highlights |
| Akane | **Pale lavender-silver**, soft and wispy, shoulder length, small side clip | **Gray-violet**, big and soft; round, soft face with fuller cheeks; slightly pale with a faint blush; sweet expressions. Clearly younger than the high-schoolers | Small and slight, compact (about 14) | **School:** sailor uniform (navy collar with white stripes, white body, red scarf, navy pleated skirt below the knee, white socks, loafers; plush-rabbit bag charm). **Home:** cute and youthful (cream cardigan, pink bunny-ear hoodie, lavender lounge pants, fuzzy socks). Room full of plushies | Light tone (pale hair) with soft highlights |
| Past-life Natsuki | Copper, tied back with a plain cord | **Face hidden in the manga** | — | **A real kimono, simple and everyday**, as worn by a modestly propertied family. Not elaborate, not peasant work clothes | Medium-gray tone |
| Rika | Black, two low pigtails, novelty clips (strawberry, star, frog with a crown) | Big and expressive | — | Uniform with a cream cardigan under the blazer | — |
| Ryōsuke | Neat black | Rectangular glasses; composed, smug | — | Uniform, striped tie | — |
| Yuzu | Light honey-brown, shoulder length, red clip | Cheeky grin | — | White blouse with name badge, burgundy waist apron, black skirt | — |
| Kirishima | Sleek black, low ponytail | Calm, unreadable | — | White keikogi, navy hakama | — |
| Takatsuki | Swept-back black | Sharp; **precise and composed, not sneering** (redesign) | — | Navy keikogi and hakama | — (prone to drift; always pass his sprite) |
| Emi | Dark hair, low bun | Warm | — | Light-blue shirt, mustard-yellow apron | — |
| Sōta | Messy dark hair, bandage on his cheek | Gap-toothed grin | Age 7 | Green dinosaur T-shirt, navy shorts, game controller | — |
| Ōno-sensei | Slightly messy | Droopy and tired; 40s, tall and thin | — | Knit cardigan over shirt and tie | — |

**High-school uniform** (proposed, not a settled school identity; no invented insignia): navy blazer with gold buttons, white shirt, burgundy ribbon or tie, charcoal **plaid** pleated skirt (trousers for boys), dark socks, brown loafers.

**The two houses:**
- Built almost touching, **about a meter between the walls**. Upstairs bedroom windows face each other within arm's reach (Muv-Luv Extra). No alley or stairs between them.
- The current `bg_street_houses` and `cg_window_night` are wrong; see pilot-notes fix 18.
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
- **The model won't hold specific geometry from text** (Oct 6). Four attempts at "houses about a meter apart" either kept the alley or produced nonsense, and editing the old background anchored the old layout. **Fix:** draw a simple layout sketch in code (blocking shapes for the walls, the gap and the windows in perspective) and pass it as the structure reference, with the style anchor for rendering.
- **Age drift:** prompts for a 14-year-old came back looking 16–17 (Akane, first pass). Spell out the age cues in §3, and check against `akane-v2/02-sailor-uniform.png`.
- **Concept-art proportions leak in** (long legs): always state "natural realistic proportions for a {height} teen" and name what to correct.
- **Content filter:** if a panel is refused (heavy blood, or teens kissing), reframe with silhouettes, a cropped close-up, implied impact or heavier ink, or try another model. Tell the author rather than quietly watering the scene down.
- **QA cost:** review cropped or downscaled previews; open full size only where something looks wrong.

## 7. Audio
**Music:** MiniMax Music 3, with extensions from ElevenLabs Music v2.5. All instrumental, looping with a crossfade.

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

**Wanted:** a specific song for the kiss scene. The title is unverified and the rights are unresolved (canon §2).

**SFX:** door_slide, notif, slip, steps.

**Voice:** Japanese, Gemini 3.8 Flash TTS. Narration is unvoiced. **The author picks voices by ear** from audition sheets: the same 2–3 in-character lines per candidate, numbered.

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
| Emi | Achernar | warm, bubbly mother | Not reviewed |
| Ryōsuke | Achird | precise, smug | Not reviewed |
| Takatsuki | Fenrir | **precise, reserved, dry** (was "curt, abrasive") | Re-check after the redesign |
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
