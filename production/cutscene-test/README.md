# Cutscene test, Oct 10

**What it tests:** whether image-to-video can animate an existing VN CG at an acceptable quality. The source is `img/bg/cg_catch.webp`, converted to PNG. It's deliberately the hard case: two characters touching, faces close up.

| File | Model | Settings | Cost |
|---|---|---|---|
| `A_minimax-h3-max.mp4` | `minimax/h3-max/image-to-video` | 8 s, 768P, prompt expansion off | ~$0.24 |
| `B_kling-v3-pro.mp4` | `fal-ai/kling-video/v3/pro/image-to-video` | 8 s, generate_audio off, custom negative prompt | ~$1.12 |
| `compare_A_vs_B.mp4` | both, stacked | — | — |

**Post-processing:** both clips re-encoded to H.264 at CRF 21 with the audio stripped. The originals are on fal storage and may expire.

**The prompt** (shared by both models): "Hand-drawn 2D anime, continuing this exact illustration in the same art style, line work and colors. In a wooden kendo dojo at golden late afternoon, the boy has just caught the copper-haired girl mid-fall on the wet floor. A held, quiet moment: she breathes in, eyes wide and searching his face; a single tear slowly slides from the corner of her eye; loose strands of her ponytail settle after the fall. He steadies her, his grip firming, a slow exhale. Dust motes drift in the window light. Very slow, gentle camera push-in toward their faces. Subtle, restrained motion only. Keep both faces, proportions, outfits and the background exactly as in the first frame; no morphing, no new people, no text."

Natsuki's long hair here is the superseded design; it doesn't matter for a quality test.
