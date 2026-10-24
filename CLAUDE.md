# Ōzakura repo: working rules

This repo is the durable store for everything Ōzakura: game build, art, audio, references, pipeline code, production outputs, **and the story docs**.

The repo is **public**, and GitHub Pages serves it at https://thefirstmccabe.github.io/ozakura/. The author decided on Oct 10 that the story docs can be public too. Still never commit credentials or anything personal.

## Start here (every thread)
1. **Read this file and the status board** (`story/production-log.md` §0). The board says what's in flight and who owns it.
2. **Then read only what your job needs** (the docs are long; don't read everything every time):
   - **Story thread:** `story/canon.md`, `story/chapter-map.md`, style guide §3b–§3c (speech and address) and §9 step 1 (what an outline contains), `story/pilot-notes.md` (the [P] details to fold in), the deliverable's `scene-outline.md`, and the latest handover note.
   - **Production thread:** the deliverable's brief (`production/<deliverable>/README.md`) and outline, `story/chapter-map.md` (the chapter's row, running threads and reader windows), style guide §1–§9 (§9 is the process), `story/pilot-notes.md`, the decision-log rows since your last session, and the canon sections the chapter touches.
   - **Audio thread** (music, voices, SFX): style guide §7 and the music cue list for the deliverable.
   - **Planning:** the production log and style guide §9.
3. Before changing a doc, read the section you're changing in full. `story/archive/` is history, not required reading.

## Threads and who owns what
| Thread | Owns (decides and edits) | Hands off to |
|---|---|---|
| **Story** | `canon.md`, `canon-revisions.md`, `chapter-map.md`; **drafts chapter outlines and reader-knowledge targets before production** (the author approves them; they live in `production/<deliverable>/scene-outline.md`, which Story owns); the speech and address sheets (style guide §3b–§3c); folding [P] details into canon | Production (outlines), via a handoff file in the deliverable's folder |
| **Production** (one per deliverable) | Builds, scripts, art, voices; `production/<deliverable>/` (except the outline) and `production/pipeline/` (except `review/`); style guide §1–§6 and §8; re-voicing builds with the §7 cast (the Audio thread picks the cast); `pilot-notes.md` [P] entries; the status board's rows for its chapters | Story (punch-list dialogue items, [P] details), the author (handovers) |
| **Audio** (was Music; widened Oct 24) | All of style guide §7: music, the voice cast and voice auditions, SFX; `production/music/`, `production/voice-auditions/`, the deliverable's `music-cues.md` | Production (finished cues; recast decisions to re-voice in the build) |
| **Design pass** (only when a big visual job comes up: a style homage, a batch of new characters or locations; small one-offs stay in whichever thread the author raises them) | Its exploration in `production/design/<pass>/`; the approved results go into style guide §1–§2. Starts from a short brief and closes when the author approves | Production (approved designs and references) |
| **Planning** | Style guide §9 (the process), `production/pipeline/review/` prompts, the log's structure. A standing thread (it doesn't retire after Pilot v2) | Everyone (process changes) |

Any thread may append to the decision log and update the status board. If a change belongs to another thread, write it down for that thread (a handoff file or a log row) instead of making it.

## What a thread decides itself, and what it asks the author
- **Decide, then tell him in a few lines and log it:** wording and clue calibration within the approved reader targets; speech, address and pronoun details; production logistics and [P] details (judged by playing); tool and pipeline choices; anything inside an approved spending cap (ask only for a single item over about $5 or if the total would pass the cap).
- **Ask him first:** plot beats, character arcs and relationships, endings, anything canon marks Open at the story level, new spending, and blocked access.
- **If unsure which side something is on, decide it, tell him plainly, and make it easy to reverse.** Record such a call as [P] or Working, never as Decided in canon, and never settle something canon marks Open.

## Story docs: `story/` (mirrored to the claude.ai Project)
The living docs exist in two places: `story/` here (with git history) and the claude.ai Project "visual novel" under `ozakura/` (where the author reads them).
- `story/canon.md` — the single story bible. It governs over everything else in this repo.
- `story/pilot-notes.md` — the shipped pilot's inventions and the agreed fix list.
- `story/style-guide.md` — designs, references, prompts, lettering, voices.
- `story/production-log.md` — the status board, recent decisions, the open budget, issues.
- `story/chapter-map.md` — the chapter-by-chapter plan (reworked Oct 18). Canon governs it.
- `story/canon-revisions.md` — canon's revision record (append-only; not required reading).

**How to edit them (every thread):**
1. `git fetch origin main` and rebase, so you start from the latest commit.
2. Edit the file in `story/` with normal file edits; never retype a whole doc.
3. Commit and push.
4. Upload the same file to the Project: `project_write` with `path: ozakura/<name>.md` and `local_path: story/<name>.md`.

`story/archive/` holds history (the log through Oct 14, legacy style-guide sections). It isn't mirrored to the Project.

If someone edited the Project copy directly, `project_read` it first and fold that change into `story/` before editing.

## Layout
- `index.html`, `script.json`, `voice/`, `audio/`, `img/`: the shipped VN pilot. `img/ch` holds sprites, `img/bg` backgrounds and CGs, `img/th` thumbnails.
- `manga/`: the manga reader, `p/` page JPGs, and the Vol. 1 PDF.
- `production/refs/handoff/`: the author's concept references (Oct 5). They outrank the older art, but don't copy their elongated proportions.
- `production/refs/vn-original/`: the ChatGPT lineup and style anchor used for the VN.
- `production/refs/akane-v2/`, `production/refs/natsuki-v2/`: approved redesign references (Oct 6). They outrank the shipped sprites for those characters.
- `production/pipeline/`: generation, lettering and layout code. **Commit pipeline code and panel manifests here as you work.** Session workspaces get wiped.
- `production/<deliverable>/`: per-deliverable sources (scripts, manifests, editable lettering, masters).

## Habits
- **Chapter production follows `story/style-guide.md` §9** (writing gates before art, fresh-agent checks, cold readers, a Japanese pass, regression runs, handover note), using the reviewer prompts in `production/pipeline/review/` and the tools in `production/pipeline/vn/`. Dialogue follows the speech sheets and address sheet in §3b–§3c.
- **Landscape only** (canon §2): the iPad is the primary target, phones and desktop Chrome are supported, and there's no portrait layout on any device (a rotate-your-device screen instead). Don't build or test for portrait.
- **Imperial units only** (feet and inches) in docs, art notes, lineups and prompts. The author doesn't want metric anywhere.
- Commit at checkpoints, not only at the end. Keep large intermediate renders out unless they're needed to rebuild.
- Before pushing, run `git fetch origin main` and rebase. The clone is shallow.
- Raw URLs (`https://raw.githubusercontent.com/thefirstmccabe/ozakura/main/...`) work directly as fal `image_urls`.
