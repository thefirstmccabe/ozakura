"""cg_tree_light (Ch3, 3.4): the Great Cherry background with one point of light hanging just under the low branch
(outline: on screen and deniable, a sunlit petal maybe). Drawn in code on the shipped background, so the place is identical.
Usage: python3 tree_light.py BG OUT"""
import sys
import numpy as np
from PIL import Image
bg = Image.open(sys.argv[1]).convert("RGB"); W, H = bg.size
x0, y0 = 0.515 * W, 0.565 * H                # just under the low branch where it leaves the trunk, against dark bark so it can't read as the sun (Nov 1 cold read: at 0.62/0.635 all three readers took it for the sun on the horizon)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
r = np.hypot((xx - x0) / 1.0, (yy - y0) / 1.15) / (W / 2400)
core = np.exp(-(r / 7.5) ** 2)                 # a small bright point
halo = 0.7 * np.exp(-(r / 20) ** 2) + 0.28 * np.exp(-(r / 60) ** 2)
a = np.clip(core + halo, 0, 1)[..., None]
glow = np.array([248, 252, 255], np.float32)   # a cool white core with a pale blue halo: a sunlit petal, maybe, or snow light
rim = np.array([205, 228, 255], np.float32)
col = glow * (core[..., None] / (core[..., None] + halo[..., None] + 1e-6)) + rim * (halo[..., None] / (core[..., None] + halo[..., None] + 1e-6))
out = np.asarray(bg).astype(np.float32) * (1 - a) + col * a
Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(sys.argv[2], quality=95)
print("light at", round(x0), round(y0))
