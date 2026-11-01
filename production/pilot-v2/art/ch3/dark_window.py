#!/usr/bin/env python3
"""Ch3 (Nov 1): bg_kohei_room_night with Nanoha's window across the gap dark, for "her light goes out" (c3_0163 on).

Inside the box of her window, warm bright pixels (the lit curtains and room) are pulled toward the night glass color,
keeping the line art and some of the curtain's shading, so the window reads as unlit; then the warm spill on the frame\nand wall around it is cooled to the wall's gray at the same value. Nothing else changes.

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
x0, x1, y0, y1 = int(.745 * W), int(.912 * W), int(.235 * H), int(.485 * H)   # the panes of her window, from Kōhei's room
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
# the lamp's spill on the frame and wall around the panes (build review r2): cool only the warm pixels, keeping their value
X0, X1, Y0, Y1 = int(.722 * W), int(.918 * W), int(.226 * H), int(.50 * H)
ring = a[Y0:Y1, X0:X1]
R, G, B = ring[..., 0], ring[..., 1], ring[..., 2]
L = (.299 * R + .587 * G + .114 * B)[..., None]
cast = np.clip((R - B - 2) / 24, 0, 1)[..., None]
cool = L * np.array([.94, .99, 1.10], np.float32)              # the same value, in the cool gray of the wall
ring[:] = ring * (1 - cast) + cool * cast
a[Y0:Y1, X0:X1] = ring
Image.fromarray(a.clip(0, 255).astype(np.uint8)).save(out)
print("wrote", out, "box", (x0, y0, x1, y1))
