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
        height = lower - upper
        
        # A bindu sits HIGH (upper < 40) and is very small (width < 20, height < 20)
        if upper < 30 and height < 20 and width < 20:
            candidates.append((i, bbox))

print("Candidates for bindu:")
for c in candidates:
    print(c)
