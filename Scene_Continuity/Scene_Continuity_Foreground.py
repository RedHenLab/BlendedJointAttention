import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture('test.mp4')
cap.set(3,640)
cap.set(4,480)
cv2.ocl.setUseOpenCL(False)
fgbg = cv2.createBackgroundSubtractorMOG2()
time = datetime.datetime.now().time()
print time
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    print(fgmask.shape)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()