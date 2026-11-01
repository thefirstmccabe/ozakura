"""cg_tree_light (Ch3, 3.4): the Great Cherry background with one point of light hanging just under the low branch
(outline: on screen and deniable, a sunlit petal maybe). Drawn in code on the shipped background, so the place is identical.
Usage: python3 tree_light.py BG OUT"""
import sys
import numpy as np
from PIL import Image
bg = Image.open(sys.argv[1]).convert("RGB"); W, H = bg.size
x0, y0 = 0.62 * W, 0.635 * H                  # under the low branch, against the darker green hill so it reads
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
r = np.hypot((xx - x0) / 1.0, (yy - y0) / 1.15) / (W / 2400)
core = np.exp(-(r / 7.5) ** 2)                 # a small bright point
halo = 0.75 * np.exp(-(r / 26) ** 2) + 0.32 * np.exp(-(r / 85) ** 2)
a = np.clip(core + halo, 0, 1)[..., None]
glow = np.array([255, 251, 226], np.float32)   # a warm white core with a golden halo: sunlight, or not
rim = np.array([255, 224, 150], np.float32)
col = glow * (core[..., None] / (core[..., None] + halo[..., None] + 1e-6)) + rim * (halo[..., None] / (core[..., None] + halo[..., None] + 1e-6))
out = np.asarray(bg).astype(np.float32) * (1 - a) + col * a
Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(sys.argv[2], quality=95)
print("light at", round(x0), round(y0))
