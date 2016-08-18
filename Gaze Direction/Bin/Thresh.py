import cv2

img = cv2.imread('../Result_Images/eye.jpg')
thresh = cv2.threshold(img , 25, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('../Result_Images/thresh_eye.jpg',thresh)