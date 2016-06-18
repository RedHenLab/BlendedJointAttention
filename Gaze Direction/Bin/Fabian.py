import cv2
import sys
import numpy as np
fr = 0;
faceCascade = cv2.CascadeClassifier('../../haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../../haarcascades/haarcascade_eye.xml')
cam = cv2.VideoCapture(-11)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        gray = np.float32(gray)
        #dst = cv2.cornerHarris(gray,2,3,0.04)
        #result is dilated for marking the corners, not important
        #dst = cv2.dilate(dst,None)
        # Threshold for an optimal value, it may vary depending on the image.
        #frame[dst>0.01*dst.max()]=[0,0,255]
 
        eyes = eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
           cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    # Display the resulting frame
    frame = cv2.flip(frame,1)

    cv2.imshow('Video',frame)
    #cv2.imshow('Video', frame)
    fr = fr + 1
    print("Frame #")
    print(fr)
    print("\n")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
