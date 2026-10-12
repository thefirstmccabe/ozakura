# Cutscene tests 2, Oct 12 (locked designs, 10 s)

| File | What | Model | Est. cost |
|---|---|---|---|
| `startframe_action.jpg` | The rōnin vs. the beast on the misty path. Refs: `inventory/beast-size-reference-v2.png`, `inventory/ronin-B.png`, `locations/past-mist-path.png` | nano-banana-pro/edit 2K | ~$0.15 |
| `startframe_bridge.jpg` | Kōhei and Natsuki at dusk by the bridge. Refs: `design-oct10/r3/kohei-short-A.png`, `natsuki-v2/01-restyle-uniform.png`, `img/bg/bg_bridge_dusk.webp` | nano-banana-pro/edit 2K | ~$0.15 |
| `action_A_kling-v3-pro.mp4` | Action, 10 s | fal-ai/kling-video/v3/pro/image-to-video | ~$1.40 |
| `action_B_minimax-h3-max.mp4` | Action, 10 s | minimax/h3-max/image-to-video 768P | ~$0.30 |
| `cut_kling-multishot.mp4` | Two shots in one 10 s generation (wide → close-up), with character elements | Kling v3 Pro, multi_prompt and elements | ~$1.40 |

**Claude's frame review:**

- **Action A (Kling):** real choreography: lunge, dodge, slash arc, second charge, then a bind with the jaws on the blade. Style and designs hold.
  - **Flaw at ~7.6 s:** the beast rears into him, and the two positions swap between frames, which is a spatial jump.
  - **Size:** the beast sometimes reads larger than the size rule.
- **Action B (H3 Max):** one slash, then about 6 s held in the jaws-on-blade bind while sliding. Less elaborate.
  - **Blood:** a small red streak at ~1.5 s despite "no blood" in the prompt.
  - A foreground tree sweeps past (parallax), which works.
- **Bridge start frame:** they read as walking on the riverbank path in front of the bridge, not on it. Fine for a continuity test; it needs a layout fix for real use.
- **Cut (Kling multi-shot):** wide (0–5 s), then a close-up of Natsuki (5–10 s). The cut lands cleanly and she's recognizable: copper hair, amber eyes, uniform and bow.
  - **Close-up drift:** her hair grows to chest length (should end at the shoulders); the look goes softer and more generic (cleaner cel shading, less of the ink-and-paint linework); an invented ear stud appears.
  - **Wide shot:** stays on-model, but they barely advance.
  - **Lesson:** don't rely on in-generation cuts for close-ups. Make each shot from its own approved start frame and cut them together in editing.
