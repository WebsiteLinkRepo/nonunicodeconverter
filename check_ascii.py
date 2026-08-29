from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
cmap = font.getBestCmap()
glyf = font['glyf']

for c in [0xE4, 0x6A, 0xF0E4, 0xF06A, 0xC2, 0x7A, 0x4E, 0xFE, 0xBA, 0xF0C2, 0xF07A, 0xF04E, 0xF0FE, 0xF0BA]:
    glyph_name = cmap.get(c)
    if glyph_name:
        print(f"Char {hex(c)}: {glyph_name}, width {font['hmtx'][glyph_name][0]}")
