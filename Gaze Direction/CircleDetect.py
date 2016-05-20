import cv2
import sys
import numpy as np

frame = cv2.imread('Test_Images/Test1.jpg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
split = cv2.Canny(frame,100,200)
circles = cv2.HoughCircles(split,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
	cv2.circle(split,(i[0],i[1]),i[2],(0,255,0),2)
	cv2.circle(split,(i[0],i[1]),2,(0,0,255),3)
	cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
	cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
	print(i)
cv2.imwrite('Result_Images/Result3.jpg', split)
cv2.imwrite('Result_Images/Result1.jpg', frame);