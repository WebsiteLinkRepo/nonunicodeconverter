import json

# Your mapping
OUR_MAPPING = {
  'అ': 'A', 'ఆ': 'B', 'ఇ': 'C', 'ఈ': 'D',
  'ఉ': 'E', 'ఊ': 'F', 'ఋ': 'ƒ', 'ఎ': 'G',
  'ఏ': 'H', 'ఐ': 'I', 'ఒ': 'J', 'ఓ': 'K', 'ఔ': 'L'
}

# The image shows: 
# అ(A) ఆ(B) ఇ(C) ఈ(D) ఉ(E) ఊ(F) ఋ(0x0192 / ƒ) ౠ(0x0192+matra? or something else?) ఎ ఏ ఐ ఒ ఓ ఔ
# 
# But in the competitor screenshot file:///home/samuelvictor/Pictures/Screenshots/Screenshot_20260902_200038.png:
# ఋ is ఋ (looks like 0x0192, ƒ)
# ౠ is ౠ (looks like 0x0192 + 0x0152?)
# ఎ is G (ఎ)
# ఏ is H (ఏ)
# ఐ is I (ఐ)
# ఒ is J (ఒ) 
# ఓ is K (ఓ)
# ఔ is L (ఔ)
