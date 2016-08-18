import cv2

img = cv2.imread('../Result_Images/eye1.jpg',0)
thresh = cv2.threshold(img , 150, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('../Result_Images/thresh_eye.jpg',thresh)