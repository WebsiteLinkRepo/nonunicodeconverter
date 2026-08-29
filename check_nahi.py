from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()

# Check what Œ Ò ë map to in Unicode bytes
chars = "ŒÒë"
print("Chars:", [hex(ord(c)) for c in chars])

for c in [0x8C, 0xD2, 0xEB, 0xF08C, 0xF0D2, 0xF0EB]:
    glyph_name = cmap.get(c)
    if glyph_name:
        width = font['hmtx'][glyph_name][0]
        glyph = glyf[glyph_name]
        print(f"Char {hex(c)}: {glyph_name}, width {width}, xMin {getattr(glyph, 'xMin', '?')}, xMax {getattr(glyph, 'xMax', '?')}")
