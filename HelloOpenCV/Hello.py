import cv2 as cv
import sys
 
img = cv.imread('baboon.jpg')

cv.imshow("Display window", img)
cv.waitKey(0)