import cv2
import sys
import numpy as np

frame = cv2.imread('Test_Images/Test1.jpg')
frame = cv2.medianBlur(frame,5)
split = cv2.Canny(frame,100,200)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(split,cv2.HOUGH_GRADIENT,1.04,100)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
	cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
	cv2.circle(gray,(i[0],i[1]),2,(0,0,255),3)
	print(i)
cv2.imwrite('Result_Images/Result3.jpg', gray)
cv2.imwrite('Result_Images/Result1.jpg', split);