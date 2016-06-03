import sys
import os
import dlib
import glob
from skimage import io
import cv2

cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
		detector = dlib.get_frontal_face_detector()
		predictor = dlib.shape_predictor(predictor_path)
		win = dlib.image_window()
		dets = detector(frame, 1)
		for k, d in enumerate(dets):
			shape = predictor(img, d)
	        print(shape)
        # Display the resulting frame
		cv2.imshow('Video', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
