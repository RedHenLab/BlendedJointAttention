import cv2
import numpy as np
from matplotlib import pyplot as plt

# Video capture via webcam
cam = cv2.VideoCapture('test.mp4')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(grey,25,0.01,10)
corners = np.int0(corners)
# print corners
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),1,(0,0,255),-1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()