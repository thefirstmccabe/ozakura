"""Face-window crops (style guide §3a). Square head crop from a transparent sprite or face image.
Usage: python3 faces.py OUTDIR SIDE_FRAC YOFF_FRAC XSHIFT_FRAC file1 file2 ...
SIDE_FRAC: square side as a fraction of image width (or of height, written as e.g. h0.24); YOFF_FRAC: start above the hair top, as a fraction of side;
XSHIFT_FRAC: shift of the crop center from the head's center, as a fraction of side."""
import sys, numpy as np
from PIL import Image
out, side_arg, yoff_f, xs_f = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
by_h = side_arg.startswith('h'); side_f = float(side_arg.lstrip('h'))
for f in sys.argv[5:]:
    im = Image.open(f).convert('RGBA'); w, h = im.size
    a = np.array(im)[..., 3] > 40
    rows = np.where(a.any(1))[0]; top = rows.min()
    side = int((h if by_h else w) * side_f)
    band = a[top:top + side // 2]                 # hair/face band only, ignores shoulders
    cols = np.where(band.any(0))[0]; cx = (cols.min() + cols.max()) // 2 + int(xs_f * side)
    y0 = max(0, top - int(yoff_f * side)); x0 = max(0, min(w - side, cx - side // 2))
    c = im.crop((x0, y0, x0 + side, y0 + side)).resize((384, 384), Image.LANCZOS)
    name = f.split('/')[-1].rsplit('.', 1)[0]
    c.save(f"{out}/{name}.webp", 'WEBP', quality=90, method=6)
    print(name, (x0, y0, side))
