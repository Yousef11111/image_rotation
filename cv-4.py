from PIL import Image
im = Image.open("./a/bride.jpg")
print(im.format, im.size, im.mode)