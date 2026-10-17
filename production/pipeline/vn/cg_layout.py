"""Layout sketch for a two-character CG (style guide §6: give the model a layout to paint over).
Crops the scene's background plate and pastes the characters at their true relative heights,
so head sizes and who-reaches-whose-chin come from the inches, not from the model's guess.

Usage: python3 cg_layout.py OUT.jpg BG.webp CROP_X0 CROP_Y0 CROP_X1 CROP_Y1 PX_PER_IN FLOOR_IN  FIG [FIG ...]
  CROP_*: fractions of the background (keep 16:9). Output is 2752x1536.
  PX_PER_IN: output pixels per inch of height. FLOOR_IN: height above the ground at the frame's bottom edge.
  FIG = path:kind:height_in:visible_frac:lift_in:center_x_frac[:mirror]
    kind 'sprite' (transparent thigh-up sprite; visible_frac = engine v) or 'full' (full-body ref on white; visible_frac ignored)
    lift_in: raise (e.g. 2 for up on her toes)."""
import sys, numpy as np
from PIL import Image, ImageOps
out, bgp = sys.argv[1], sys.argv[2]
cx0, cy0, cx1, cy1, ppi, floor = map(float, sys.argv[3:9])
W, H = 2752, 1536
bg = Image.open(bgp).convert('RGB'); bw, bh = bg.size
canvas = bg.crop((int(cx0 * bw), int(cy0 * bh), int(cx1 * bw), int(cy1 * bh))).resize((W, H), Image.LANCZOS).convert('RGBA')
ground_y = H + floor * ppi
for spec in sys.argv[9:]:
    p = spec.split(':'); path, kind = p[0], p[1]; h, v, lift, cx = map(float, p[2:6]); mirror = len(p) > 6
    im = Image.open(path).convert('RGBA')
    if kind == 'full':   # white background -> alpha: only near-white connected to the image edge (a white shirt stays)
        from scipy import ndimage
        a = np.array(im); white = a[..., :3].min(axis=2) > 236
        lab, _ = ndimage.label(white); edge = set(np.unique(np.r_[lab[0], lab[-1], lab[:, 0], lab[:, -1]])) - {0}
        bgmask = np.isin(lab, list(edge)); a[..., 3] = np.where(bgmask, 0, 255); im = Image.fromarray(a)
    a = np.array(im)[..., 3]; ys, xs = np.where(a > 24); im = im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    if mirror: im = ImageOps.mirror(im)
    span_in = h if kind == 'full' else h * v               # inches covered by the cropped image, head top to its bottom edge
    sc = span_in * ppi / im.height; im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.LANCZOS)
    bottom_in = lift + (0 if kind == 'full' else h * (1 - v))
    y_bottom = ground_y - bottom_in * ppi
    canvas.alpha_composite(im, (int(cx * W - im.width / 2), int(y_bottom - im.height)))
    print(f"{path}: head top y={int(y_bottom - im.height)}, height {im.height}px")
canvas.convert('RGB').save(out, quality=92)
