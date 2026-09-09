from PIL import Image
img = Image.open('public/original.png')
pixels = img.load()
width, height = img.size
max_b = 0
min_b = 255
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if a > 0:
            bright = (r+g+b)/3
            max_b = max(max_b, bright)
            min_b = min(min_b, bright)
print(f"Max brightness: {max_b}, Min brightness: {min_b}")
