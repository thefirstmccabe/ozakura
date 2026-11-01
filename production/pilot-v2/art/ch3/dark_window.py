#!/usr/bin/env python3
"""Ch3 (Nov 1): bg_kohei_room_night with Nanoha's window across the gap dark, for "her light goes out" (c3_0163 on).

Inside the box of her window, warm bright pixels (the lit curtains and room) are pulled toward the night glass color,
keeping the line art and some of the curtain's shading, so the window reads as unlit. Nothing outside the box changes.

  python3 dark_window.py v2/img/bg/bg_kohei_room_night.webp OUT_MASTER.png
then export_cg.py OUT_MASTER.png bg_kohei_room_night_dark (the source is the 2400×1340 game plate; no larger master).
"""
import sys
import numpy as np
from PIL import Image, ImageFilter

src, out = sys.argv[1:3]
im = Image.open(src).convert("RGB")
a = np.asarray(im).astype(np.float32)
H, W = a.shape[:2]
x0, x1, y0, y1 = int(.745 * W), int(.912 * W), int(.235 * H), int(.49 * H)   # her window and its frame, from Kōhei's room
box = a[y0:y1, x0:x1]
R, G, B = box[..., 0], box[..., 1], box[..., 2]
L = .299 * R + .587 * G + .114 * B
warm = np.clip((R - B - 4) / 36, 0, 1) * np.clip((L - 60) / 60, 0, 1)
m = Image.fromarray((warm * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(2.5))
w = (np.asarray(m).astype(np.float32) / 255)[..., None]
glass = np.array([44, 52, 76], np.float32)                    # the night blue of the wall and sky around it
dark = glass * (.78 + .32 * (L[..., None] / 255))             # a trace of the curtain folds, low contrast
box[:] = box * (1 - w) + dark * w
a[y0:y1, x0:x1] = box
Image.fromarray(a.clip(0, 255).astype(np.uint8)).save(out)
print("wrote", out, "box", (x0, y0, x1, y1))
