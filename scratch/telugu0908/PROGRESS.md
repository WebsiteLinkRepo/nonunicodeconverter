# Shree-Tel-0908 Telugu converter — progress / handoff

**To resume in a new chat, say:** "read scratch/telugu0908/PROGRESS.md and the approved
plan at ~/.claude/plans/woolly-singing-sedgewick.md, then continue."

Approved plan: `/home/samuelvictor/.claude/plans/woolly-singing-sedgewick.md`

## Goal

Correct both-direction converter for the legacy Shree-Lipi Telugu font
`public/SHREE-TEL.ttf` (= `~/Downloads/Shree-Tel-0908 Regular (2).ttf`, byte-identical,
md5 `e1c117bbab3d4e135139c7804736a3c9`). No competitor site and no ShreeLipi software
exist, so every mapping must be recovered from the font and backed by a measurement.

Decisions the user made:
- The new engine **replaces** the existing `shreelipi` + `telugu` path (retire
  `src/utils/shreeLipiTeluguConverter.ts`), rather than adding a second dropdown entry.
- ఋ ౠ ఌ ౡ have no glyph: keep the `బ`/`ల` + kommu approximation, **no warning**.
- User-confirmed ground truth (their own screenshot):
  `అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఎ ఏ ఐ ఒ ఓ ఔ అం అః` = `A B C D E F º$$ º$* G H I J K L A… A@`

## Key facts established (all measured, none assumed)

- Emit **(3,1) cmap codepoints** (cp1252-range chars), not raw bytes. That is what
  Chromium and Windows both look up. 217 codepoints available.
- Glyph names in the font are standard Macintosh names assigned by position — meaningless.
- Slot census: 166 main-line, 25 below-base (subscripts), 16 above-base, 9 blank stubs.
- Chromium's sanitiser rejects `SHREE-TEL.ttf` (`post: Bad string index 5`).
  `fixfont.py` already produced the loadable `public/SHREE-TEL-web.ttf` (untracked).
  No `@font-face` for this family exists in `src/` yet, so preview can't work.
- Reverse conversion for Telugu Shree-Lipi is currently **broken in main**: it falls
  through to `getMapping('shreelipi')`, which returns the *Devanagari* table.
- Baseline accuracy of the pre-existing untracked tables, `bmatch.py --paired`
  (1803 cases): median IoU 0.26, only 305 at >=0.45. Conjuncts median 0.24 (unsolved);
  bare consonants 0.56; correct pairs measure 0.55-0.75.

## Tooling state

| file | state |
|---|---|
| `glyphmask.py` | **NEW, working.** pycairo single-glyph rasteriser + bitset IoU. self-match 1.0, ka-vs-ba 0.21. |
| `notoatoms.py` | **NEW, working.** Decodes Noto Serif Telugu glyph names into (Telugu text, role). 719 names, only 5 unrecognised. Noto elides a consonant's trailing `a` before a vowel-initial role (`ka`+`ivowel` = `kivowel`), handled. |
| `atlas.py` | **NEW, ran once.** Scores all 217 slots against 666 named Noto atoms. Wrote `atlas.json`; report saved at `/tmp/atlas_report.txt` (regenerate with `python3 scratch/telugu0908/atlas.py > /tmp/atlas_report.txt`). ~6 min. |
| `bmatch.py` | pre-existing. `--paired` is the acceptance gate. Still needs `--vote` (contextual voting) and `--selfcheck` modes. |
| `identities.py` | pre-existing, **substantially wrong**. Being rebuilt from atlas + voting. |
| `build_tables.py` | pre-existing; generates the TS mapping. Needs extending for length marks / composed matras / special conjuncts. |
| `verify.mjs` | pre-existing; `roundtrip` and `spec` modes. Needs a wider case set + contact sheet. |
| `heads.py` | **NEW.** The derived head / base / vattu / precomposed tables, the vowel-sign variant pool, and the geometric `pad_for` / `pollu_for` rules. Single source of truth for `build_tables.py`. |
| `search.py` | **NEW.** Stages `bases`, `cm`, `conj`, `chead`, `narrow`, `spacer`. Candidates rendered once, scored against every reference. |
| `dsearch.py` | **NEW.** Differential rendering (subtract the carrier) plus the `width` stage. Useful for marks that stand clear of the letter; not for signs that overlap it. |
| `geomcheck.py` | **NEW.** Pure-geometry check: which conjuncts would draw the subscript beside the letter instead of under it. 262 → 41 after the pad. |
| `assign.py` | pre-existing, now obsolete — the run-anchored search replaced the planned Hungarian assignment. |

