#!/usr/bin/env python3
"""
Decide Shree-Tel-0908 identities by *searching* candidate emissions against shaped Unicode
references, one stage at a time.

  python3 scratch/telugu0908/search.py bases      # bare consonants: base form + talakattu
  python3 scratch/telugu0908/search.py matras     # C + each of the 13 vowel signs
  python3 scratch/telugu0908/search.py conjuncts  # C1 + virama + C2

Why a search rather than a lookup: the atlas (atlas.py) identifies whole glyphs against
Noto's named atoms, which settles subscripts, matras and full letters. It cannot settle a
Shree-Lipi `base` - a letter with its talakattu removed - because no Unicode font contains
such a partial shape, and it cannot say which of the three talakattu hooks or which width
variant of a matra a given letter expects. Those are answered by rendering the actual
candidate strings and measuring.

The economy that makes it cheap: candidates are rendered ONCE and scored against every
reference. 600 candidate cells plus 37 reference cells in two screenshots gives the whole
36 x 600 score matrix, so the search space can be generous instead of hand-narrowed - which
is exactly where the previous attempt went wrong.

Writes scratch/telugu0908/solved_<stage>.json and prints a ranked report.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import bmatch as B
import slotinfo as S

CONS = list('కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరఱలళవశషసహ') + ['క్ష']
MATRAS = list('ాిీుూృౄెేైొోౌ')
OUT = lambda stage: os.path.join(HERE, f'solved_{stage}.json')


def render(refs, cands):
    """-> (ref masks, cand masks). One browser pass, candidates rendered once."""
    items = ([{'id': 'R:' + k, 'text': v, 'font': 'noto'} for k, v in refs.items()]
             + [{'id': 'C:' + k, 'text': v, 'font': 'legacy'} for k, v in cands.items()])
    masks = B.render_all(items)
    R = {k: B.pack(masks.get('R:' + k)) for k in refs}
    C = {k: B.pack(masks.get('C:' + k)) for k in cands}
    return R, C


def rank(R, C, keep=int(os.environ.get('KEEP', '8'))):
    out = {}
    for rid, rm in R.items():
        scored = sorted(((B.score(rm, cm), cid) for cid, cm in C.items()), reverse=True)
        out[rid] = [[cid, round(sc, 3)] for sc, cid in scored[:keep]]
    return out


def stage_bases():
    """Every main-line slot, alone and with each of the three talakattu hooks."""
    refs = {c: c for c in CONS}
    cands = {}
    for cp in S.LETTERS:
        cands[f"{cp:04X}"] = chr(cp)
        for tk in S.TALAKATTU:
            cands[f"{cp:04X}+{tk:02X}"] = chr(cp) + chr(tk)
    return refs, cands


def stage_matras(solved_bases):
    """base(C) + every above/mid mark, plus every main slot alone to catch precomposed
    forms. Scored against all 13 C+matra references at once."""
    refs = {}
    for c in CONS:
        for m in MATRAS:
            refs[c + m] = c + m
    marks = S.ABOVE + S.MIDMARK + [cp for cp in S.LETTERS]
    cands = {}
    for c in CONS:
        head = solved_bases.get(c, {}).get('base')
        if not head:
            continue
        for cp in marks:
            cands[f"{c}|{cp:04X}"] = head + chr(cp)
        # precomposed: a single main slot standing for the whole C+matra
        for cp in S.LETTERS:
            cands[f"{c}|={cp:04X}"] = chr(cp)
    return refs, cands



#: Bases whose identity is settled beyond doubt by stage 1 (score >= 0.6 with a clear
#: margin). Used as carriers when searching for subscripts: rendering `base(కc) + tk + S`
#: against the reference `క్X` isolates S, and repeating it with a second, differently
#: shaped carrier turns a single measurement into a vote.
CARRIERS = {'క': '\u004D\u00E6', 'ద': '\u00A7\u00E6', 'బ': '\u00BB'}


def stage_subs():
    """Which slot is the subscript of each consonant. Reference `C1 virama C2` with C1 a
    settled carrier; candidate `carrier + slot` over every slot that could physically be a
    subscript - all below-class plus the main-class slots small enough to be a post-base
    form. Two carriers, so a winner has to agree twice."""
    refs, cands = {}, {}
    subslots = S.BELOW + [cp for cp in S.LETTERS if S.SLOTS[cp]['adv'] <= 320]
    for carrier, head in CARRIERS.items():
        for c in CONS:
            refs[f"{carrier}|{c}"] = carrier + '\u0C4D' + c
        for cp in subslots:
            cands[f"{carrier}|{cp:04X}"] = head + chr(cp)
    return refs, cands


def stage_cm():
    """C + vowel sign, scored the same way the acceptance gate scores: whole cluster, tight
    crop, aspect-normalised. The candidate space comes from heads.py (precomposed form where
    the font has one, otherwise base plus each width variant of the sign, plus the composed
    two-piece spellings the Kannada Shree-Lipi layout uses for ొ ో ౌ ై), so the search picks
    among structurally legitimate spellings rather than free-associating.

    The differential metric in dsearch.py is the better instrument in principle but not here:
    a vowel sign overlaps the letter's strokes, so subtracting the bare letter leaves only the
    non-overlapping sliver, and the sliver differs between typefaces more than the marks do.
    """
    import dsearch
    refs, cands = {}, {}
    for c in CONS:
        for m in MATRAS:
            refs[f"{c}{m}"] = c + m
        for lab, txt in dsearch.matra_candidates(c).items():
            cands[f"{c}|{lab}"] = txt
    return refs, cands


def main_spacer():
    """Does a subscript need an advance-only glyph in front of it?

    The subscripts are marks at roughly x -450..-60, so they need the pen about 450 units in,
    but a narrow letter plus its talakattu only reaches ~220 - which is why క్క came out with
    the subscript beside క rather than under it (scratch/telugu0908/geomcheck.py counts 262
    such pairs). The font contains nine glyphs whose outline is a 5x5 stub - invisible - with
    real advances of 179, 200, 205, 242, 250 and 404 units. Those are the obvious candidates
    for the missing advance, so try each of them between the letter and the subscript.
    """
    import heads as H
    A = '\u0C15'
    head = ''.join(chr(x) for x in H.head(A))
    stubs = [cp for cp, v in S.SLOTS.items() if v['class'] == 'blank']
    refs = {b: A + '\u0C4D' + b for b in CONS}
    cands = {}
    for b in CONS:
        cands[f"{b}|-"] = head + chr(H.VATTU[b])
        for sp in stubs:
            cands[f"{b}|{sp:04X}"] = head + chr(sp) + chr(H.VATTU[b])
    print(f"# {len(refs)} refs x {len(cands)} candidates  stubs="
          f"{[(f'{c:04X}', S.SLOTS[c]['adv']) for c in stubs]}", file=sys.stderr)
    R, C = render(refs, cands)
    from collections import Counter
    votes = Counter()
    for b in CONS:
        rm = R[b]
        ranked = sorted(((B.score(rm, C[k]), k.split('|')[1])
                         for k in cands if k.startswith(f"{b}|")), reverse=True)
        votes[ranked[0][1]] += 1
        print(f"\u0C4D{b:<4} " + '  '.join(f"{k} {s:.2f}" for s, k in ranked[:4]))
    print("# winners: " + str(votes.most_common()))


def main_narrow():
    """Given a NARROW first letter, which single glyph writes the subscript?

    క is 182 units wide and its identity is the most solidly evidenced in the font (0.72),
    so `క ్ X` for all 36 X, scored against every slot in the font as the subscript and both
    with and without the talakattu, isolates the question the `chead` search could not answer:
    whether a narrow base takes a different subscript form from a wide one.
    """
    import heads as H
    A = '\u0C15'
    head = ''.join(chr(x) for x in H.head(A, with_matra=True))
    refs = {b: A + '\u0C4D' + b for b in CONS}
    cands = {}
    for cp in S.SLOTS:
        cands[f"n{cp:04X}"] = head + chr(cp)
        for tk in S.TALAKATTU:
            cands[f"t{tk:02X}{cp:04X}"] = head + chr(tk) + chr(cp)
    print(f"# {len(refs)} refs x {len(cands)} candidates", file=sys.stderr)
    R, C = render(refs, cands)
    for b in CONS:
        rm = R[b]
        ranked = sorted(((B.score(rm, cm), cid) for cid, cm in C.items()), reverse=True)[:5]
        cur = f"{H.VATTU[b]:04X}"
        print(f"\u0C4D{b:<4} assigned={cur}  " + '  '.join(f"{c} {s:.2f}" for s, c in ranked))


def main_chead():
    """Which form of the FIRST letter a subscript attaches to.

    The subscripts are zero-advance marks whose ink sits at roughly x -450..-60, so they are
    drawn back over whatever precedes them and need the pen to be around 450 units in. A
    `base` form is only 180-330 wide and `base + talakattu` adds 40, so feeding a subscript a
    narrow base draws it to the LEFT of the letter instead of under it - visible in
    scratch/telugu0908/out/probe: క్క came out with the subscript alongside క, while ల్ల and
    ప్ప, whose first letters are wide, came out right.

    So: for every first letter, try every main-line slot and every slot + talakattu as the
    carrier, with the subscript held fixed at one of three well-evidenced ones, and vote.
    """
    import heads as H
    C2 = ['\u0C32', '\u0C24', '\u0C2E']          # ల, త, మ - subscripts confirmed 0.77 / 0.80 / 28 votes
    refs, cands = {}, {}
    for a in CONS:
        for b in C2:
            refs[f"{a}|{b}"] = a + '\u0C4D' + b
    for cp in S.LETTERS:
        for b in C2:
            cands[f"{cp:04X}|{b}"] = chr(cp) + chr(H.VATTU[b])
            for tk in S.TALAKATTU:
                cands[f"{cp:04X}+{tk:02X}|{b}"] = chr(cp) + chr(tk) + chr(H.VATTU[b])
    print(f"# {len(refs)} refs x {len(cands)} candidates", file=sys.stderr)
    R, C = render(refs, cands)
    from collections import Counter
    out = {}
    for a in CONS:
        votes = Counter()
        best = {}
        for b in C2:
            rm = R[f"{a}|{b}"]
            ranked = sorted(((B.score(rm, C[f"{k}|{b}"]), k)
                             for k in {x.split('|')[0] for x in cands}), reverse=True)
            best[b] = ranked[0]
            for sc, k in ranked[:3]:
                votes[k] += sc
        top = votes.most_common(3)
        out[a] = {'vote': [[k, round(v, 2)] for k, v in top],
                  'best': {b: [best[b][1], round(best[b][0], 3)] for b in C2}}
        cur = ''.join(f'{x:04X}' for x in H.head(a))
        print(f"{a:<4} current={cur:<12} " + '  '.join(f"{k}:{v:.2f}" for k, v in top))
    with open(os.path.join(HERE, 'solved_chead.json'), 'w') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=0)


def main_conj():
    """C1 + virama + C2. Two things are open: whether the first letter keeps its talakattu
    under a subscript, and - for the subscripts the atlas ranked weakly - which slot it is.
    Both are cheap to settle jointly, because there are only a handful of candidates per pair
    and each candidate cell is rendered once."""
    import json as _json
    import heads as H
    atlas = _json.load(open(os.path.join(HERE, 'atlas.json')))['atoms']

    def vattu_options(c):
        """The assigned slot first, then any other slot the atlas ranked for the same
        subscript, so a weak assignment can be overturned by the cluster measurement."""
        opts = [H.VATTU[c]]
        for lab, rows in atlas.items():
            if not lab.startswith('\u0C4D' + c + '/subscript'):
                continue
            for cp, _sc in rows[:3]:
                v = int(cp, 16)
                if v not in opts:
                    opts.append(v)
        return opts[:4]

    refs, cands = {}, {}
    for a in CONS:
        full = ''.join(chr(x) for x in H.head(a))
        base = ''.join(chr(x) for x in H.head(a, with_matra=True))
        for b in CONS:
            refs[f"{a}|{b}"] = a + '\u0C4D' + b
            for tag, head in (('f', full), ('b', base)):
                if tag == 'b' and base == full:
                    continue
                for v in vattu_options(b):
                    cands[f"{a}|{b}|{tag}{v:04X}"] = head + chr(v)
    print(f"# {len(refs)} refs x {len(cands)} candidates", file=sys.stderr)
    R, C = render(refs, cands)
    out = {}
    for a in CONS:
        for b in CONS:
            rm = R[f"{a}|{b}"]
            ranked = sorted(((B.score(rm, C[k]), k.split('|')[2])
                             for k in cands if k.startswith(f"{a}|{b}|")), reverse=True)
            out[f"{a}|{b}"] = {'label': ranked[0][1], 'score': round(ranked[0][0], 3),
                               'runners': [[l, round(s, 3)] for s, l in ranked[1:3]]}
    with open(os.path.join(HERE, 'solved_conj.json'), 'w') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=0)
    sc = sorted(v['score'] for v in out.values())
    print(f"# {len(sc)} pairs, median {sc[len(sc) // 2]:.2f}, "
          f"{sum(1 for x in sc if x >= 0.45)} at >=0.45")
    from collections import Counter
    print("# head choice: " + str(Counter(v['label'][0] for v in out.values())))
    # which subscript slot won, per C2, voting over all 36 first letters
    for b in CONS:
        votes = Counter(out[f"{a}|{b}"]['label'][1:] for a in CONS)
        print(f"\u0C4D{b:<4} " + '  '.join(f"{k}:{n}" for k, n in votes.most_common(3)))


def main_cm():
    """Constrained ranking: each C+matra reference is scored only against the candidates
    spelled for that same pair. Ranking against the whole pool (as the other stages do) lets
    a candidate labelled for a different vowel sign win on shape alone, which is a useful
    consistency signal but not a usable verdict."""
    import dsearch
    refs = {f"{c}{m}": c + m for c in CONS for m in MATRAS}
    plan = {c: dsearch.matra_candidates(c) for c in CONS}
    cands = {f"{c}|{lab}": txt for c in CONS for lab, txt in plan[c].items()}
    print(f"# {len(refs)} refs x {len(cands)} candidates (constrained)", file=sys.stderr)
    R, C = render(refs, cands)
    out = {}
    for c in CONS:
        for m in MATRAS:
            rm = R[f"{c}{m}"]
            ranked = sorted(((B.score(rm, C[f"{c}|{lab}"]), lab)
                             for lab in plan[c] if lab.startswith(m + '|')), reverse=True)
            if not ranked:
                continue
            out[c + m] = {'label': ranked[0][1].split('|', 1)[1],
                          'score': round(ranked[0][0], 3),
                          'runners': [[l.split('|', 1)[1], round(s, 3)] for s, l in ranked[1:4]]}
    with open(os.path.join(HERE, 'solved_cm.json'), 'w') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=0)
    scores = sorted(v['score'] for v in out.values())
    print(f"# {len(scores)} pairs, median {scores[len(scores) // 2]:.2f}, "
          f"{sum(1 for s in scores if s >= 0.45)} at >=0.45")
    for k, v in out.items():
        print(f"{k:<8} {v['label']:<18} {v['score']:.2f}")


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else 'bases'
    if stage == 'cm':
        return main_cm()
    if stage == 'conj':
        return main_conj()
    if stage == 'chead':
        return main_chead()
    if stage == 'narrow':
        return main_narrow()
    if stage == 'spacer':
        return main_spacer()
    if stage == 'bases':
        refs, cands = stage_bases()
    elif stage == 'cm':
        refs, cands = stage_cm()
    elif stage == 'subs':
        refs, cands = stage_subs()
    elif stage == 'matras':
        prev = json.load(open(OUT('bases')))
        refs, cands = stage_matras(prev)
    else:
        raise SystemExit(f'unknown stage {stage}')

    print(f"# {len(refs)} refs x {len(cands)} candidates", file=sys.stderr)
    R, C = render(refs, cands)
    missing = [k for k, v in list(R.items()) + list(C.items()) if not v[1]]
    if missing:
        print(f"# WARNING {len(missing)} empty renders, e.g. {missing[:5]}", file=sys.stderr)
    table = rank(R, C)
    with open(OUT(stage) + '.raw', 'w') as fh:
        json.dump(table, fh, ensure_ascii=False, indent=0)
    for rid in refs:
        row = table[rid]
        print(f"{rid:<8} " + '  '.join(f"{c} {s:.2f}" for c, s in row[:6]))


if __name__ == '__main__':
    main()
