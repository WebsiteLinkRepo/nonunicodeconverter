from fontTools.ttLib import TTFont

font = TTFont('public/SHREE-TEL-web.ttf')
cmap = font.getBestCmap()
print(f"Space mapped to: {cmap.get(ord(' '))}")
print(f"Cmap for M: {cmap.get(ord('M'))}")
print(f"Cmap for æ: {cmap.get(ord('æ'))}")

mtx = font['hmtx'].metrics
def advance(name):
    return mtx[name][0] if name in mtx else None

for c in [' ', 'M', 'æ', 'Q']:
    glyph_name = cmap.get(ord(c))
    if glyph_name:
        print(f"Glyph for '{c}': {glyph_name}, advance: {advance(glyph_name)}")
    else:
        print(f"No glyph for '{c}'")
