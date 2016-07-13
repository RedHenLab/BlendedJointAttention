import cv2
import numpy as np
from matplotlib import pyplot as plt

# Defining cascade variables
faceCascade1 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')
faceCascade2 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
faceCascade3 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt.xml')

# Video capture via webcam
cam = cv2.VideoCapture('../Test/test.mp4')
cam.set(3,640)
cam.set(4,480)
video_capture = cam
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
		grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		corners = cv2.goodFeaturesToTrack(grey,900,0.01,10)
		corners = np.int0(corners)
		# print corners
		for i in corners:
			x,y = i.ravel()
			cv2.circle(frame,(x,y),1,(0,0,255),-1)

		# Display the resulting frame
		cv2.imshow('Video', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()