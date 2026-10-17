"""bg_houses_night_lit: the night houses plate with Nanoha's upstairs light on. Her window faces Kōhei's
across the three-foot gap, so from the street the light shows only as a warm glow spilling into the gap.
Usage: python3 gap_glow.py in.png out.png"""
import sys, numpy as np
from PIL import Image, ImageFilter
im = Image.open(sys.argv[1]).convert('RGB'); a = np.asarray(im).astype(float) / 255
h, w = a.shape[:2]; sx, sy = w / 2752, h / 1536
yy, xx = np.mgrid[0:h, 0:w]
cx, cy = 1356 * sx, 650 * sy
# tall narrow glow inside the gap, brightest at the upstairs window height
g = np.exp(-(((xx - cx) / (46 * sx)) ** 2) - (((yy - cy) / (190 * sy)) ** 2))
halo = 0.35 * np.exp(-(((xx - cx) / (140 * sx)) ** 2) - (((yy - cy) / (260 * sy)) ** 2))
m = np.clip(g + halo, 0, 1)[..., None]
warm = np.array([1.0, 0.74, 0.45])
out = 1 - (1 - a) * (1 - m * 0.62 * warm)          # screen blend
Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8)).save(sys.argv[2])
