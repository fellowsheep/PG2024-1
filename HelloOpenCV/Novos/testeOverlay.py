import numpy as np
import cv2 as cv

# Load two images
img1 = cv.imread('baboon.jpg')
img2 = cv.imread('./Novos/eyeglasses.png',cv.IMREAD_UNCHANGED)
img3 = cv.imread('./Novos/eyeglasses.png')

b,g,r,a = cv.split(img2)

assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img3.shape
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
#img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
#ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
#mask_inv = cv.bitwise_not(mask)
mask = a
mask_inv = cv.bitwise_not(a) 

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img3,img3,mask = mask)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv.imshow('res',img1)
cv.imshow('alpha',a)
cv.waitKey(0)
cv.destroyAllWindows()