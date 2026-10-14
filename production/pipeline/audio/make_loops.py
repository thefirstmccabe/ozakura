"""Make seamless, leveled BGM loops.
For each track: decode, trim silence and any fade-out tail, then crossfade the
tail into the head so the file loops without a seam. Level to -19 LUFS.
Usage: python3 make_loops.py <name> <src> <outdir> [xfade_seconds]
"""
import sys, subprocess, numpy as np, json
name, src, outdir = sys.argv[1:4]
X = float(sys.argv[4]) if len(sys.argv) > 4 else 3.0
SR = 44100
raw = subprocess.run(["ffmpeg","-v","error","-i",src,"-f","f32le","-ac","2","-ar",str(SR),"-"],capture_output=True).stdout
a = np.frombuffer(raw, dtype=np.float32).reshape(-1,2).copy()
# frame RMS (0.25 s)
hop = SR//4
rms = np.array([np.sqrt(np.mean(a[i:i+hop]**2)+1e-12) for i in range(0,len(a)-hop,hop)])
db = 20*np.log10(rms)
ref = np.median(db[db > db.max()-40])
# start: first frame within 25 dB of median
s = int(np.argmax(db > ref-25))*hop
# end: last frame within 8 dB of median (drops fade-outs and silence)
e_idx = len(db)-1-int(np.argmax(db[::-1] > ref-8))
e = (e_idx+1)*hop
body = a[s:e]
n = int(X*SR)
if len(body) < 3*n: n = len(body)//4
t = np.linspace(0,1,n,dtype=np.float32)[:,None]
fo, fi = np.cos(t*np.pi/2), np.sin(t*np.pi/2)   # equal-power
seam = body[-n:]*fo + body[:n]*fi
loop = np.concatenate([body[n:-n], seam])
tmp = f"/tmp/claude-0/{name}.f32"
loop.astype(np.float32).tofile(tmp)
out = f"{outdir}/{name}.mp3"
subprocess.run(["ffmpeg","-v","error","-y","-f","f32le","-ac","2","-ar",str(SR),"-i",tmp,
  "-af","loudnorm=I=-19:TP=-1.5:LRA=11","-ar",str(SR),"-b:a","192k",out],check=True)
d = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out],capture_output=True,text=True).stdout)
print(json.dumps({"name":name,"src_s":round(len(a)/SR,1),"trim_start_s":round(s/SR,1),"trim_end_s":round(e/SR,1),"loop_s":round(d,1),"xfade_s":round(n/SR,1)}))
