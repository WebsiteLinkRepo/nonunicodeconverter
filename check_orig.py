from PIL import Image
img = Image.open('public/original.png')
pixels = img.load()
# Check top left pixel (background) and middle pixel (arrow)
print("Background (0,0):", pixels[0,0])
print("Middle (300,300):", pixels[300,300])
