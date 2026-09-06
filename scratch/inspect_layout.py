from fontTools.ttLib import TTFont

font = TTFont('public/SHREE-TEL-web.ttf')
cmap = font.getBestCmap()

def print_glyph(ch):
    g = cmap.get(ord(ch))
    print(f"'{ch}' ({hex(ord(ch))}): {g}")

print_glyph('¿')
print_glyph('æ')
print_glyph(' ')
print_glyph('˜')
print_glyph('˜')
print_glyph('Z')
print_glyph('f')
print_glyph('m')
print_glyph('p')
print_glyph('^')

