import cv2 as cv
import sys
 
img = cv.imread('baboon.jpg')
print(img.shape)

for i in range(img.shape[0]):  #percorre as lihas
	for j in range(img.shape[1]): #oercirre as colunas
		media = img.item(i,j,0) * 0.33 + img.item(i,j,1) * 0.33 + img.item(i,j,2) * 0.33
		img.itemset((i,j,0),media) #canal azul - B
		img.itemset((i,j,1),media) #canal verde - G
		img.itemset((i,j,2),media) #canal vermelho - R
		

cv.imshow("Display window", img)
cv.waitKey(0)