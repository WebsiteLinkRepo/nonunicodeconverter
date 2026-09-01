import fontTools.ttLib as ttLib
from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)

# Render isolated words from the screenshots
# 1. युग
# 2. त्र्यं
# 3. भस्म
# 4. मृत्युंजय

tests = [
    ("युग", "`wJ"),
    ("त्र्यं", "Í`§"),
    ("भस्म", "^ñ_"),
    ("मृत्युंजय", "_hm_¥Ë`w§O`"),
    ("य", "`"),
    ("म", "_"),
    ("स", "g"),
    ("स्म", "ñ_"),
    ("भ", "^"),
    ("य", "`"),
]

for name, enc in tests:
    img = Image.new('RGB', (300, 200), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((50, 60), enc, font=font, fill=(0, 0, 0))
    # sanitize filename
    fn = name.replace(" ", "_")
    img.save(f"scratch/test_render_{fn}.png")

print("Rendered all test images")
