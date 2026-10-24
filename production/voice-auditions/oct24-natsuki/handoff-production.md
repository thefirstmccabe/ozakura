# Handoff to Production: Natsuki's voice, Oct 24 (Audio thread)

The author picked **option 6**: Zephyr with a brighter direction, raised **+1 semitone**.

**Re-voice all of Natsuki's lines** (Ch1 now; Ch2 onward from the start):
- Voice: `Zephyr` (google/gemini-3.8-flash-tts)
- Style instruction (replace the `natsuki` entry in `production/pipeline/vn/voice_jobs.py`):
  "A 16-year-old Japanese high-school girl with a young, light, clear anime-heroine voice. Bright, sunny and quietly confident; playful and teasing, a smile in every line, never loud. Must sound like a teenager, never a grown woman."
  Keep any per-line emotion notes the pipeline adds (wistful, laughing, etc.).
- Post-process every line: `ffmpeg -af "asetrate=24000*1.0595,aresample=24000,atempo=0.9439"` (style guide §7, "+1").
- Past-life Natsuki (the dream woman) is unchanged: Despina.

Reference clip of the picked sound: `bright-up1.mp3` in this folder (the audition lines, not game lines).
