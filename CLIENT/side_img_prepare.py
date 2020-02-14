import cv2
import os
import sys

img = cv2.imread(sys.argv[1])
for i in range(len(img)):
	for j in range(len(img[i])):
		for z in range(len(img[i][j])):
			if img[i][j][z] >= 105:
				img[i][j][z] = 255
			else:
				img[i][j][z] = 0

cv2.imwrite('images/img.jpg', img)
