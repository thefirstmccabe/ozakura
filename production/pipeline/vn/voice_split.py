"""Split one batched TTS take (several lines read in order, one speaker) back into lines.

The take's pauses between lines are only a little longer than pauses inside a line, so cut points are chosen
by dynamic programming: segment durations should match each line's expected length (from its kana count),
and cuts prefer long silences. Segments whose length is far from expected are flagged for a re-take.

Usage as a module: split(wav_path, texts) -> list of (start_s, end_s, ratio)
"""
import numpy as np, wave, re

FR = 0.01  # analysis frame, seconds


def load(path):
    w = wave.open(path)
    sr = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float) / 32768
    return x, sr


def weight(text):
    """Rough spoken length of a Japanese line: kana/kanji count, plus pauses for punctuation."""
    t = re.sub(r"\s", "", text)
    chars = len(re.sub(r"[、。！？!?…「」『』・ー〜―]", "", t))
    kanji = len(re.findall(r"[一-鿿]", t))
    pauses = len(re.findall(r"[、]", t)) * 0.8 + len(re.findall(r"[。！？!?]", t)) * 1.2 + t.count("……") * 1.5
    return chars + kanji * 0.8 + pauses + 1.5


def silences(x, sr, min_len=0.22):
    fr = int(sr * FR)
    n = len(x) // fr
    e = np.sqrt(np.mean(x[: n * fr].reshape(n, fr) ** 2, axis=1))
    th = max(0.004, np.percentile(e, 25) * 1.6)
    sil = e < th
    runs, i = [], 0
    while i < n:
        if sil[i]:
            j = i
            while j < n and sil[j]:
                j += 1
            runs.append((i * FR, j * FR))
            i = j
        else:
            i += 1
    total = n * FR
    lead = runs[0][1] if runs and runs[0][0] == 0 else 0.0
    tail = runs[-1][0] if runs and runs[-1][1] >= total - FR else total
    inner = [r for r in runs if r[0] > lead and r[1] < tail and r[1] - r[0] >= min_len]
    return inner, lead, tail


def split(path, texts):
    x, sr = load(path)
    gaps, lead, tail = silences(x, sr)
    n = len(texts)
    if n == 1:
        return [(lead, tail, 1.0)]
    w = np.array([weight(t) for t in texts])
    speech = tail - lead - sum(g[1] - g[0] for g in gaps) * 0.5
    exp = w / w.sum() * speech
    # candidate cut k: gap gaps[k]; boundary times
    G = len(gaps)
    if G < n - 1:
        raise ValueError(f"only {G} pauses for {n} lines")
    starts = [lead] + [g[1] for g in gaps]
    ends = [g[0] for g in gaps] + [tail]
    glen = [g[1] - g[0] for g in gaps]
    INF = 1e18
    # dp[i][k]: best cost with line i ending at boundary k (k = index into ends; k=G means tail)
    dp = np.full((n, G + 1), INF)
    bp = np.zeros((n, G + 1), dtype=int)

    def seg_cost(i, s_idx, e_idx):
        d = ends[e_idx] - starts[s_idx]
        if d <= 0.05:
            return INF
        return (np.log(d / exp[i])) ** 2

    for k in range(G + 1):
        dp[0][k] = seg_cost(0, 0, k) - (1.2 * glen[k] if k < G else 0)
    for i in range(1, n):
        for k in range(i, G + 1):
            best, arg = INF, -1
            for j in range(i - 1, k):
                if dp[i - 1][j] >= INF:
                    continue
                c = dp[i - 1][j] + seg_cost(i, j + 1, k) - (1.2 * glen[k] if k < G else 0)
                if c < best:
                    best, arg = c, j
            dp[i][k], bp[i][k] = best, arg
    k = G
    cuts = []
    for i in range(n - 1, -1, -1):
        cuts.append(k)
        k = bp[i][k]
    cuts = cuts[::-1]
    out, prev = [], 0
    for i, k in enumerate(cuts):
        s = starts[prev] if i else lead
        e = ends[k]
        out.append((s, e, (e - s) / exp[i]))
        prev = k + 1
    return out


if __name__ == "__main__":
    import sys, json
    path, texts = sys.argv[1], json.load(open(sys.argv[2]))
    for (s, e, r), t in zip(split(path, texts), texts):
        print(f"{s:6.2f} {e:6.2f} {e - s:5.2f}s ratio {r:4.2f}  {t}")
