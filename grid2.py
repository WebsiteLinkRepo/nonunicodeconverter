from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 30)

cols = 16
rows = 8
cell_size = 60
img = Image.new('RGB', (cols * cell_size, rows * cell_size), color='white')
draw = ImageDraw.Draw(img)

for i in range(128, 256):
    row = (i - 128) // cols
    col = (i - 128) % cols
    x = col * cell_size
    y = row * cell_size
    
    draw.rectangle([x, y, x + cell_size, y + cell_size], outline='gray')
    draw.text((x + 2, y + 2), str(i), fill='blue')
    
    draw.text((x + 10, y + 20), chr(61440 + i), font=font, fill='black')

img.save('grid2.png')
