# Oct 12 follow-up tests (Planning thread)

**A: anime-structure fight (rōnin vs. beast).** `fight_kling_12fps.mp4` and `fight_veo_12fps.mp4`.
Same 8 cuts, same stills; only the in-betweens differ (Kling v3 Pro, 3 s, vs. Veo 3.1 first-last-frame, 4 s).
- `keys/`: key poses. `cN_start` / `cN_end` feed the generated cuts (C2, C3, C4, C6, C7); `c1_wide`, `c5_impact_v2`, `c8_wide` are the limited cuts (push, impact hold, pan). Files without `_v2` are superseded first passes (no beast mask).
- Rebuild: `python3 production/pipeline/anime/build_fight.py production/cutscene-test/oct12b/keys <raw_clips_dir> <out_dir> k|v`. The raw clips are not committed (fal URLs in `jobs.md` and the build notes).

**B: jigeiko insert, 2 pages.** `insert-script.md`, `insert-spec.json`, `panels/` (color `pN-N.jpg`, B&W `pN-N_bw.jpg`), `pages/`.
- Rebuild: `python3 production/pipeline/manga/compose.py insert-spec.json panels pages [--suffix _bw]` (run from this folder).
