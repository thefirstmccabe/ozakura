# Ōzakura repo: working rules

This repo is the durable store for everything Ōzakura: game build, art, audio, references, pipeline code, production outputs, **and the story docs**.

The repo is **public**, and GitHub Pages serves it at https://thefirstmccabe.github.io/ozakura/. The author decided on Oct 10 that the story docs can be public too. Still never commit credentials or anything personal.

## Story docs: `story/` (mirrored to the claude.ai Project)
The four living docs exist in two places: `story/` here (with git history) and the claude.ai Project "visual novel" under `ozakura/` (where the author reads them).
- `story/canon.md` — the single story bible. It governs over everything else in this repo.
- `story/pilot-notes.md` — the shipped pilot's inventions and the agreed fix list.
- `story/style-guide.md` — designs, references, prompts, lettering, voices.
- `story/production-log.md` — decisions, budget, issues, next steps.

**How to edit them (every thread):**
1. `git fetch origin main` and rebase, so you start from the latest commit.
2. Edit the file in `story/` with normal file edits; never retype a whole doc.
3. Commit and push.
4. Upload the same file to the Project: `project_write` with `path: ozakura/<name>.md` and `local_path: story/<name>.md`.

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
- Commit at checkpoints, not only at the end. Keep large intermediate renders out unless they're needed to rebuild.
- Before pushing, run `git fetch origin main` and rebase. The clone is shallow.
- Raw URLs (`https://raw.githubusercontent.com/thefirstmccabe/ozakura/main/...`) work directly as fal `image_urls`.
