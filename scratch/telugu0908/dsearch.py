#!/usr/bin/env python3
"""
Differential search: identify the part a candidate ADDS to a cluster, not the cluster.

  python3 scratch/telugu0908/dsearch.py subs      # subscript of every consonant
  python3 scratch/telugu0908/dsearch.py tk        # which talakattu hook each base takes
  python3 scratch/telugu0908/dsearch.py matras    # which width variant of each vowel sign

Why the plain cluster search in search.py cannot do this
-------------------------------------------------------
Scoring `క్X` against `base(క) + tk + S` measures mostly the shared క. Every candidate that
puts roughly the right amount of ink below the base lands within noise of every other, which
is exactly what happened: 00B2 / 00D8 / 00E5 "won" for 25 different subscripts.

The fix is to subtract the carrier. Each cell is rendered at a fixed origin and baseline, so
for one font the masks share a coordinate frame and

    added(H, S)   = ink(H + S)      AND NOT ink(H)
    added(C1, C2) = ink(C1 ్ C2)    AND NOT ink(C1)

isolate the subscript on the legacy and the Unicode side respectively. Only then are the two
tight-cropped and scale-normalised and compared, so the measurement is shape-to-shape - the
same thing atlas.py does with outlines, but derived from real shaped rendering, which is what
lets it also answer questions about *positioned* marks that no single glyph can answer.
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)

import slotinfo as S

N = 64
STRIDE = 80
JITTER = 3
BATCH = 400
VIRAMA = '్'
CONS = list('కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరఱలళవశషసహ') + ['క్ష']
MATRAS = list('ాిీుూృౄెేైొోౌ')


def render(items, tag):
    """-> {id: (set of (x,y) ink pixels, box size)} in a per-font fixed frame.

    No tight crop here: the cell box is the frame, so masks from the same font are directly
    comparable and can be subtracted."""
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as fh:
        json.dump(items, fh, ensure_ascii=False)
        ipath = fh.name
    out = os.path.join(tempfile.gettempdir(), f'dsearch_{tag}')
    env = dict(os.environ, ALIGN='left', COLS='10')
    subprocess.run(['node', os.path.join(HERE, 'refsheet.mjs'), ipath, out],
                   cwd=REPO, check=True, capture_output=True, env=env)
    meta = json.load(open(out + '.json'))
    sc = meta['scale']
    page = Image.open(out + '.png')
    PAD = 60
    masks = {}
    for k, b in meta['boxes'].items():
        # identical geometry for every cell of a given font, so the crop is a shared frame
        x = int(b['x'] * sc) - PAD
        y = int(b['y'] * sc) - PAD
        w = int(b['width'] * sc) + 2 * PAD
        h = int(b['height'] * sc) + 2 * PAD
        bw = page.crop((x, y, x + w, y + h)).convert('L').point(lambda v: 255 if v < 200 else 0)
        px = bw.load()
        ink = set()
        for yy in range(h):
            for xx in range(w):
                if px[xx, yy]:
                    ink.add((xx, yy))
        masks[k] = ink
    return masks


def render_all(items):
    masks = {}
    for n in range(0, len(items), BATCH):
        masks.update(render(items[n:n + BATCH], str(n // BATCH)))
    return masks


def pack(ink):
    """Tight-crop a pixel set and pack it aspect-preserved into N x N."""
    if not ink:
        return 0, 0
    xs = [p[0] for p in ink]
    ys = [p[1] for p in ink]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w, h = x1 - x0 + 1, y1 - y0 + 1
    s = N / max(w, h)
    ox = (N - int(w * s)) // 2 + JITTER
    oy = (N - int(h * s)) // 2 + JITTER
    bits = 0
    for x, y in ink:
        bits |= 1 << ((int((y - y0) * s) + oy) * STRIDE + int((x - x0) * s) + ox)
    return bits, bits.bit_count()


def score(a, b):
    ab, an = a
    bb, bn = b
    if not an or not bn:
        return 0.0
    best = 0.0
    for dy in range(-JITTER, JITTER + 1):
        sh = dy * STRIDE
        s1 = bb << sh if sh >= 0 else bb >> -sh
        for dx in range(-JITTER, JITTER + 1):
            c = s1 << dx if dx >= 0 else s1 >> -dx
            i = (ab & c).bit_count()
            if i:
                best = max(best, i / (an + c.bit_count() - i))
    return best


# --------------------------------------------------------------------------- stages

import heads as H

S_ = lambda cps: ''.join(chr(c) for c in cps)


def matra_candidates(c):
    """Every way this font could plausibly write C + vowel sign, as {label: glyph string}.

    Two dimensions the first pass got wrong and this one searches:

    * head form. A sign drawn ABOVE the letter takes the talakattu's place, so it follows the
      narrow `base`; a sign drawn BELOW it (ు ూ ృ ౄ) leaves the top alone, so it follows the
      complete `full` form. Both are offered for every sign and measured.
    * ై. Telugu writes it as the ె mark plus a hook under the letter - Noto spells its own
      ై exactly that way (`aivowelsigntelu` spans y -309..681, `ailengthmarktelu` is the
      -309..-70 part alone) - so every below-baseline slot is tried as the hook rather than
      only the one the atlas guessed.
    """
    out = {}
    base = S_(H.head(c, with_matra=True))
    full = S_(H.head(c))
    pre = H.PRECOMP_I.get(c)
    pu = H.PRECOMP_U.get(c)
    for m, variants in H.MATRA_VARIANTS.items():
        if m == 'ి' and pre:
            out[f"{m}|pre"] = chr(pre[0])
        if m == 'ీ' and pre:
            out[f"{m}|pre"] = chr(pre[1])
        if m == 'ు' and pu:
            out[f"{m}|pre"] = chr(pu[0])
        if m == 'ూ' and pu:
            out[f"{m}|pre"] = chr(pu[1])
        for head, tag in ((base, ''), (full, 'F')):
            if head == base and tag == 'F':
                continue
            for v in variants:
                out[f"{m}|{tag}{v:04X}"] = head + chr(v)
            if m == 'ై':
                # Only the two slots the atlas matched against Noto's `ailengthmarktelu`
                # (both 0.88). Letting every below-baseline slot compete just picks whichever
                # of the 25 subscripts happens to fill the gap best, which is over-fitting:
                # the first pass had ై borrowing ్త, ్గ, ్ల and ్ష for different letters.
                for v in variants:
                    for hook in (0x004F, 0x2022):
                        out[f"{m}|{tag}{v:04X}.{hook:04X}"] = head + chr(v) + chr(hook)
            if m == 'ౄ':
                for v in variants:
                    out[f"{m}|{tag}{v:04X}.002A"] = head + chr(v) + chr(0x2A)
            if m in ('ొ', 'ో', 'ౌ'):
                # composed: the e/ee sign plus a wide right-hand piece, the pattern Modular
                # Infotech uses in its Kannada layout (æ = ೆ, æã = ೊ, æãà = ೋ)
                src = 'ె' if m in ('ొ', 'ౌ') else 'ే'
                for a in H.MATRA_VARIANTS[src]:
                    for b in (0x0026, 0x00F6, 0x00F7, 0x00F8, 0x00F9, 0x00FA, 0x00FB, 0x0178,
                              0x005A, 0x006F, 0x003E, 0x00E9, 0x00EA, 0x00EB):
                        out[f"{m}|{tag}{a:04X}.{b:04X}"] = head + chr(a) + chr(b)
    return out


def stage_matras():
    """For every consonant, decide which width variant of each vowel sign the font expects,
    by comparing the ink each candidate ADDS to the bare head against the ink Unicode adds
    to the bare consonant."""
    items, plan = [], {}
    for c in H.HEAD:
        head = S_(H.head(c, with_matra=True))
        items.append({'id': f"H:{c}", 'text': head, 'font': 'legacy'})
        items.append({'id': f"B:{c}", 'text': c, 'font': 'noto'})
        cands = matra_candidates(c)
        plan[c] = cands
        for lab, txt in cands.items():
            items.append({'id': f"C:{c}:{lab}", 'text': txt, 'font': 'legacy'})
        for m in H.MATRA_VARIANTS:
            items.append({'id': f"R:{c}:{m}", 'text': c + m, 'font': 'noto'})
    print(f"# {len(items)} cells", file=sys.stderr)
    masks = render_all(items)

    result, report = {}, []
    for c in H.HEAD:
        hb = masks.get(f"H:{c}", set())
        bb = masks.get(f"B:{c}", set())
        for m in H.MATRA_VARIANTS:
            ref = pack(masks.get(f"R:{c}:{m}", set()) - bb)
            ranked = []
            for lab in plan[c]:
                if not lab.startswith(m + '|'):
                    continue
                add = masks.get(f"C:{c}:{lab}", set()) - hb
                ranked.append((score(ref, pack(add)), lab))
            ranked.sort(reverse=True)
            if ranked:
                result[c + m] = [[l, round(s, 3)] for s, l in ranked[:5]]
                report.append((c, m, ranked[0]))
    with open(os.path.join(HERE, 'solved_matras.json'), 'w') as fh:
        json.dump(result, fh, ensure_ascii=False, indent=0)
    for c, m, (s, lab) in report:
        print(f"{c}{m:<3} {lab:<20} {s:.2f}")




def stage_width():
    """Learn each consonant's mark width class from the font's own precomposed forms.

    For 17 consonants the font ships a precomposed C+ి and C+ీ. Rendering `base + variant`
    against that precomposed glyph is a comparison of the font with ITSELF - same typeface,
    same frame, same size - so the correct variant scores near 1.0 and the wrong one does
    not. That pins the width class without any cross-typeface guessing, and the class then
    carries over to the ా / ె / ే / ొ / ో / ౌ variants, which the font supplies in matched
    sets of two and three.
    """
    items = []
    for c, (pi, pii) in H.PRECOMP_I.items():
        base = S_(H.head(c, with_matra=True))
        items.append({'id': f"P:{c}:i", 'text': S_(H.head(c, True)[:-1] + [pi]), 'font': 'legacy'})
        items.append({'id': f"P:{c}:ii", 'text': S_(H.head(c, True)[:-1] + [pii]), 'font': 'legacy'})
        for v in H.MATRA_VARIANTS['ి']:
            items.append({'id': f"V:{c}:i:{v:04X}", 'text': base + chr(v), 'font': 'legacy'})
        for v in H.MATRA_VARIANTS['ీ']:
            items.append({'id': f"V:{c}:ii:{v:04X}", 'text': base + chr(v), 'font': 'legacy'})
    print(f"# {len(items)} cells", file=sys.stderr)
    masks = render_all(items)
    for c in H.PRECOMP_I:
        for role, m in (('i', 'ి'), ('ii', 'ీ')):
            ref = pack(masks.get(f"P:{c}:{role}", set()))
            row = sorted(((score(ref, pack(masks.get(f"V:{c}:{role}:{v:04X}", set()))), f"{v:04X}")
                          for v in H.MATRA_VARIANTS[m]), reverse=True)
            print(f"{c}{m:<3} " + '  '.join(f"{v} {s:.3f}" for s, v in row))


if __name__ == '__main__':
    stage = sys.argv[1] if len(sys.argv) > 1 else 'matras'
    if stage == 'matras':
        stage_matras()
    elif stage == 'width':
        stage_width()
    else:
        raise SystemExit(f'unknown stage {stage}')
