# Head pose estimation via dlib

import cv2
import numpy as np
import dlib 

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlibcascades/shape_predictor_68_face_landmarks.dat')

while True:
    # Capture frame-by-frame
	ret, frame = video_capture.read()
	if ret:
		continue
	# Display the resulting frame
	cv2.imshow('Video', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()