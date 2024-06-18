import cv2 as cv
import sys
 
img = cv.imread('baboon.jpg')
img2 = img.copy()
img3 = img.copy()
imgR = img.copy()
imgG = img.copy()
imgB = img.copy()
img4 = img.copy()
img5 = img.copy()

cor = [255, 0, 255] #magenta

print(img.shape)

for i in range(img.shape[0]):  #percorre as lihas
	for j in range(img.shape[1]): #percorre as colunas
		media = img.item(i,j,0) * 0.33 + img.item(i,j,1) * 0.33 + img.item(i,j,2) * 0.33
		mediaPond = img.item(i,j,0) * 0.07 + img.item(i,j,1) * 0.71 + img.item(i,j,2) * 0.21
		
		img2.itemset((i,j,0),media) #canal azul - B
		img2.itemset((i,j,1),media) #canal verde - G
		img2.itemset((i,j,2),media) #canal vermelho - R
		
		img3.itemset((i,j,0),mediaPond) #canal azul - B
		img3.itemset((i,j,1),mediaPond) #canal verde - G
		img3.itemset((i,j,2),mediaPond) #canal vermelho - R

		imgR.itemset((i,j,0),img.item(i,j,2)) #canal azul - B
		imgR.itemset((i,j,1),img.item(i,j,2)) #canal verde - G
		imgR.itemset((i,j,2),img.item(i,j,2)) #canal vermelho - R

		imgG.itemset((i,j,0),img.item(i,j,1)) #canal azul - B
		imgG.itemset((i,j,1),img.item(i,j,1)) #canal verde - G
		imgG.itemset((i,j,2),img.item(i,j,1)) #canal vermelho - R

		imgB.itemset((i,j,0),img.item(i,j,0)) #canal azul - B
		imgB.itemset((i,j,1),img.item(i,j,0)) #canal verde - G
		imgB.itemset((i,j,2),img.item(i,j,0)) #canal vermelho - R

		img4.itemset((i,j,0),img.item(i,j,0) | cor[0]) #canal azul
		img4.itemset((i,j,1),img.item(i,j,1) | cor[1]) #canal verde
		img4.itemset((i,j,2),img.item(i,j,2) | cor[2]) #canal vermelho

		img5.itemset((i,j,0),img.item(i,j,0) ^ 255)
		img5.itemset((i,j,1),img.item(i,j,1) ^ 255)
		img5.itemset((i,j,2),img.item(i,j,2) ^ 255)

cv.imshow('Imagem Original', img)
#cv.imshow('Imagem em Grayscale - média aritmética',img2)
#cv.imshow('Imagem em Grayscale - média ponderada',img3)
#cv.imshow('Canal R',imgR)
#cv.imshow('Canal G',imgG)
#cv.imshow('Canal B',imgB)
# cv.imshow('Filtro colorizacao',img4)
cv.imshow('Filtro negativo',img5)

cv.waitKey(0)