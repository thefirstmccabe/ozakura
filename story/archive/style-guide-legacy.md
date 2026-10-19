# Ōzakura — Style guide legacy sections

Moved out of `story/style-guide.md` on Oct 19. Only needed if Manga Vol. 1 (black and white) is ever fixed or extended; current inserts are full color (§4a).

## 4. Manga art (black and white; legacy Vol. 1)
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

