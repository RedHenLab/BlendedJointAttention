#Fabian implementation

import cv2
import numpy as np
from matplotlib import pyplot as plt
import dlib 

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

def process_eye(split):
    split = cv2.GaussianBlur(split,(5,5),0)
    split = cv2.adaptiveThreshold(split,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    split = cv2.dilate(split, None, iterations=1)
    return split

def filter_eye(split):
    split = cv2.medianBlur(split,10)
    split = cv2.bilateralFilter(split,20,75,75)
    return split

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../../dlibcascades/shape_predictor_68_face_landmarks.dat')


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
        dets = detector(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        for k, d in enumerate(dets):
            # Get the landmarks/parts for the face in box d.
            shape = predictor(frame, d)
            # print(type(shape.part(1).x))
            x1 = shape.part(36).x-4
            y1 = shape.part(37).y-10
            x2 = shape.part(39).x+4
            y2 = shape.part(40).y+10
            x3 = shape.part(42).x-4
            y3 = shape.part(43).y-10
            x4 = shape.part(45).x+4
            y4 = shape.part(46).y+10
            roi_eye1 = frame[y1:y2,x1:x2]
            roi_eye1 = process_eye(roi_eye1)
            roi_eye2 = frame[y3:y4,x3:x4]
            roi_eye2 = process_eye(roi_eye2)
            frame[y1:y2,x1:x2] = roi_eye1
            frame[y3:y4,x3:x4] = roi_eye2
        # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
