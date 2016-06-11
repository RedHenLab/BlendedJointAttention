import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture('test.mp4')
video_capture = cap
cv2.ocl.setUseOpenCL(False)
fgbg = cv2.createBackgroundSubtractorMOG2()
time = datetime.datetime.now().time()
print time
while(1):
    ret, frame = video_capture.read()
    fgmask = fgbg.apply(frame)
    print(fgmask.shape)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()