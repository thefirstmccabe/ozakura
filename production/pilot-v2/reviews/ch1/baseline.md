# Ch1 regression baseline (§9 step 6)

- **Baseline build:** `v2/` as of commit c487bdf (the Oct 17 build the author played). Its `script.json` is copied here as `baseline-script.json`.
- **Shots:** `qa_play.py http://127.0.0.1:8765/ <dir> --size 1180x820 --every` against that build. The Oct 18 run: 275 shots; all 273 lines seen; 169/169 voiced lines decode; no bad requests.
- The shots (about 1 GB) aren't committed. To regenerate them in a fresh session:
  1. `git worktree add /tmp/v2base c487bdf`
  2. Serve `/tmp/v2base/v2` and rerun the command above.
- **Diff:** `snapshot_diff.py base_shots baseline-script.json new_shots v2/script.json OUT`.
