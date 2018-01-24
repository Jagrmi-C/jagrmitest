from PIL import Image, ImageFilter
im = Image.open('_FMvw5VE3pI.jpg')
im.show()
im_sharp = im.filter(ImageFilter.SHARPEN)
im_sharp.save('sharp-_FMvw5VE3pI.jpg', 'JPEG')
r, g, b = im_sharp.split()
exif_data = im._getexif()
print(exif_data)
