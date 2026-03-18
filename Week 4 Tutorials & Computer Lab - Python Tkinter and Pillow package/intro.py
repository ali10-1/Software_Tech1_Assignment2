
#intro.py
from PIL import Image
# create an image via import
image = Image.open('Assets/Cat.JPG')
# analyze the image
print(image.size)
print(image.filename)
print(image.format)
# # flip the image
image = image.transpose(Image.Transpose.ROTATE_90)
# # show the image
image.show()
# exercise
