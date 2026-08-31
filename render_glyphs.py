from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.recordingPen import RecordingPen
# Actually rendering glyph paths is hard, let's just dump their bounds/advance 
# and render them using fontTools + PIL directly? 
# Maybe just render the characters themselves into an image?
# Yes, ImageFont.truetype() and draw.text()

font = ImageFont.truetype('public/AnuSM/ttf/NEOGANBO.TTF', 64)
img = Image.new('RGB', (1000, 1000), (255, 255, 255))
d = ImageDraw.Draw(img)

chars = ""
for c in range(0xF070, 0xF080):
    chars += chr(c)

d.text((10, 10), chars, font=font, fill=(0, 0, 0))
img.save('glyphs_sheet.png')                
