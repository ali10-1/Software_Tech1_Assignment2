from PIL import Image
image = Image.open('Assets/dog.jpg')
# get one pixel
print(image.getpixel((0,0)))
# # grayscale images
red_grayscale_image = image.getchannel('R')
# blue_grayscale_image = image.getchannel('B')
red_grayscale_image.show()
# blue_grayscale_image.show()
# change the pixel color
image.putpixel((0,0), (256,42,246))
image.show()
