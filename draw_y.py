from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 100)
img = Image.new('RGB', (200, 200), color = (255, 255, 255))
draw = ImageDraw.Draw(img)
draw.text((50, 50), chr(61440 + 121), font=font, fill=(0, 0, 0))
img.save('draw_y.png')
