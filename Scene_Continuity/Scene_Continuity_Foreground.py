import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture('test.mp4')
video_capture = cap
cv2.ocl.setUseOpenCL(False)
fgbg = cv2.createBackgroundSubtractorMOG2()
time = datetime.datetime.now()
scene_num = 0
while(1):
    ret, frame = video_capture.read()
    fgmask = fgbg.apply(frame)
    num_white = 0
    time = datetime.datetime.now()
    for i in range(fgmask.shape[0]):
    	for j in range(fgmask.shape[1]):
    		if fgmask[i][j] == 255:
    			num_white = num_white+1
    			if(num_white>0.8*fgmask.shape[0]*fgmask.shape[0]):
    				scene_num = scene_num + 1
    				print("Scene changed : ", scene_num)
    				break
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()