import cv2 as cv
import sys
 
img = cv.imread('baboon.jpg')
res = img.copy()

k = 125

for i in range(img.shape[0]):  #percorre as lihas
	for j in range(img.shape[1]): #percorre as colunas
		media = img.item(i,j,0) * 0.33 + img.item(i,j,1) * 0.33 + img.item(i,j,2) * 0.33
		res.itemset((i,j,0),media) #canal azul - B
		res.itemset((i,j,1),media) #canal verde - G
		res.itemset((i,j,2),media) #canal vermelho - R
		if res.item(i,j,0) < k:
			res.itemset((i,j,0),0) #canal azul - B
			res.itemset((i,j,1),0) #canal verde - G
			res.itemset((i,j,2),0) #canal vermelho - R
		else:
			res.itemset((i,j,0),255) #canal azul - B
			res.itemset((i,j,1),255) #canal verde - G
			res.itemset((i,j,2),255) #canal vermelho - R

cv.imshow("Imagem original", img)
cv.imshow("Imagem binarizada", res)
cv.waitKey(0)