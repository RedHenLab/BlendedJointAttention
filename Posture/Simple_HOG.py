import cv2
hog = cv2.HOGDescriptor()
im = cv2.imread('test.jpg')
h = hog.compute(im)
print type(h)