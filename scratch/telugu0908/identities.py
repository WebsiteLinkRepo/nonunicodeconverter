#!/usr/bin/env python3
"""
The identity table for Shree-Tel-0908, in plat3 codes (what a browser must receive).

HOW THESE WERE DERIVED (see INVENTORY.md for the full evidence trail)
--------------------------------------------------------------------
The font is laid out in per-consonant runs of consecutive *byte* codes:

    [full]  [base]  [base+ి]  [base+ీ]  [vattu]

`full` is a complete standalone letter; `base` is a narrow form whose ink overhangs its
advance so a talakattu can be drawn back over it; `vattu` is the subscript form (zero
advance, negative x). Not every consonant has all five.

The anchor that made this decodable: the (ి, ీ) pairs are mechanically detectable - they
sit at adjacent codes with identical advance and x-bounds and differ only in yMax. Each
such slot was then matched against all 36 `C+ి` references rendered in Chromium, which
identified the base immediately to its left. 16 bases fell out that way with no guessing.
The rest came from byte-order position within the varga sequence plus visual confirmation
on rendered sheets (scratch/telugu0908/out/*.png).

CONFIDENCE is recorded per entry so the verification pass knows where to look first.
"""

TALAKATTU = 0xE6        # normal
TALAKATTU_SHIFT = 0xE7  # sits further right; used by the ప/ఫ/ష family
TALAKATTU_RIGHT = 0xE8  # further right again
DROP = 0xAB             # the small pendant that distinguishes ధ from ద

# consonant -> forms. 'full' renders alone; 'base' needs 'tk' appended.
# 'i'/'ii' are precomposed C+ి / C+ీ. 'vattu' is the subscript form.
CONSONANTS = {
    'క':  {'base': 0x4D, 'tk': TALAKATTU, 'vattu': 0x4F, 'conf': 'high'},
    'ఖ':  {'full': 0x51, 'base': 0x52, 'tk': TALAKATTU, 'i': 0x53, 'ii': 0x54, 'vattu': 0x55, 'conf': 'high'},
    'గ':  {'base': 0x56, 'tk': TALAKATTU, 'i': 0x57, 'ii': 0x58, 'vattu': 0x59, 'conf': 'high'},
    'ఘ':  {'base': 0x153, 'tk': TALAKATTU, 'vattu': 0x5B, 'conf': 'medium'},
    'ఙ':  {'base': 0x5C, 'tk': TALAKATTU, 'vattu': 0x5D, 'conf': 'medium'},
    'చ':  {'base': 0x5E, 'tk': TALAKATTU, 'i': 0x5F, 'ii': 0x60, 'vattu': 0x61, 'conf': 'high'},
    'ఛ':  {'base': 0x62, 'tk': TALAKATTU, 'i': 0x63, 'ii': 0x64, 'vattu': 0x65, 'conf': 'high'},
    'జ':  {'full': 0x66, 'base': 0x67, 'tk': TALAKATTU, 'i': 0x68, 'ii': 0x69, 'vattu': 0x6A,
           'u': 0x6B, 'uu': 0x6C, 'conf': 'high'},
    'ఝ':  {'full': 0x6D, 'vattu': 0x6F, 'conf': 'low'},
    'ఞ':  {'base': 0x70, 'tk': TALAKATTU, 'vattu': 0x71, 'conf': 'medium'},
    'ట':  {'full': 0x72, 'base': 0x73, 'tk': TALAKATTU, 'vattu': 0x74, 'conf': 'high'},
    'ఠ':  {'base': 0x75, 'tk': TALAKATTU, 'i': 0x76, 'ii': 0x77, 'vattu': 0x78, 'conf': 'high'},
    'డ':  {'base': 0x79, 'tk': TALAKATTU, 'vattu': 0x7A, 'conf': 'high'},
    'ఢ':  {'base': 0xC9, 'tk': TALAKATTU, 'vattu': 0x7C, 'conf': 'high'},
    'ణ':  {'full': 0xD7, 'vattu': 0xD8, 'conf': 'high'},
    'త':  {'base': 0x2122, 'tk': TALAKATTU, 'i': 0x2020, 'ii': 0xA1, 'vattu': 0x161, 'conf': 'high'},
    'థ':  {'base': 0xA3, 'tk': TALAKATTU, 'i': 0xA4, 'ii': 0xA5, 'vattu': 0xA6, 'conf': 'high'},
    'ద':  {'base': 0xA7, 'tk': TALAKATTU, 'i': 0xA8, 'ii': 0xA9, 'vattu': 0xAA, 'conf': 'high'},
    'ధ':  {'prefix': DROP, 'base': 0xA7, 'tk': TALAKATTU, 'vattu': 0xAE, 'conf': 'low'},
    'న':  {'base': 0xAF, 'tk': TALAKATTU, 'i': 0xB0, 'ii': 0xB1, 'vattu': 0xB2, 'conf': 'high'},
    'ప':  {'full': 0xB3, 'base': 0xB4, 'tk': TALAKATTU_SHIFT, 'vattu': 0xB5, 'conf': 'medium'},
    'ఫ':  {'base': 0xB8, 'tk': TALAKATTU_SHIFT, 'vattu': 0xB9, 'conf': 'medium'},
    'బ':  {'full': 0xBA, 'base': 0xBB, 'tk': TALAKATTU, 'i': 0xBC, 'ii': 0xBD, 'vattu': 0xBE, 'conf': 'high'},
    'భ':  {'base': 0xBF, 'tk': TALAKATTU, 'i': 0xC0, 'ii': 0xC1, 'vattu': 0xC2, 'conf': 'high'},
    'మ':  {'full': 0x2DC, 'vattu': 0xC3, 'conf': 'medium'},
    'య':  {'base': 0xC4, 'tk': TALAKATTU, 'vattu': 0xC5, 'conf': 'high'},
    'ర':  {'base': 0xC6, 'tk': TALAKATTU, 'i': 0xC7, 'ii': 0xC8, 'vattu': 0xCA, 'conf': 'high'},
    'ల':  {'full': 0xCB, 'base': 0xCC, 'tk': TALAKATTU, 'i': 0xCD, 'ii': 0xCE, 'vattu': 0xCF, 'conf': 'high'},
    'వ':  {'base': 0xD0, 'tk': TALAKATTU, 'i': 0xD1, 'ii': 0xD2, 'vattu': 0xD3, 'conf': 'high'},
    'శ':  {'base': 0xD4, 'tk': TALAKATTU, 'i': 0xD5, 'ii': 0xD6, 'vattu': 0x2030, 'conf': 'medium'},
    'ష':  {'full': 0xD9, 'base': 0xDA, 'tk': TALAKATTU_SHIFT, 'vattu': 0xDB, 'conf': 'medium'},
    'స':  {'full': 0xDC, 'base': 0xDD, 'tk': TALAKATTU, 'vattu': 0xDE, 'conf': 'medium'},
    'హ':  {'full': 0xE0, 'base': 0xDF, 'tk': TALAKATTU, 'vattu': 0xE1, 'conf': 'medium'},
    'ళ':  {'base': 0xE2, 'tk': TALAKATTU, 'i': 0xE3, 'ii': 0xE4, 'vattu': 0xE5, 'conf': 'high'},
    'ఱ':  {'base': 0x201A, 'tk': TALAKATTU, 'vattu': 0x192, 'conf': 'medium'},
    'క్ష': {'base': 0x201E, 'tk': TALAKATTU, 'vattu': 0x3C, 'conf': 'high'},
}

