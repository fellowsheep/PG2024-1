import numpy as np
import cv2 as cv

#from matplotlib import pyplot as plt #precisa instalar matplotlib

#lendo a imagem toda
img = cv.imread('baboon.jpg')

#utilizando a imagem em grayscale
imgGray = cv.imread('baboon.jpg', cv.IMREAD_GRAYSCALE)
assert imgGray is not None, "file could not be read, check with os.path.exists()"
#plt.hist(imgGray.ravel(),256,[0,256]); plt.show()

imgPikachu = cv.imread('./Novos/pikachu.png',cv.IMREAD_GRAYSCALE)
imgPikachu = cv.resize(imgPikachu, (512,512))
#plt.hist(imgPikachu.ravel(),256,[0,256]); plt.show()

#Função de blur:
imgBlurred5x5 = cv.blur(imgGray,(5,5))
imgBlurred15x15 = cv.blur(imgGray,(15,15))

imgPBlurred5x5 = cv.blur(imgPikachu,(5,5))
imgPBlurred15x15 = cv.blur(imgPikachu,(15,15))

#Detecção de bordas com o método Canny
imgBaboonCanny = cv.Canny(imgBlurred5x5,100,200)
imgPikachuCanny = cv.Canny(imgPBlurred5x5,50,100)


cv.imshow('Img grayscale:',imgGray)
cv.imshow('Baboon canny',imgBaboonCanny)
#cv.imshow('Img blur 5x5', imgBlurred5x5)
#cv.imshow('Img blur 15x15', imgBlurred15x15)

cv.imshow('Pikachu gray', imgPikachu)
cv.imshow('Pikachu canny',imgPikachuCanny)
#cv.imshow('Img Pikachu blur 5x5', imgPBlurred5x5)
#cv.imshow('Img Pikachu blur 15x15', imgPBlurred15x15)


cv.waitKey(0)
cv.destroyAllWindows()

