import fontTools.ttLib as ttLib

font = ttLib.TTFont('public/AnuSM main/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()

# Reverse cmap to find codepoint for each glyph
rev_cmap = {}
for cp, name in cmap.items():
    rev_cmap[name] = cp

print("Number of glyphs:", len(font.getGlyphOrder()))

# Print all glyphs with their names and PUA/Unicode codepoints
for name in font.getGlyphOrder():
    cp = rev_cmap.get(name)
    cp_str = f"{hex(cp)} ({chr(cp) if cp and cp < 128 else ' '})" if cp else "NO_CP"
    contours = glyf[name].numberOfContours if name in glyf else 0
    print(f"Glyph: {name:20s} | CP: {cp_str:15s} | Contours: {contours}")
