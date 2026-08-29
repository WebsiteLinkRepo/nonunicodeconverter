from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/PRIYAANK.TTF')
if 'kern' in font:
    print("Has kern table!")
else:
    print("No kern table.")
