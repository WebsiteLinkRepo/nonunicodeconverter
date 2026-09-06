#!/usr/bin/env python3
"""
Head forms: the glyph string that carries a consonant, and the subscript it contributes.

Derived, not guessed. Each consonant's `vattu` was identified by atlas.py (single-glyph
shape match against Noto's named `<C>subscripttelu`), and the font lays each consonant out
as a contiguous run `[full] base [C+ి] [C+ీ] vattu`, so the vattu anchors the rest of the
run. `head` is then confirmed by search.py stage 1, which renders every main-line slot
alone and with each of the three talakattu hooks and scores it against the bare consonant.

`tk` records which hook the letter takes, or '' for the twelve Telugu consonants that carry
their own top and take none (ఖ ఙ జ ఝ ఞ ట ణ బ ఱ ల హ మ) - a distinction the measurements
reproduce independently: for those letters the bare slot beats every hooked variant.

`conf` is the stage-1 score of the chosen head form. Anything below 0.45 is flagged in
PROGRESS.md as needing a targeted re-search rather than quietly shipped as certain.
"""

#: consonant -> (head slot, talakattu slot or '', narrow base slot or '', stage-1 score)
HEAD = {
    'క':   (0x004D, 0x00E6, None,   0.72),
    'ఖ':   (0x0051, None,   0x0052, 0.61),
    'గ':   (0x0056, 0x00E6, None,   0.56),
    'ఘ':   (0x0153, 0x00E8, None,   0.28),
    'ఙ':   (0x005C, None,   None,   0.54),
    'చ':   (0x005E, 0x00E6, None,   0.55),
    'ఛ':   (0x0062, 0x00E6, None,   0.48),
    'జ':   (0x0066, None,   0x0067, 0.67),
    'ఝ':   (0x006D, None,   None,   0.61),
    'ఞ':   (0x0070, None,   None,   0.53),
    'ట':   (0x0072, None,   0x0073, 0.48),
    'ఠ':   (0x0075, 0x00E6, None,   0.73),
    'డ':   (0x0079, 0x00E6, None,   0.64),
    'ఢ':   (0x00C9, 0x00E6, None,   0.68),
    'ణ':   (0x00D7, None,   None,   0.68),
    'త':   (0x2122, 0x00E6, None,   0.65),
    'థ':   (0x00A3, 0x00E6, None,   0.73),
    'ద':   (0x00A7, 0x00E6, None,   0.72),
    'ధ':   (0x00A7, 0x00E6, None,   0.36),   # + the 0x00AB pendant; see PENDANT
    'న':   (0x00AF, 0x00E8, None,   0.60),
    'ప':   (0x00B3, None,   0x00B4, 0.37),
    'ఫ':   (0x00B8, None,   None,   0.37),
    'బ':   (0x00BA, None,   0x00BB, 0.73),
    'భ':   (0x00BF, 0x00E6, None,   0.63),
    'మ':   (0x00AC, 0x00E6, None,   1.00),   # owner-confirmed
    'య':   (0x00C4, 0x00E7, None,   0.39),
    'ర':   (0x00C6, 0x00E6, None,   0.73),
    'ఱ':   (0x201A, None,   None,   0.65),
    'ల':   (0x00CB, None,   0x00CC, 0.64),
    'ళ':   (0x00E2, 0x00E6, None,   0.53),
    'వ':   (0x00D0, 0x00E8, None,   0.50),
    'శ':   (0x00D4, 0x00E6, None,   0.59),
    'ష':   (0x00D9, None,   0x00DA, 0.31),
    'స':   (0x00DC, None,   0x00DD, 0.39),
    'హ':   (0x00E0, None,   0x00DF, 0.54),
    'క్ష': (0x201E, 0x00E6, None,   0.48),
}

