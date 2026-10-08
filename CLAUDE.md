# Ōzakura repo: working rules

This repo is the durable store for all Ōzakura **files**: game build, art, audio, references, pipeline code and production outputs. Text canon lives in the claude.ai Project "visual novel" under `ozakura/`: `canon.md` (the single story bible), `pilot-notes.md`, `style-guide.md` and `production-log.md`. Read those first; they govern over anything here.

The repo is **public**, and GitHub Pages serves it at https://thefirstmccabe.github.io/ozakura/. Do not commit story-bible text, plot spoilers, credentials or anything personal.

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
