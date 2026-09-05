# Shree-Tel-0908: how every mapping was derived

Nothing in `src/utils/mappings/shreeLipiTelugu0908.ts` was typed by hand or read off a glyph
name. This file records where each value came from, and — as importantly — which values are
still weakly evidenced.

There is no competitor site to copy and no ShreeLipi software to type reference text in, so
the encoding had to be recovered from the font. Five independent channels were used; each one
is cheap, and the point of having five is that they can disagree and be arbitrated.

## The font

`public/SHREE-TEL.ttf` — Modular Infotech, "Shree-Tel-0908", version 1.10, 22 Sep 2001.
Byte-identical to the file the project owner supplied (md5 `e1c117bbab3d4e135139c7804736a3c9`).
219 glyphs, 1000 upem, no GSUB and no GPOS: rendering is literally "look each character up in
the cmap, draw it, advance by hmtx", so the *encoding* carries all the layout.

**Addressing.** The font has (0,0), (1,0) and (3,1) cmaps. Glyph names are the standard
Macintosh names assigned by position, so `numbersign` is not a `#` and nothing can be inferred
from a name. Both Chromium and Windows resolve text through **(3,1)**, so that is what the
converter emits: 217 codepoints, all in the cp1252 range. Confirmed twice over — by the
project owner's own reference output (`A`=అ … `L`=ఔ) and, independently, by the published
Kannada Shree-Lipi map in `scratch/kannada_shreelipi_repo/`, which uses the same `A`–`L` block
and the same `@` for visarga.

**Structural census** of those 217 slots (`slotinfo.py`): 166 main-line forms, 25
zero-advance marks under the baseline (subscripts), 16 zero-advance marks above it
(talakattu and the i/e/o sign family), 10 blank stubs.

**Web loading.** Chromium's OpenType Sanitiser rejects the original outright
(`post: Bad string index 5`) and falls back to a Latin face without saying so, which is why
the preview needs `public/SHREE-TEL-web.ttf` from `fixfont.py` (post 2.0 → 3.0, cmap
subtable headers recompiled; outlines, advances and both cmaps untouched).

## Channel 1 — structural filter

`hmtx` advance plus glyph bbox. A form whose ink lies entirely below the baseline can only be
a subscript; one with zero advance and ink above the x-height can only be a mark; one that
occupies its own advance is a main-line form. This alone cuts the candidate space per role by
roughly ten times and is the reason the searches below could afford to be generous.

## Channel 2 — named-glyph atlas (`atlas.py`, `notoatoms.py`, `glyphmask.py`)

Noto Serif Telugu names every atom the script needs: `katelu`, `kasubscripttelu`,
`kivoweltelu`, `ailengthmarktelu`, `nakaarapollutelu`, `tailengthmarkwidetelu`. Each Shree-Tel
glyph is rasterised with pycairo and scored against ~660 of those *labelled* single glyphs, so
a slot is identified against a named reference rather than guessed from byte order. 97k pairs,
one pass, no browser.

This settled the subscripts, the vowel signs, the marks and the digits. Representative
top-1 results: `U+0040 → visargatelu 0.86`, `U+0152 → viramatelu 0.74`,
`U+003E → aavowelsigntelu 0.86`, `U+00A2 → tasubscripttelu 0.80`,
`U+0078 → tthasubscripttelu 0.78`, `U+00CF → lasubscripttelu 0.77`,
`U+201D → rephtelu 0.81`, `U+201C → nakaarapollutelu 0.62`.

What it cannot do: a Shree-Lipi `base` is a letter with its talakattu removed and no Unicode
font contains such a partial shape, so bases score low and ambiguously there.

## Channel 3 — run structure

The font lays each consonant out as a contiguous run in varga order:

    [full]  base  [base+ి]  [base+ీ]  vattu     e.g. ఖ = 0051 0052 0053 0054 0055

Because channel 2 pins the vattu, the vattu anchors the rest of its own run. This is what
arbitrated the two false friends: `U+00CA` matches Noto's `్ఱ` best but sits at ర's run
position, and Telugu ్ర and ్ఱ are near-identical shapes, so position decides.

The extension region (bytes 0x7D upward, where cp1252 puts its typographic punctuation)
continues the same varga order from త onward, with the overflow forms — ఱ, క్ష, మ, ఘ, the
pollu variants, the vowel-sign width variants — filling the gaps.

## Channel 4 — cluster search against shaped Unicode (`search.py`, `bmatch.py`)

