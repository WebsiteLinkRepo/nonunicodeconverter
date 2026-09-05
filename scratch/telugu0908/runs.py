#!/usr/bin/env python3
"""
Audit the tables against the font's own slot ORDER.

    python3 scratch/telugu0908/runs.py            # audit + per-letter verdict
    python3 scratch/telugu0908/runs.py --dump     # every slot in byte order

Why this exists
---------------
Every other channel in this directory scores *shapes*. Shape scores cannot separate the
pairs that matter: between two correct Telugu fonts the IoU of tha-vs-dha is 0.93,
ttha-vs-ra 0.92, pa-vs-sa 0.79, pha-vs-ssa 0.69, gha-vs-ma 0.65. So a shape metric ranks
but does not decide, and that is how wrong letters shipped.

Slot order is independent evidence with no metric in it. The font's (1,0) cmap gives each
glyph its original byte, and Modular Infotech numbered the bytes in varga order, laying each
consonant out as a contiguous run:

    [full]  base  [base+i]  [base+ii]  vattu

so a letter whose vattu the atlas has pinned also has its head pinned, to within the run.
Sorted by plat3 codepoint the runs are shredded, because bytes 0x80-0x9F map through cp1252
to scattered punctuation codepoints; sorted by byte they are contiguous and readable.

A letter whose head is NOT at a run position is an overflow form - the font ran out of
contiguous slots and parked it in the 0x82-0x9C extension block or in a gap. Those are
exactly the letters worth doubting. The published Kannada Shree-Lipi map in
scratch/kannada_shreelipi_repo/ shows the same vendor doing the same thing, and spelling
some overflow letters as multi-glyph compositions rather than single slots.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))

import heads as H
import tel908 as T

VARGA = 'కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరలళవశషసహఱ'


def atlas_labels():
    path = os.path.join(HERE, 'atlas.json')
    if not os.path.exists(path):
        return {}
    slots = json.load(open(path))['slots']
    return {int(k, 16): ' | '.join(f'{a} {v:.2f}' for a, v in s['top'][:3])
            for k, s in slots.items()}


def assignments():
    """plat3 codepoint -> list of roles the shipped tables give it."""
    role = {}

    def add(cp, what):
        role.setdefault(cp, []).append(what)

    for c, (h, tk, narrow, _) in H.HEAD.items():
        add(h, f'{c} head')
        if narrow:
            add(narrow, f'{c} base')
    for c, v in H.VATTU.items():
        add(v, f'_{c} vattu')
    for c, (i, ii) in H.PRECOMP_I.items():
        add(i, f'{c}i'), add(ii, f'{c}ii')
    for c, (u, uu) in H.PRECOMP_U.items():
        add(u, f'{c}u'), add(uu, f'{c}uu')
    for m, variants in H.MATRA_VARIANTS.items():
        for cp in variants:
            add(cp, f'matra {m}')
    for c, cps in H.VOWELS.items():
        for cp in cps:
            add(cp, f'vowel {c}')
    for c, cps in H.DIGITS.items():
        for cp in cps:
            add(cp, f'digit {c}')
    for c, cps in H.LIGATURES.items():
        for cp in cps:
            add(cp, f'lig {c}')
    for cp, what in ((H.PENDANT, 'dha pendant'), (H.ANUSVARA, 'sunna'),
                     (H.VISARGA, 'visarga'), (H.POLLU, 'pollu'),
                     (H.NAKAARA_POLLU, 'na pollu'), (H.REPH, 'reph'),
                     (H.AI_LENGTH, 'ai hook'), (H.TA_RA, 'ta-ra')):
        add(cp, what)
    for cp in H.POLLU_ALT:
        add(cp, 'pollu alt')
    for cp in H.STUBS:
        add(cp, 'pad stub')
    for cp in (0x00E6, 0x00E7, 0x00E8):
        add(cp, 'talakattu')
    return role


def main():
    face = T.Face(os.path.join(REPO, 'public', 'SHREE-TEL.ttf'))
    labels = atlas_labels()
    role = assignments()
    byte = {cp: b for cp, b in face.byte_of.items() if b is not None}
    inv = {}
    for cp in sorted(face.plat3):
        m = face.metrics(cp)
        inv[cp] = (m['adv'], m['bbox'], m['contours'])

    if '--dump' in sys.argv:
        print(f"{'byte':>4} {'plat3':>6} {'adv':>4}  {'assigned to':<22} atlas top-3")
        for cp in sorted(byte, key=lambda c: (byte[c], c)):
            what = ', '.join(role.get(cp, [])) or '-'
            print(f"{byte[cp]:>4X} {cp:>6X} {inv[cp][0]:>4}  {what:<22} {labels.get(cp, '')}")
        print()

    # --- per letter: is the head inside its own contiguous run? -------------------------
    own = {}
    for c in VARGA:
        h, tk, narrow, _ = H.HEAD[c]
        cps = {h, H.VATTU[c]} | ({narrow} if narrow else set())
        cps |= set(H.PRECOMP_I.get(c, ())) | set(H.PRECOMP_U.get(c, ()))
        own[c] = sorted(byte[x] for x in cps if x in byte)

    print('run audit. A letter owns its head, narrow base, precomposed forms and vattu; in')
    print('this font those are consecutive bytes. The vattu is the anchor - atlas.py matched')
    print('it against a NAMED Noto subscript - so a head sitting next to it is pinned by')
    print('order alone. A head far from its own vattu is an overflow form: a guess.\n')
    owner = {}
    for c in VARGA:
        h, tk, narrow, _ = H.HEAD[c]
        for x, n in ([(h, f'{c} head'), (narrow, f'{c} base'), (H.VATTU[c], f'_{c} vattu')]
                     + list(zip(H.PRECOMP_I.get(c, ()), (f'{c}i', f'{c}ii')))
                     + list(zip(H.PRECOMP_U.get(c, ()), (f'{c}u', f'{c}uu')))):
            if x in byte:
                owner.setdefault(byte[x], n)

    print(f"{'ltr':<4}{'head':>5} {'own bytes':<24} verdict")
    parked = []
    for c in VARGA:
        h, tk, narrow, _ = H.HEAD[c]
        hb, vb = byte.get(h), byte.get(H.VATTU[c])
        bs = own[c]
        others = [b for b in bs if b != hb]
        dist = min((abs(b - hb) for b in others), default=0)
        gap = [b for b in range(min(hb, vb) + 1, max(hb, vb)) if b not in bs]
        if dist <= 1:
            verdict = 'in run'
        elif dist <= 3 and all(owner.get(b) is None for b in gap):
            verdict = f'in run ({dist - 1} free slot(s) between head and vattu)'
        else:
            verdict = f'OVERFLOW - head is {dist} bytes from its own run'
            parked.append(c)
        filled = [f'{b:02X}={owner[b]}' for b in gap if b in owner]
        if filled and dist <= 3:
            verdict += '; gap held by ' + ', '.join(filled)
        elif filled:
            verdict += '; gap holds ' + ', '.join(filled[:3])
        if narrow and hb is not None and byte.get(narrow) is not None and hb > byte[narrow]:
            verdict += '; FULL/BASE byte order inverted'
        print(f"{c:<4}{hb:>5X} {' '.join(f'{b:02X}' for b in bs):<24} {verdict}")

    print(f"\noverflow letters ({len(parked)}): {' '.join(parked) or 'none'}")
    print('Their head has no slot of its own, so it is only as good as the shape match that')
    print('chose it. Everything marked "in run" is pinned by slot order, metric or no.\n')

    # --- heads should climb monotonically in varga order --------------------------------
    seq = [(c, byte.get(H.HEAD[c][0])) for c in VARGA]
    bad = [(a, b) for (a, x), (b, y) in zip(seq, seq[1:]) if x is not None and y is not None and y < x]
    print('varga order inversions (a later letter with a lower byte):',
          ' '.join(f'{a}>{b}' for a, b in bad) or 'none')

    # --- what is left over: the candidate pool for the overflow heads -------------------
    free = [cp for cp in sorted(byte, key=lambda c: byte[c])
            if cp not in role and inv[cp][2] not in (0,)]
    print(f'\nunassigned slots with an outline ({len(free)}) - the pool an overflow head'
          ' must come from:')
    print(f"  {'byte':>4} {'plat3':>6} {'adv':>4}  atlas top-3")
    for cp in free:
        print(f"  {byte[cp]:>4X} {cp:>6X} {inv[cp][0]:>4}  {labels.get(cp, '')}")


if __name__ == '__main__':
    main()
