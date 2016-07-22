import cv2

def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)

hog = cv2.HOGDescriptor()
im = cv2.imread('test.jpg')
found,w=hog.detectMultiScale(im, winStride=(8,8), padding=(32,32), scale=1.05)
draw_detections(im,found)
cv2.imwrite('Result1.jpg', im)