from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 50)

candidates = []
for i in range(32, 256):
    img = Image.new('RGB', (100, 100), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), chr(61440 + i), font=font, fill=(0, 0, 0))
    
    img_inv = Image.eval(img, lambda x: 255 - x)
    bbox = img_inv.getbbox()
    
    if bbox:
        left, upper, right, lower = bbox
        width = right - left
        if width > 30:
            candidates.append((i, width))

candidates.sort(key=lambda x: x[1], reverse=True)
print("Widest characters:")
for c in candidates[:20]:
    print(c)