## Where it stands

**Shipped and verified.** The engine replaces the old Telugu Shree-Lipi path in both
directions, tests pass, `astro check` is clean for the changed files and `npm run build`
succeeds.

Acceptance gate (`bmatch.py --paired`, 1803 clusters, Noto Serif Telugu reference vs
Shree-Tel candidate, IoU over a ±3px search). Correct pairs measure 0.55–0.75 in this metric,
so it ranks and triages — it is not a proof:

| bucket | before | now |
|---|---|---|
| overall median | 0.26 | **0.45** |
| at IoU ≥ 0.45 | 305 / 1803 | **894 / 1803** |
| C + vowel sign | 0.32 | **0.47** |
| conjuncts | 0.24 | **0.45** |
| bare consonants | 0.56 | **0.59** |
| pollu | 0.38 | **0.43** |
| vowels | 0.52 | 0.52 |
| visarga | 0.28 | 0.31 |
| anusvara | 0.38 | 0.38 |

Round-trip: 1803/1803 clean. Table generator reports no slot serving two roles.

## The four things that produced the improvement

1. **Per-consonant vowel-sign spelling.** The font ships width variants of ా ి ీ ె ే ొ ో ౌ
   (three of ా, ె and ే; two of ి and ీ) and precomposed C+ి / C+ీ glyphs for 17 consonants.
   Modelling one variant per sign — what the old tables did — misplaces the sign on most
   letters.
2. **Head form depends on where the sign sits.** Signs above the letter take the talakattu's
   place and follow the narrow base; ు ూ ృ ౄ hang below and follow the complete form.
3. **ై is two pieces** — the ె mark plus a hook under the letter, as Noto spells its own ై.
4. **Conjuncts need an advance-only pad.** A subscript is a mark whose ink sits at x −450…−60,
   so it needs the pen ~450 units in; a narrow letter plus its talakattu only reaches ~220 and
   the mark lands *beside* the letter. The font has five invisible glyphs with advances
   179–404; inserting the one that centres the mark took conjuncts from 0.26 to 0.45. This was
   the single largest win and it is checkable without rendering (`geomcheck.py`).

## What is still open

- **41 of 1296 conjuncts** still misplace the subscript geometrically (down from 262). They are
  listed by `python3 scratch/telugu0908/geomcheck.py`. Fixing them needs a pad finer than the
  five available stub widths, or a second subscript variant for those letters.
- **Weak head forms.** `heads.py` records the stage-`bases` score for each. మ 0.18, ఘ 0.28,
  ష 0.31, ధ 0.36, ప/ఫ 0.37, య/స 0.39. INVENTORY.md lists the untested candidate for each —
  `U+00AC` (the font's widest slot, advance 726) for మ is the most promising.
- **anusvara and visarga** sit at 0.38 / 0.31. The glyphs are right (atlas 0.76 / 0.86); the
  low cluster score is most likely metric noise from a small ring against a different
  typeface, but it has not been confirmed.
- **Not yet done:** `bmatch.py --selfcheck`, and no one who reads Telugu has looked at
  `scratch/telugu0908/out/contact.png` (200 worst clusters, reference above, output below).
  That eyeball check is the real acceptance test and it is the next thing to do.

## Rebuild / re-verify

```
python3 scratch/telugu0908/build_tables.py          # regenerate the TS tables
python3 scratch/telugu0908/geomcheck.py             # subscript placement, no rendering
node    scratch/telugu0908/verify.mjs roundtrip     # forward/reverse consistency
node    scratch/telugu0908/verify.mjs spec > /tmp/spec.json
python3 scratch/telugu0908/bmatch.py /tmp/spec.json --paired    # the gate
WORST=200 node scratch/telugu0908/verify.mjs sheet  # contact sheet for eyeballing
npx vitest run src/utils/shreeLipiTelugu0908Converter.test.ts
npx astro check && npm run build
```

Re-running a search stage (only needed if `heads.py` changes):
`python3 scratch/telugu0908/search.py {bases|cm|conj|chead|narrow|spacer}` — `cm` is the slow
one at roughly six minutes.
