import sys

def generate_combos(vowels, consonants, virama, filename):
    lines = []
    # 1. Base vowels
    for v in vowels: lines.append(v)
    # 2. Base consonants
    for c in consonants: lines.append(c)
    # 3. Consonant + vowel (no virama needed for standard vowel signs in unicode, wait actually we need vowel SIGNS)
    # Actually, simpler: I'll just write a JS script that uses the Unicode ranges to generate the exact same combinations as I did for Telugu!
