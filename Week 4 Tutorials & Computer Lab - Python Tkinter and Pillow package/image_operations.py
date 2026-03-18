#image_operations.py
from PIL import Image, ImageOps
# create an image
image = Image.open('assets/insects/2_Sphaer 2021_1_2021_06_03-11-22-54-894.PNG')
# position changes
image_mirror = ImageOps.mirror(image)
image_scale = ImageOps.scale(image, 0.5)
# color changes
image_inverted = ImageOps.invert(image_mirror)
# add and remove
image_border = ImageOps.expand(
image = image_inverted,
border = 10,
fill = (255,255,255))
image_padded = ImageOps.pad(image, (1000,6000))
image_crop = ImageOps.crop(image = image, border = 200)
image_border.show()