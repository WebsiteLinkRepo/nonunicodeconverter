from PIL import Image
img = Image.open('public/original.png')
pixels = img.load()
print("(100,100):", pixels[100,100])
print("(200,200):", pixels[200,200])
print("(300,300):", pixels[300,300])
print("(400,400):", pixels[400,400])
