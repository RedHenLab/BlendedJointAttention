import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image.jpg', 0)

corners = cv2.goodFeaturesToTrack(img,25,0.01,10)
corners = np.int0(corners)
print corners
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

# plt.imshow(img),plt.show()
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()