VOWELS = {
    'అ': [0x41], 'ఆ': [0x42], 'ఇ': [0x43], 'ఈ': [0x44], 'ఉ': [0x45], 'ఊ': [0x46],
    'ఎ': [0x47], 'ఏ': [0x48], 'ఐ': [0x49], 'ఒ': [0x4A], 'ఓ': [0x4B], 'ఔ': [0x4C],
    # The font has no ఋ/ౠ/ఌ/ౡ glyph. బ + one or two kommus is the substitution the
    # font's own users make, confirmed by the project owner from a rendered sample.
    'ఋ': [0xBA, 0x24, 0x24], 'ౠ': [0xBA, 0x24, 0x2A],
    'ఌ': [0xCB, 0x24, 0x24], 'ౡ': [0xCB, 0x24, 0x2A],
}

# Vowel signs. A matra REPLACES the talakattu - verified: base+mark scores far better than
# base+talakattu+mark against every C+matra reference.
MATRAS = {
    'ా': [0x3E], 'ి': [0xEC], 'ీ': [0xEE], 'ు': [0x24], 'ూ': [0x2A],
    'ృ': [0x23], 'ౄ': [0x23, 0x2A],
    'ె': [0xF0], 'ే': [0xF3], 'ై': [0xF1],
    'ొ': [0xF2], 'ో': [0xF5], 'ౌ': [0xF4],
}

ANUSVARA = 0x2026   # sunna, free-standing ring
VISARGA = 0x40      # two stacked dots
POLLU = 0x152       # explicit halant, drawn above
LIGATURES = {'శ్రీ': [0x7D]}
DIGITS = {chr(0x0C66 + i): [0x30 + i] for i in range(10)}
