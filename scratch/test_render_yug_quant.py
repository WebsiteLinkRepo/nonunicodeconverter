from PIL import Image, ImageDraw, ImageFont
import json

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 60)
font_small = ImageFont.load_default()

# Let's test words and their variations
words = [
    ("इस युग में (current)", "Bg `wJ _o§"),
    ("क्वांटम (current: ¹$m§Q>_)", "¹$m§Q>_"),
    ("क्वांटम (alt: Šdm§Q>_)", "Šdm§Q>_"),
    ("क्वांटम (alt: Šdm§Q>_)", "Šdm§Q>_"),
    ("क्वांटम (alt: Šdm§Q>_)", "Šdm§Q>_"),
    ("युग (`wJ)", "`wJ"),
    ("यु (from font)", "`w"),
]

img = Image.new('RGB', (800, len(words)*90 + 50), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, txt in words:
    draw.text((20, y+15), label, fill=(100, 100, 100))
    draw.text((350, y), txt, font=font, fill=(0, 0, 0))
    y += 80

img.save('scratch/test_render_yug_quant.png')
print('Saved scratch/test_render_yug_quant.png')
