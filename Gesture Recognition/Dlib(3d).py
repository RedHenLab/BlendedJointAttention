import sys
import os
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlibcascades/shape_predictor_68_face_landmarks.dat')
win = dlib.image_window()

cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

while True:
    ret, frame = video_capture.read()
    if ret:
	    win.clear_overlay()
	    win.set_image(frame)

	    # Ask the detector to find the bounding boxes of each face. The 1 in the
	    # second argument indicates that we should upsample the image 1 time. This
	    # will make everything bigger and allow us to detect more faces.
	    dets = detector(frame, 1)
	    for k, d in enumerate(dets):
	        # Get the landmarks/parts for the face in box d.
	        shape = predictor(frame, d)
	        win.add_overlay(shape)
