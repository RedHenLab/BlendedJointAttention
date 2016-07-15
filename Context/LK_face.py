import cv2
import numpy as np
from matplotlib import pyplot as plt

# Video capture via webcam
cam = cv2.VideoCapture('../Test/test.mp4')
cam.set(3,640)
cam.set(4,480)
video_capture = cam

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
print ret
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, 900,0.01,10)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
		grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		corners = cv2.goodFeaturesToTrack(grey,900,0.01,10)
		corners = np.int0(corners)
		# print corners
		for i in corners:
			x,y = i.ravel()
			cv2.circle(frame,(x,y),1,(0,0,255),-1)

		# Display the resulting frame
		cv2.imshow('Video', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()