#: consonant -> subscript slot. atlas.py single-glyph scores, run order arbitrating the two
#: Two false friends, both settled on structure rather than shape, because the shapes really
#: are near-identical: U+00CA matches Noto's ్ఱ best but sits at ర's run position, and Telugu
#: ్ర and ్ఱ differ by a hairline. U+004F and U+2022 both match Noto's ai hook at 0.88 and are
#: both small hooks under the letter; U+004F sits at క's run position and U+2022 sits in the
#: extras block beside the pollu forms, so U+004F is ్క and U+2022 is the hook. The cluster
#: search prefers U+004F as the hook by a hair, but it is choosing between two shapes it
#: cannot tell apart, and U+0050 - the only other candidate for ్క - has a 379-unit advance,
#: so it would push the next letter aside instead of tucking under this one.
VATTU = {
    'క': 0x004F, 'ఖ': 0x0055, 'గ': 0x0059, 'ఘ': 0x0192, 'ఙ': 0x005D, 'చ': 0x0061,
    'ఛ': 0x0065, 'జ': 0x006A, 'ఝ': 0x2030, 'ఞ': 0x0071, 'ట': 0x0074, 'ఠ': 0x0078,
    'డ': 0x007A, 'ఢ': 0x007C, 'ణ': 0x007E, 'త': 0x00A2, 'థ': 0x00A6, 'ద': 0x00AA,
    'ధ': 0x00AE, 'న': 0x00B2, 'ప': 0x00B5, 'ఫ': 0x00B9, 'బ': 0x00BE, 'భ': 0x00C2,
    'మ': 0x00C3, 'య': 0x00C5, 'ర': 0x00CA, 'ఱ': 0x005B, 'ల': 0x00CF, 'ళ': 0x00E5,
    'వ': 0x00D3, 'శ': 0x00D8, 'ష': 0x00DB, 'స': 0x00DE, 'హ': 0x00E1, 'క్ష': 0x003C,
}

#: Precomposed C + ి and C + ీ, at run positions base+1 and base+2 where the font has them.
#: atlas.py matched these directly against Noto's `<C>ivoweltelu` / `<C>iivoweltelu`.
PRECOMP_I = {
    'ఖ': (0x0053, 0x0054), 'గ': (0x0057, 0x0058), 'చ': (0x005F, 0x0060),
    'ఛ': (0x0063, 0x0064), 'జ': (0x0068, 0x0069), 'ఠ': (0x0076, 0x0077),
    'త': (0x2020, 0x00A1), 'థ': (0x00A4, 0x00A5), 'ద': (0x00A8, 0x00A9),
    'న': (0x00B0, 0x00B1), 'బ': (0x00BC, 0x00BD), 'భ': (0x00C0, 0x00C1),
    'ర': (0x00C7, 0x00C8), 'ల': (0x00CD, 0x00CE), 'వ': (0x00D1, 0x00D2),
    'శ': (0x00D5, 0x00D6), 'ళ': (0x00E3, 0x00E4),
}

#: Precomposed C + ు / C + ూ. Only జ has them (run positions after its vattu).
PRECOMP_U = {'జ': (0x006B, 0x006C)}

#: The pendant that distinguishes ధ from ద: a zero-advance mark at positive x below the
#: baseline (U+00AB, bbox 214,-96,281,57), the only slot shaped that way.
PENDANT = 0x00AB

#: Marks. ANUSVARA/VISARGA confirmed against the user's own reference output (అం = A…,
#: అః = A@); POLLU and the two alternates matched Noto's `viramatelu` at 0.74-0.76.
ANUSVARA = 0x2026
VISARGA = 0x0040
POLLU = 0x0152
POLLU_ALT = (0x0160, 0x2039)
NAKAARA_POLLU = 0x201C      # న్ as one glyph, Noto `nakaarapollutelu` 0.62
REPH = 0x201D               # ర్ as one glyph, Noto `rephtelu` 0.81
AI_LENGTH = 0x2022          # Noto `ailengthmarktelu` 0.88; see INVENTORY.md on why not U+004F
TA_RA = 0x02C6              # త్ర as one glyph, Noto `tarasubscripttelu` 0.72

#: Independent vowels, confirmed against the user's reference output A-L.
VOWELS = {
    'అ': [0x41], 'ఆ': [0x42], 'ఇ': [0x43], 'ఈ': [0x44], 'ఉ': [0x45], 'ఊ': [0x46],
    'ఎ': [0x47], 'ఏ': [0x48], 'ఐ': [0x49], 'ఒ': [0x4A], 'ఓ': [0x4B], 'ఔ': [0x4C],
    # No glyph exists; బ / ల + one or two kommus is the substitution, which the user
    # confirmed renders as intended and asked not to warn about.
    'ఋ': [0xBA, 0x24, 0x24], 'ౠ': [0xBA, 0x24, 0x2A],
    'ఌ': [0xCB, 0x24, 0x24], 'ౡ': [0xCB, 0x24, 0x2A],
}

#: Candidate width variants of each vowel sign, from atlas.py. Which one a given consonant
#: takes is decided per (consonant, matra) by dsearch.py - that is the table the real
#: Shree-Lipi keyboard driver carried, and modelling one variant per matra is what made the
#: previous attempt score 0.21-0.35 on ై ొ ో ౌ.
MATRA_VARIANTS = {
    'ా': [0x003E, 0x00E9, 0x00EA, 0x00EB, 0x00FB],
    'ి': [0x00EC, 0x00ED],
    'ీ': [0x00EE, 0x00EF],
    'ు': [0x0024],
    'ూ': [0x002A],
    'ృ': [0x2013, 0x0023],
    'ౄ': [0x2014, 0x0023],
    'ె': [0x00F0, 0x00F1, 0x00F2],
    'ే': [0x00F3, 0x00F4, 0x00F5],
    'ై': [0x00F0, 0x00F1, 0x00F2],          # ె variant + a below-baseline hook
    'ొ': [0x0026, 0x00F6, 0x00F7, 0x0178],
    'ో': [0x005A, 0x00F8, 0x00F9],
    'ౌ': [0x006F, 0x00FA],
}

