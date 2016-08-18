import numpy as np
import cv2

img = cv2.imread('../Test/image.jpg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(grey,25,0.01,10)
corners = np.int0(corners)
# print corners
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),1,(0,0,255),-1)

cv2.imwrite('image.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()