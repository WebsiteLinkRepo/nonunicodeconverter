from fontTools.ttLib import TTFont
import sys

def dump(font_path):
    font = TTFont(font_path)
    cmap = font['cmap'].getBestCmap()
    if not cmap:
        print("No cmap found")
        return
    for code, name in cmap.items():
        print(f"Char: {chr(code) if code < 256 else hex(code)} (Code: {code}) -> Glyph Name: {name}")

if __name__ == '__main__':
    dump(sys.argv[1])
