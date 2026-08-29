from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/PRIYAANK.TTF')
hmtx = font['hmtx']
cmap = font.getBestCmap()

chars_to_check = [0xF04E, 0xF0A2, 0xF0FE, 0xF0E7, 0xF079, 0xF0EE]
for c in chars_to_check:
    glyph_name = cmap.get(c)
    if glyph_name:
        width = hmtx[glyph_name][0]
        print(f"Char {hex(c)}: width {width}")
    else:
        print(f"Char {hex(c)} not in cmap")
