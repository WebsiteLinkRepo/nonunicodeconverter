import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 28)
noto_font = ImageFont.truetype(ref_font_path, 28)
label_font = ImageFont.load_default()

words = [
    # Basic words to test combos
    ("తెలుగు", "తöలðగð", "§öËðVð"),
    ("భాష", "భéషæ", "¿éÙæ"),
    ("ద్రావిడ", "దé్రవìడæ", "§é–Ñyæ"),
    ("రామ", "రéమæ", "ˆéÄæ"),
    ("కృష్ణ", "కృషæ్ణ", "a#ÙæŠ"),
    ("విజ్ఞానము", "వìజé్ఞనæమð", "Ñ\\éq¯æÄð"),
    ("యొక్క", "యùకæ్క", "ÅùaæŒ"),
]

# We will actually run the converter via JS, but for now we'll just check manually the characters.
# Wait, let's write a file that imports and calls the JS converter on these words, and we render THAT.
