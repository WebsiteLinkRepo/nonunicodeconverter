from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
font = TTFont(font_path)
cmap = font.getBestCmap()

# Print all glyphs with code, hex, char representation
for code, name in sorted(cmap.items()):
    try:
        ch = chr(code)
    except:
        ch = '?'
    print(f"{code:5d}  0x{code:04X}  {name:25s}  {repr(ch)}")
