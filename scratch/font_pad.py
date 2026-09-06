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

for c in ['\u00FF', '\u00FC', '\u00FD', '\u00FE']:
    print(f"Pad: U+{ord(c):04X} Advance: {get_advance(c)}")

