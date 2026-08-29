from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/PRIYAANK.TTF')
hmtx = font['hmtx']
cmap = font.getBestCmap()
for c in [0xF04D, 0xF0A1]:
    glyph_name = cmap.get(c)
    if glyph_name:
        width = hmtx[glyph_name][0]
        print(f"Char {hex(c)}: width {width}")
