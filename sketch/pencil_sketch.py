# load library
import cv2

# load image
filename = 'images/tony2.jpg'

# read image
img = cv2.imread(filename)

# convert to gray scale
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the image
inverted_gray_image = 255-gray_scale

# blur the image by gaussian function
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

# invert blurred image
inverted_blurred = 255-blurred_img

# create pencil sketch
pencil_sketch = cv2.divide(gray_scale, inverted_gray_image, scale=256.0)

cv2.imshow('original image', img)
cv2.imshow('new image', pencil_sketch)
cv2.waitKey(0)
