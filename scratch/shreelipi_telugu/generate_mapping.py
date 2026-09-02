# Mapping derived from visual inspection of Shree-Tel-0908 font blocks
# A = 0x41 = అ
# B = 0x42 = ఆ
# C = 0x43 = ఇ
# D = 0x44 = ఈ
# E = 0x45 = ఉ
# F = 0x46 = ఊ
# G = 0x47 = ఎ
# H = 0x48 = ఏ
# I = 0x49 = ఐ
# J = 0x4a = ఒ
# K = 0x4b = ఓ
# L = 0x4c = ఔ

# Consonants (need to map these precisely)
# a = 0x61 = క
# ... etc.

mapping = {
    "అ": "A",
    "ఆ": "B",
    "ఇ": "C",
    "ఈ": "D",
    "ఉ": "E",
    "ఊ": "F",
    "ఎ": "G",
    "ఏ": "H",
    "ఐ": "I",
    "ఒ": "J",
    "ఓ": "K",
    "ఔ": "L",
    "క": "a",
    # ... fill more based on observation
}

import json
print(json.dumps(mapping, indent=2, ensure_ascii=False))
