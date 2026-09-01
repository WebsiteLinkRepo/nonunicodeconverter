from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"

# Let's render at high resolution and at small sizes (16, 20, 24, 32, 48)
words = [
    ("भस्म", "^ñ_"),
    ("विमूढ़", "{d_y‹T>"),
    ("महा", "_hm"),
    ("हमारे", "h_mao"),
    ("मात्रा", "_mÌm"),
    ("युग", "`wJ"),
    ("युद्ध", "`wÕ"),
    ("महामृत्युंजय", "_hm_¥Ë`w§O`"),
]

for size in [20, 24, 32, 48]:
    font = ImageFont.truetype(font_path, size)
    img = Image.new('RGB', (800, len(words) * (size + 15) + 30), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    y = 15
    for hindi, shree in words:
        draw.text((20, y), f"{hindi}:", fill=(120, 120, 120))
        draw.text((200, y), shree, font=font, fill=(0, 0, 0))
        y += size + 15

    img.save(f"scratch/current_render_{size}.png")
    print(f"Saved scratch/current_render_{size}.png")
