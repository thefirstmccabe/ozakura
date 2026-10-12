"""Assemble the Oct 12 anime-structure fight test (rōnin vs. beast).

Usage: python3 build_fight.py <keys_dir> <clips_dir> <out_dir> <model_prefix>
  keys_dir   production/cutscene-test/oct12b/keys (c1_wide.jpg, c5_impact_v2.jpg, c8_wide.jpg)
  clips_dir  raw generated in-betweens named <prefix><cut>.mp4, e.g. k2.mp4 / v2.mp4
  prefix     k (Kling v3 Pro) or v (Veo 3.1 first-last-frame)

Method: limited cuts (push, impact hold, pan) are made from stills in ffmpeg; animated cuts
are generated between approved start/end key poses, trimmed, sped up to anime pacing and
dropped to 12 fps ("on twos"). Hard cuts throughout. Output 1280x720, no audio.
"""
import os, subprocess, sys

FPS = 12
W, H = 1280, 720

# cut -> (source window start, end in seconds, target on-screen duration)
ANIM = {
    'k': {2: (0.0, 3.0, 2.0), 3: (0.0, 3.0, 1.5), 4: (1.2, 3.0, 1.3), 6: (0.0, 3.0, 1.4), 7: (0.0, 3.0, 1.8)},
    'v': {2: (0.0, 4.0, 2.0), 3: (0.0, 4.0, 1.5), 4: (0.0, 2.4, 1.5), 6: (0.0, 4.0, 1.6), 7: (0.0, 4.0, 1.8)},
}


def ff(args):
    subprocess.run(['ffmpeg', '-v', 'error', '-y'] + args, check=True)


ENC = ['-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-r', str(FPS), '-an']


def push(still, out, dur=2.5, z=0.06):
    n = int(dur * FPS)
    ff(['-i', still, '-vf',
        f"scale=3840:-2,zoompan=z='1+{z}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}",
        '-frames:v', str(n)] + ENC + [out])


def pan(still, out, dur=2.5):
    ff(['-loop', '1', '-i', still, '-t', str(dur), '-vf',
        f"scale=1600:-2,crop={W}:{H}:x='(iw-{W})*t/{dur}':y='(ih-{H})/2',fps={FPS}"] + ENC + [out])


def impact(still, out, dur=0.75):
    ff(['-loop', '1', '-i', still, '-t', str(dur), '-vf',
        f"scale=1376:774,crop={W}:{H}:x='48+26*sin(n*2.7)*exp(-n/5)':y='27+16*cos(n*3.1)*exp(-n/5)',"
        f"fps={FPS},fade=t=in:st=0:d=0.17:color=white"] + ENC + [out])


def anim(src, out, a, b, target):
    k = target / (b - a)
    ff(['-ss', str(a), '-to', str(b), '-i', src, '-vf',
        f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setpts={k}*PTS,fps={FPS}"] + ENC + [out])


def main(keys, clips, out_dir, p):
    os.makedirs(out_dir, exist_ok=True)
    tmp = os.path.join(out_dir, f'_parts_{p}')
    os.makedirs(tmp, exist_ok=True)
    parts = []
    push(os.path.join(keys, 'c1_wide.jpg'), f'{tmp}/c1.mp4'); parts.append('c1')
    for c in (2, 3, 4):
        anim(os.path.join(clips, f'{p}{c}.mp4'), f'{tmp}/c{c}.mp4', *ANIM[p][c]); parts.append(f'c{c}')
    impact(os.path.join(keys, 'c5_impact_v2.jpg'), f'{tmp}/c5.mp4'); parts.append('c5')
    for c in (6, 7):
        anim(os.path.join(clips, f'{p}{c}.mp4'), f'{tmp}/c{c}.mp4', *ANIM[p][c]); parts.append(f'c{c}')
    pan(os.path.join(keys, 'c8_wide.jpg'), f'{tmp}/c8.mp4'); parts.append('c8')
    with open(f'{tmp}/list.txt', 'w') as f:
        f.writelines(f"file '{x}.mp4'\n" for x in parts)
    out = os.path.join(out_dir, f'fight_{"kling" if p == "k" else "veo"}_12fps.mp4')
    ff(['-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
        '-crf', '20', '-r', str(FPS), '-an', '-movflags', '+faststart', out])
    print(out)


if __name__ == '__main__':
    main(*sys.argv[1:5])
