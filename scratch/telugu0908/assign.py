#!/usr/bin/env python3
"""
Globally assign the 36 Telugu consonants to legacy glyph recipes, 1-to-1.

  python3 scratch/telugu0908/assign.py

Per-letter nearest-neighbour matching fails on this font because several Telugu letters
are near-homoglyphs (న/స, ప/వ, ఖ/ఘ, జ/ఙ, మ/య) and they all pile onto the same handful of
candidates. Forcing a one-to-one assignment fixes that: a candidate can only be spent
once, so the second-best letter is pushed onto its own true match.

Greedy seed, then pairwise swaps until no swap lowers the total cost. Prints the
assignment plus, for each letter, how much better its winner was than its runner-up -
low margin means "go look at the sheet".
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bmatch

HERE = os.path.dirname(os.path.abspath(__file__))
CONS = list('కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరలళవశషసహఱ')
MARKS = [None, 0xE6, 0xE7, 0xE8]


def build_candidates(inv):
    cands = []
    for r in inv['rows']:
        if r['class'] != 'BASE':
            continue
        for m in MARKS:
            if m is None:
                cands.append({'id': f"{r['cp']:#04x}", 'text': chr(r['cp'])})
            else:
                cands.append({'id': f"{r['cp']:#04x}+{m:#04x}", 'text': chr(r['cp']) + chr(m)})
    return cands


def main():
    inv = json.load(open(os.path.join(HERE, 'inventory.json')))
    cands = build_candidates(inv)
    refs = [{'id': c, 'text': c} for c in CONS]
    items = ([{**r, 'id': 'R:' + r['id'], 'font': 'noto'} for r in refs]
             + [{**c, 'id': 'C:' + c['id'], 'font': 'legacy'} for c in cands])
    masks = bmatch.render_all(items)
    R = {r['id']: bmatch.pack(masks.get('R:' + r['id'])) for r in refs}
    C = {c['id']: bmatch.pack(masks.get('C:' + c['id'])) for c in cands}
    ids = list(C)
    print(f"# {len(R)} letters x {len(C)} candidates", flush=True)

    sim = {r: {c: bmatch.score(R[r], C[c]) for c in ids} for r in R}
    cost = {r: {c: 1.0 - v for c, v in row.items()} for r, row in sim.items()}

    # greedy seed over globally best pairs
    pairs = sorted(((cost[r][c], r, c) for r in cost for c in ids))
    assign, used = {}, set()
    for _, r, c in pairs:
        if r not in assign and c not in used:
            assign[r], _ = c, used.add(c)

    # pairwise swap until stable
    changed = True
    while changed:
        changed = False
        letters = list(assign)
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                a, b = letters[i], letters[j]
                ca, cb = assign[a], assign[b]
                if cost[a][ca] + cost[b][cb] > cost[a][cb] + cost[b][ca] + 1e-9:
                    assign[a], assign[b] = cb, ca
                    changed = True

    out = {}
    for c in CONS:
        won = assign[c]
        runner = sorted(((v, k) for k, v in sim[c].items() if k != won), reverse=True)[0]
        out[c] = {'recipe': won, 'score': round(sim[c][won], 3),
                  'runnerUp': runner[1], 'runnerScore': round(runner[0], 3)}
        flag = '  <-- LOW' if sim[c][won] < 0.45 else ''
        print(f"{c}  {won:<12} {sim[c][won]:.2f}   (2nd {runner[1]} {runner[0]:.2f}){flag}")
    json.dump(out, open(os.path.join(HERE, 'assign_consonants.json'), 'w'),
              ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