DIGITS = {chr(0x0C66 + i): [0x30 + i] for i in range(10)}
LIGATURES = {'శ్రీ': [0x7D]}


def head(c, with_matra=False):
    """The glyph string for consonant `c`. With a matra following, the narrow base form is
    used where the font provides one and the talakattu is dropped, because the vowel sign
    occupies the same space."""
    h, tk, narrow, _ = HEAD[c]
    pre = [PENDANT] if c == 'ధ' else []
    if with_matra:
        return pre + [narrow if narrow else h]
    return pre + ([h] if not tk else [h, tk])


# --------------------------------------------------------------------------- conjunct pad

#: Advance-only glyphs: the outline is a 5x5 stub, so they draw nothing and only move the pen.
#: The font has nine, but four are unusable in output: 0x0020 is a real space (it would break
#: word wrapping and word counts), 0x00A0 is a no-break space that the app's own paste
#: sanitiser rewrites to a space, and 0x0090 / 0x00AD are a C1 control and a soft hyphen,
#: neither of which survives a trip through Word or RTF intact. That leaves five printable
#: cp1252 characters with advances 179, 200, 205, 242 and 404.
STUBS = (0x00FC, 0x00FD, 0x00FF, 0x00FE, 0x203A)


def _geom(seq, slots):
    pen, x0, x1 = 0, 1e9, -1e9
    for cp in seq:
        v = slots[cp]
        if v['bbox']:
            x0 = min(x0, pen + v['bbox'][0])
            x1 = max(x1, pen + v['bbox'][2])
        pen += v['adv']
    return pen, x0, x1


def pad_for(c, sub, slots):
    """The stub that best centres THIS subscript under THIS letter.

    The per-letter default (`conjunct_pad`) uses the average subscript, which is right for most
    pairs but wrong where a mark's own x range is unusual - the marks run from x -599..-21 for
    ్ఘ to 214..281 for the ధ pendant, so one pad cannot serve all of them."""
    pen, bx0, bx1 = _geom(head(c), slots)
    b = slots[sub]['bbox']
    if b is None or slots[sub]['class'] != 'below':
        return None
    mid = (b[0] + b[2]) / 2
    target = (bx0 + bx1) / 2
    options = [(abs(pen + mid - target), None)]
    options += [(abs(pen + slots[sp]['adv'] + mid - target), sp) for sp in STUBS]
    return min(options)[1]


def pollu_for(c, slots):
    """Which of the three pollu marks sits over this letter.

    U+0152, U+0160 and U+2039 are the same mark at three x offsets (-87..255, -158..176 and
    0..304), which is the font's usual way of width-matching a mark to a letter. Pick the one
    whose ink centres on the letter's."""
    pen, bx0, bx1 = _geom(head(c), slots)
    target = (bx0 + bx1) / 2
    best = None
    for cp in (POLLU,) + POLLU_ALT:
        b = slots[cp]['bbox']
        d = abs(pen + (b[0] + b[2]) / 2 - target)
        if best is None or d < best[0]:
            best = (d, cp)
    return best[1]


def conjunct_pad(c, slots):
    """The stub glyph to emit between a letter and a subscript, or None.

    A subscript is a zero-advance mark whose ink sits at roughly x -450..-60, so it needs the
    pen about 450 units in to land under the letter. A narrow letter plus its talakattu only
    reaches ~220, and without the pad the mark is drawn beside the letter instead of beneath
    it - 262 of the 1296 pairs, which `geomcheck.py` lists. The pad is chosen so the mark's
    centre lands on the centre of the letter's ink, and measured: inserting it lifts క్ఖ from
    0.30 to 0.66 and క్గ to 0.62 against the shaped Unicode reference.
    """
    pen, bx0, bx1 = _geom(head(c), slots)
    marks = [slots[v]['bbox'] for v in VATTU.values()
             if slots[v]['class'] == 'below' and slots[v]['bbox']]
    mid = sum((b[0] + b[2]) / 2 for b in marks) / len(marks)
    target = (bx0 + bx1) / 2                  # where the mark's centre should land
    options = [(abs(pen + mid - target), None)]
    options += [(abs(pen + slots[sp]['adv'] + mid - target), sp) for sp in STUBS]
    return min(options)[1]
