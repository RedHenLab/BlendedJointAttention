import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture('test.mp4')
video_capture = cap
cv2.ocl.setUseOpenCL(False)
fgbg = cv2.createBackgroundSubtractorMOG2()
time = datetime.datetime.now().time()
print time
scene_num = 0
while(1):
    ret, frame = video_capture.read()
    fgmask = fgbg.apply(frame)
    num_zero = 0
    for i in range(len(fgmask.shape[0])):
    	for j in range(len(fgmask.shape[1])):
    		if fgmask[i][j] == 0:
    			num_zero = num_zero+1
    if(num_zero<0.1*fgmask.shape[0]*fgmask.shape[0]):
    	scene_num = scene_num + 1
    	print("Scene changed : ", scene_num)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()