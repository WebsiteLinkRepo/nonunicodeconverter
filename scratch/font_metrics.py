from fontTools.ttLib import TTFont

font = TTFont('public/SHREE-TEL-web.ttf')
hmtx = font['hmtx'].metrics
cmap = font.getBestCmap()

def get_advance(char):
    codepoint = ord(char)
    if codepoint in cmap:
        glyph_name = cmap[codepoint]
        return hmtx[glyph_name][0]
    return -1

chars_to_check = [' ', 'M', '\u00e6', 'Q', 'V', '\u0153', '\u00e8']
for c in chars_to_check:
    print(f"Char: U+{ord(c):04X} '{c}' Advance: {get_advance(c)}")

