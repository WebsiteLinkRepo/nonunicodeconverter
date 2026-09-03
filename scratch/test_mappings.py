#!/usr/bin/env python3
"""
Test different mapping candidates for broken Telugu consonants.
Based on identify/sweep results, pick the best single-glyph or composition.
"""
import sys
sys.path.insert(0, 'scratch')
from telugu_verify import verify

# Test the top candidates from identify/sweep results
CANDIDATES = {
    'ఘ': [
        ('6D', 0x6D, 'single 0x6D'),
        ('C4', 0xC4, 'single 0xC4'),
    ],
    'ఛ': [
        ('62+E6', (0x62, 0xE6), 'base 0x62 + E6'),
        ('A3+E6', (0xA3, 0xE6), 'base 0xA3 + E6'),
    ],
    'జ': [
        ('67', 0x67, 'single 0x67 - WINNER'),
        ('66', 0x66, 'single 0x66'),
    ],
    'ధ': [
        ('A3+E6', (0xA3, 0xE6), 'base 0xA3 + E6'),
        ('C9+E6', (0xC9, 0xE6), 'base 0xC9 + E6'),
    ],
    'న': [
        ('AF+E6', (0xAF, 0xE6), 'base 0xAF + E6'),
        ('D1', 0xD1, 'single 0xD1'),
        ('B0', 0xB0, 'single 0xB0'),
    ],
    'ప': [
        ('D1', 0xD1, 'single 0xD1'),
        ('B0', 0xB0, 'single 0xB0'),
        ('B2', 0xB2, 'single 0xB2 - ORIGINAL'),
    ],
    'ఫ': [
        ('52', 0x52, 'single 0x52'),
        ('B8', 0xB8, 'single 0xB8 - ORIGINAL'),
    ],
    'మ': [
        ('60', 0x60, 'single 0x60'),
        ('C4', 0xC4, 'single 0xC4 - ORIGINAL'),
    ],
    'య': [
        ('6D', 0x6D, 'single 0x6D'),
        ('C5', 0xC5, 'single 0xC5 - ORIGINAL'),
    ],
    'వ': [
        ('D1', 0xD1, 'single 0xD1'),
        ('A8', 0xA8, 'single 0xA8'),
        ('D0', 0xD0, 'single 0xD0 - ORIGINAL'),
    ],
    'ష': [
        ('DA', 0xDA, 'single 0xDA'),
        ('D9', 0xD9, 'single 0xD9'),
    ],
    'స': [
        ('B0', 0xB0, 'single 0xB0'),
        ('DC', 0xDC, 'single 0xDC - ORIGINAL'),
    ],
}

def code_to_str(code):
    """Convert code (int or tuple) to string."""
    if isinstance(code, int):
        return chr(code)
    return ''.join(chr(c) for c in code)

print("Testing all candidates for each broken consonant...")
for letter, cands in CANDIDATES.items():
    print(f"\n{letter}:")
    for name, code, desc in cands:
        s = code_to_str(code)
        # verify returns list of (target, output, score) tuples that fail
        bad = verify([letter], name=f"test_{letter}_{name}", threshold=0.45)
        if not bad:
            print(f"  ✓ {name:12s} {desc:30s} PASS")
        else:
            score = bad[0][2]
            print(f"  ✗ {name:12s} {desc:30s} score={score:.3f}")
