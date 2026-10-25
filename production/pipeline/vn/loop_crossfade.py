"""Make a living still loop seamlessly: the last D frames cross-fade into the first D (the result is D frames shorter).
The loop point then steps from frame D-1 to frame D of the source, an ordinary frame step, so petals and hair don't jump.
Usage: python3 loop_crossfade.py IN.mp4 OUT.mp4 [--frames 12] [--crf 20]"""
import argparse, subprocess, numpy as np
ap = argparse.ArgumentParser(); ap.add_argument("inp"); ap.add_argument("out")
ap.add_argument("--frames", type=int, default=12); ap.add_argument("--crf", default="20"); a = ap.parse_args()
probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate",
                        "-of", "csv=p=0", a.inp], capture_output=True, text=True).stdout.strip().split(",")
w, h, fps = int(probe[0]), int(probe[1]), probe[2]
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", a.inp, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
f = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3).astype(np.float32)
N, D = len(f), a.frames
L = N - D
enc = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", fps, "-i", "-",
                        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", a.crf, "-preset", "slow",
                        "-movflags", "+faststart", "-an", a.out], stdin=subprocess.PIPE)
for i in range(L):
    fr = f[i + D]
    if i >= L - D:
        j = i - (L - D); al = (j + 1) / (D + 1)
        fr = (1 - al) * f[i + D] + al * f[j]
    enc.stdin.write(np.clip(fr + 0.5, 0, 255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait()
print(f"{N} frames in, {L} out; loop point steps from source frame {D - 1} to {D}")
