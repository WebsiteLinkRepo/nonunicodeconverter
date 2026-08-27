from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 50)

candidates = []
for i in range(32, 256):
    img = Image.new('RGB', (100, 100), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), chr(61440 + i), font=font, fill=(0, 0, 0))
    
    # Find bounding box of the black pixels
    bbox = img.getbbox() # this gets the box of non-zero (white). So we need to invert.
    img_inv = Image.eval(img, lambda x: 255 - x)
    bbox = img_inv.getbbox()
    
    if bbox:
        left, upper, right, lower = bbox
        width = right - left
        height = lower - upper
        
        # A 'u' matra usually sits low. The baseline for this font is around y=50.
        # Let's just print all characters that are very short (height < 20) and sit below y=60
        if upper > 40 and height < 30:
            candidates.append((i, bbox))

print("Candidates for below-baseline matras:")
for c in candidates:
    print(c)
