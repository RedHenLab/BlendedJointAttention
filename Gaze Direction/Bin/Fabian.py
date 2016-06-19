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

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlibcascades/shape_predictor_68_face_landmarks.dat')


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
        dets = detector(frame, 1)
        for k, d in enumerate(dets):
            # Get the landmarks/parts for the face in box d.
            shape = predictor(frame, d)
            # print(type(shape.part(1).x))
            x1 = shape.part(36).x
            y1 = shape.part(37).y
            x2 = shape.part(39).x
            y2 = shape.part(40).y
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255,0,0),2)
        # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
