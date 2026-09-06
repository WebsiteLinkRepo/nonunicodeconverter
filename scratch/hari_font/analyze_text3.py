# Let's write a script to look through ALL characters in the Hari font and print out their visual representation (if possible)
# Or we can just build a comprehensive map based on Gujarati logic.
import requests

# We have `hari.ttf`, let's check its cmap again specifically for characters between 0x20 and 0xFF.
from fontTools.ttLib import TTFont
FONT_PATH = "/home/samuelvictor/Downloads/hari.ttf"
tt_font = TTFont(FONT_PATH)
cmap = tt_font.getBestCmap()
for c in sorted(cmap.keys()):
    if c < 256:
        name = chr(c)
        if name.isprintable():
            pass # print(f"{c:#04x} '{name}'")
        else:
            pass # print(f"{c:#04x} (non-printable)")
