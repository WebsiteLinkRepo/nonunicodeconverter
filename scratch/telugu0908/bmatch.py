#!/usr/bin/env python3
"""
Cross-match shaped Unicode references against legacy candidate strings, in one Chromium
pass. This is the tool that decides slot identities.

  python3 scratch/telugu0908/bmatch.py pool.json           # top matches per reference
  python3 scratch/telugu0908/bmatch.py pool.json --by-cand # ... and per candidate

pool.json = {"refs":  [{"id":"ka","text":"క"}, ...],
             "cands": [{"id":"0x4d+tk","text":"Mæ"}, ...],
             "reffont": "noto"}

Both sides are rendered by the same browser at the same size and baseline, so the only
difference being measured is the typeface. The Unicode side needs real GSUB (matras and
conjuncts reorder), which is the whole reason a browser is in the loop; the legacy side
needs the sanitised font (see fixfont.py) or Chromium silently falls back to Latin.

Masks are packed into Python ints, one bit per pixel, with a row stride wider than the
mask so an x-shift cannot bleed into the next row. Score = max IoU over a +/-3 px
translation search. Triage only - confirm the winner on a sheet before writing it down.
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
N = 64          # mask is N x N
STRIDE = 80     # > N + 2*JITTER so shifted rows stay separated
JITTER = 3
PAD = 40        # crop slack: zero-advance marks draw outside the element box


BATCH = 500     # cells per screenshot; a single page of thousands blows past PIL's limit


def _render_batch(items, tag):
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as fh:
        json.dump(items, fh, ensure_ascii=False)
        ipath = fh.name
    out = os.path.join(tempfile.gettempdir(), f'bmatch_sheet_{tag}')
    subprocess.run(['node', os.path.join(HERE, 'refsheet.mjs'), ipath, out],
                   cwd=REPO, check=True, capture_output=True)
    meta = json.load(open(out + '.json'))
    sc = meta['scale']
    page = Image.open(out + '.png')
    masks = {}
    for k, b in meta['boxes'].items():
        box = (max(0, int(b['x'] * sc) - PAD), max(0, int(b['y'] * sc) - PAD),
               int((b['x'] + b['width']) * sc) + PAD, int((b['y'] + b['height']) * sc) + PAD)
        bw = page.crop(box).convert('L').point(lambda v: 255 if v < 200 else 0)
        bb = bw.getbbox()
        masks[k] = bw.crop(bb) if bb else None
    return masks


def render_all(items, reffont='noto'):
    """-> {id: PIL 'L' tight-cropped ink mask}"""
    norm = [{'id': i['id'], 'text': i['text'], 'font': i.get('font', 'legacy')} for i in items]
    masks = {}
    for n in range(0, len(norm), BATCH):
        masks.update(_render_batch(norm[n:n + BATCH], n // BATCH))
    return masks


def pack(img):
    """Tight-cropped 'L' -> (int bitmask, popcount), aspect-preserved into N x N."""
    from PIL import Image
    if img is None:
        return 0, 0
    w, h = img.size
    s = N / max(w, h)
    nw, nh = max(1, round(w * s)), max(1, round(h * s))
    canvas = Image.new('L', (STRIDE, STRIDE), 0)
    canvas.paste(img.resize((nw, nh), Image.LANCZOS),
                 ((N - nw) // 2 + JITTER, (N - nh) // 2 + JITTER))
    px = canvas.load()
    bits = 0
    for y in range(STRIDE):
        row = 0
        for x in range(STRIDE):
            if px[x, y] > 100:
                row |= 1 << x
        bits |= row << (y * STRIDE)
    return bits, bits.bit_count()


def score(a, b):
    """max IoU over a +/-JITTER translation search. a, b are (bits, popcount)."""
    ab, an = a
    bb, bn = b
    if not an or not bn:
        return 0.0
    best = 0.0
    for dy in range(-JITTER, JITTER + 1):
        sh = dy * STRIDE
        shifted = bb << sh if sh >= 0 else bb >> -sh
        for dx in range(-JITTER, JITTER + 1):
            c = shifted << dx if dx >= 0 else shifted >> -dx
            inter = (ab & c).bit_count()
            if inter:
                best = max(best, inter / (an + c.bit_count() - inter))
    return best


def paired(pool, worst=40):
    """Score each ref against the candidate with the SAME id. For verifying a finished
    table rather than searching: 1803 pairs instead of a cross product."""
    items = ([{**r, 'id': 'R:' + r['id'], 'font': pool.get('reffont', 'noto')} for r in pool['refs']]
             + [{**c, 'id': 'C:' + c['id'], 'font': 'legacy'} for c in pool['cands']])
    masks = render_all(items)
    rows = []
    for r in pool['refs']:
        a = pack(masks.get('R:' + r['id']))
        b = pack(masks.get('C:' + r['id']))
        rows.append((score(a, b), r['id'], r['text']))
    rows.sort()
    ok = sum(1 for s, _, _ in rows if s >= 0.45)
    print(f"# {len(rows)} pairs: {ok} at IoU>=0.45, {len(rows) - ok} below")
    print(f"# median {rows[len(rows) // 2][0]:.2f}")

    # Per-category medians, because one number over 1803 mixed cases hides which part of the
    # encoding is actually wrong: a bad conjunct rule and a bad vowel sign look identical in
    # the aggregate.
    from collections import defaultdict
    VIR = '\u0C4D'

    def bucket(s):
        if len(s) == 1 and '\u0C05' <= s <= '\u0C14':
            return 'vowel'
        if s in ('\u0C15\u0C4D\u0C37', '\u0C36\u0C4D\u0C30\u0C40'):
            return 'special'
        if s.endswith('\u0C02'):
            return 'anusvara'
        if s.endswith('\u0C03'):
            return 'visarga'
        if s.endswith(VIR):
            return 'pollu'
        if VIR in s:
            return 'conjunct'
        return 'bare-cons' if len(s) == 1 else 'C+matra'

    g = defaultdict(list)
    for s, i, _t in rows:
        g[bucket(i)].append(s)
    print(f"# {'bucket':<10} {'n':>5} {'median':>7} {'mean':>6} {'>=0.45':>7}")
    for k, v in sorted(g.items()):
        v.sort()
        print(f"# {k:<10} {len(v):>5} {v[len(v) // 2]:>7.2f} "
              f"{sum(v) / len(v):>6.2f} {sum(1 for x in v if x >= 0.45):>7}")
    json.dump([[round(s, 3), i] for s, i, _ in rows],
              open(os.path.join(HERE, 'paired_scores.json'), 'w'), ensure_ascii=False)
    for s, i, t in rows[:worst]:
        print(f"  {s:.2f}  {i}")
    return rows


def main():
    pool = json.load(open(sys.argv[1]))
    if '--paired' in sys.argv:
        paired(pool)
        return
    reffont = pool.get('reffont', 'noto')
    items = ([{**r, 'id': 'R:' + r['id'], 'font': reffont} for r in pool['refs']]
             + [{**c, 'id': 'C:' + c['id'], 'font': 'legacy'} for c in pool['cands']])
    masks = render_all(items, reffont)
    R = {r['id']: pack(masks.get('R:' + r['id'])) for r in pool['refs']}
    C = {c['id']: pack(masks.get('C:' + c['id'])) for c in pool['cands']}
    print(f"# refs={len(R)} cands={len(C)}  (missing: "
          f"{sum(1 for v in list(R.values()) + list(C.values()) if not v[1])})")
    table = {}
    for rid, rm in R.items():
        ranked = sorted(((score(rm, cm), cid) for cid, cm in C.items()), reverse=True)
        table[rid] = ranked
        print(f"{rid:<10} " + '  '.join(f"{c} {s:.2f}" for s, c in ranked[:6]))
    if '--by-cand' in sys.argv:
        print()
        for cid, cm in C.items():
            ranked = sorted(((score(rm, cm), rid) for rid, rm in R.items()), reverse=True)
            print(f"{cid:<10} " + '  '.join(f"{r} {s:.2f}" for s, r in ranked[:4]))
    json.dump({k: v[:12] for k, v in table.items()},
              open(os.path.join(HERE, 'last_match.json'), 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
