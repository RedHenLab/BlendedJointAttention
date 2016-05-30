import cv2
import numpy as np

img = cv2.imread('Test_Images/Cube.jpg')
img1 = img

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img,127,255,0)
_, contours,hierarchy = cv2.findContours(thresh, 1, 2)

for i in range(len(contours)):
	cnt = contours[i]
	M = cv2.moments(cnt)
	# print M
	
	if(M['m00']!=0):
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])


		epsilon = 0.1*cv2.arcLength(cnt,True)
		approx = cv2.approxPolyDP(cnt,epsilon,True)
		if(len(approx)==4):
			cv2.drawContours(img1, contours[i], -1, (0,0,255), 3)

cv2.imwrite('Result_Images/Cube.jpg', img1)