Candidates are rendered once in Chromium and scored against every reference, so 600 candidate
cells plus 37 reference cells give the whole 36 × 600 matrix in two screenshots. That economy
is what let the search stay generous instead of hand-narrowed.

Stage `bases` — every main-line slot alone and with each of the three talakattu hooks, scored
against the bare consonant. This produced the talakattu assignment, and it reproduced Telugu
orthography without being told it: for ఖ ఙ జ ఝ ఞ ట ణ బ ఱ ల హ మ the bare slot beat every
hooked variant, and those are exactly the Telugu consonants that carry their own top.

Stage `cm` — C + vowel sign, 468 references against a structurally generated candidate space
(precomposed glyph where the font has one; otherwise base or full plus each width variant of
the sign; plus the two-piece spellings Modular Infotech's Kannada layout uses for ొ ో ౌ ై).
Ranking is constrained to the candidates spelled for that same pair, because an unconstrained
ranking lets a candidate labelled for a different sign win on shape alone.

Two things this stage discovered that the first attempt had wrong:

* **Head form depends on where the sign sits.** A sign drawn above the letter takes the
  talakattu's place and follows the narrow `base`; ు ూ ృ ౄ hang below, leave the top alone and
  follow the complete form. Offering both and measuring lifted ు from 0.32 to 0.35 and ూ from
  0.29 to 0.38.
* **ై is two pieces**, the ె mark plus a hook under the letter — which is how Noto spells its
  own ై (`aivowelsigntelu` spans y −309…681; `ailengthmarktelu` is the −309…−70 part alone).
  Adding the hook lifted ై from 0.27 to 0.43, and the hook it picks, `U+004F`, is the slot the
  atlas had matched to `ailengthmarktelu` at 0.88. That in turn moved క's subscript to the
  next slot along, `U+0050`.

## Channel 5 — differential rendering (`dsearch.py`)

Subtracting the carrier isolates what a candidate *adds*: `ink(H+S) − ink(H)` against
`ink(C1 ్ C2) − ink(C1)`. Cells are rendered left-aligned at a fixed baseline (`ALIGN=left`
in `refsheet.mjs`) so the masks share a frame — with the default centred layout, adding a mark
shifts the base sideways and the subtraction leaves ghost outlines instead of the mark.

Useful for marks that stand clear of the letter (ృ 0.50, ై 0.41, ౌ 0.46). Not useful for signs
that overlap the letter's strokes, because the subtraction then keeps only the
non-overlapping sliver and the sliver differs between typefaces more than the marks do. The
plain cluster search is the better instrument there, and that is what the shipped tables use.

Its `width` stage answered a question worth recording: `base + ి-variant` does **not**
reproduce the font's own precomposed `C+ి` glyph (same-font IoU only 0.2–0.55), so the
precomposed forms are separately drawn designs with a lower i-mark, not compositions. The
converter therefore prefers them whenever the cluster has no intervening subscript.

## Confidence

`heads.py` records the stage-`bases` score of every chosen head form. Solid (≥ 0.53):
క ఖ గ ఙ చ జ ఝ ఞ ఠ డ ఢ ణ త థ ద న బ భ ర ఱ ల ళ శ హ. Weak, and the first place to look if
something renders wrongly:

| letter | score | note |
|---|---|---|
| మ | 0.18 | no slot matches; `U+00AC` (advance 726, the widest in the font) is the untested candidate |
| ఘ | 0.28 | `U+0153` by elimination; `U+005A`/`U+005B` are the run-position alternatives |
| ష | 0.31 | run position is unambiguous, the measurement is not |
| ధ | 0.36 | modelled as ద plus the `U+00AB` pendant, the only slot shaped like one |
| ప, ఫ | 0.37 | run positions `00B3`/`00B4` and `00B8`; ప ఫ ష స all resemble each other across typefaces |
| య | 0.39 | run position `00C4`, takes the right-shifted hook |
| స | 0.39 | run position `00DD` |
| క్ష | 0.48 | `U+201E` |

## Gaps the font genuinely has

* **ఋ ౠ ఌ ౡ** — no glyph. Emitted as బ / ల plus one or two kommus, which is the substitution
  the font's own users make; the project owner confirmed it renders as intended and asked for
  no warning.
* **ఁ arasunna, ఀ candrabindu** — no glyph. The sunna is emitted and the character is
  reported as unmapped.
* **఼ nukta** — no glyph, dropped and reported.
* **్ర vs ్ఱ** — near-identical shapes; `U+00CA` is assigned to ్ర on run position, and ఱ's
  subscript to `U+005B`.
