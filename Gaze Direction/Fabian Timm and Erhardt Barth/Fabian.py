#Done by intensity.py

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

#extract eye image

faceCascade1 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')
faceCascade2 = cv2.CascadeClassifier('../haarcascades/haarcascade_profileface.xml')
eyecascade1 = cv2.CascadeClassifier('../haarcascades/haarcascade_eye.xml')
eyecascade2 = cv2.CascadeClassifier('../haarcascades/haarcascade_eye_tree_eyeglasses.xml')

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:

		faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
		faces2 = faceCascade2.detectMultiScale(gray, 1.1, 5)
		# Draw a rectangle around the faces
		flag = 0
		for (x, y, w, h) in faces1:
		    eyes1 = eyecascade1.detectMultiScale(gray, 1.5, 6)
		    eyes2 = eyecascade2.detectMultiScale(gray, 1.5, 6)
		    for (x1, y1, w1, h1 ) in eyes1:
				split = frame[y1:y1+h1,x1:x1+w1]
				flag = 1

		    if flag == 0:
		        for (x2, y2, w2, h2 ) in eyes2:
					split = frame[y2:y2+h2,x2:x2+w2]
					flag = 1

		if flag == 0:
			for (x, y, w, h) in faces2:
				eyes1 = eyecascade1.detectMultiScale(gray, 1.7, 6)
				eyes2 = eyecascade2.detectMultiScale(gray, 1.7, 6)
				for (x1, y1, w1, h1 ) in eyes1:
					flag = 1
					split = frame[y1:y1+h1, x1:x1+w1]

					if flag == 0 :
						for (x2, y2, w2, h2 ) in eyes2:
							split = frame[y2:y2+h2,x2:x2+w2]
							flag = 1
if flag ==1 :
	split
	minin = 1000000
	minj=0
	mini=0
	for i in range(gray.shape[0]):
		for j in range(gray.shape[1]):
			if (gray[i][j]<minin):
				minin=gray[i][j]
				mini=i
				minj=j
				print(mini,minj)

cv2.circle(img,(mini,minj),4,(0,0,255))
cv2.imwrite('../Result_Images/eye2.jpg', img);
