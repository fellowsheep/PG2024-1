import numpy as np
import cv2 as cv

#from matplotlib import pyplot as plt #precisa instalar matplotlib

#lendo a imagem toda
img = cv.imread('baboon.jpg')

#utilizando a imagem em grayscale
imgGray = cv.imread('baboon.jpg', cv.IMREAD_GRAYSCALE)

#Função de blur:
imgBlurred5x5 = cv.blur(imgGray,(5,5))
imgBlurred15x15 = cv.blur(imgGray,(15,15))
imgBaboonGaussianBlurred3x3 = cv.GaussianBlur(imgGray, (3, 3), 0)
imgBaboonGaussianBlurred5x5 = cv.GaussianBlur(img, (5, 5), 0)

imgGaussianBlurred3x3 = cv.GaussianBlur(img, (3, 3), 0)    
imgGray = cv.cvtColor(imgBaboonGaussianBlurred5x5, cv.COLOR_BGR2GRAY)

#Detecção de bordas com o método Canny
imgBaboonCanny = cv.Canny(imgGray,100,200)

#Detecção de bordas com o método Sobel
ddepth = cv.CV_16S 
scale = 1
delta = 0 

grad_x = cv.Sobel(imgGray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
grad_y = cv.Sobel(imgGray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    
    
abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)
    
    
grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

imgDilation = cv.dilate(imgBaboonCanny,(15,15),iterations = 1)
imgErosion = cv.erode(imgDilation,(3,3),iterations = 1)

cv.imshow('Img grayscale:',imgGray)
#cv.imshow('Img blur 5x5', imgBlurred5x5)
#cv.imshow('Img gaussian blur 5x5', imgBaboonGaussianBlurred5x5)
cv.imshow('Baboon canny',imgBaboonCanny)
#cv.imshow('Baboon Sobel', grad)
cv.imshow('Dilatação:',imgDilation)
cv.imshow('Erosão:',imgErosion)



cv.waitKey(0)
cv.destroyAllWindows()

