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
	    # win.clear_overlay()
	    # win.set_image(frame)

	    dets = detector(frame, 1)
	    for k, d in enumerate(dets):
	        # Get the landmarks/parts for the face in box d.
	        shape = predictor(frame, d)
	        # print(type(shape.part(1).x))
	        cv2.circle(frame,(shape.part(1).x,shape.part(1).y),2,(0,0,255))
	        