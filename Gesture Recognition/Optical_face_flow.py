import cv2
import numpy as np

# Defining cascade variables
faceCascade1 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')

# Video capture via webcam
cam = cv2.VideoCapture("../Test/test.mp4")
cam.set(3,640)
cam.set(4,480)
video_capture = cam
frame_num = 0
roi_gray_old=[]
p0 = []
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces1 = faceCascade1.detectMultiScale(gray, 1.4, 5)
		img = frame
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces1:
			roi_gray = gray[y:y+h, x:x+w]
			if frame_num == 0:
				roi_gray_old = roi_gray
				# Take first frame and find corners in it
				p0 = cv2.goodFeaturesToTrack(roi_gray, mask = None, maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7 )
				# Create a mask image for drawing purposes
				mask = np.zeros_like(old_frame)
				frame_num = frame_num + 1
			else :
				# calculate optical flow
				p1, st, err = cv2.calcOpticalFlowPyrLK(roi_gray_old, roi_gray, p0,	maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

				# Select good points
				good_new = p1[st==1]
				good_old = p0[st==1]

				# draw the tracks
				for i,(new,old) in enumerate(zip(good_new,good_old)):
					print i
					a,b = new.ravel()
					c,d = old.ravel()
					cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
					cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
				img = cv2.add(frame,mask)

		# Display the resulting frame
		cv2.imshow('Video', img)
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break
		# Release video capture
video_capture.release()
cv2.destroyAllWindows()