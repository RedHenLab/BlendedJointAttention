import cv2
import numpy as np

# Defining cascade variables
faceCascade1 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')

# Video capture via webcam
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
video_capture = cam
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces1 = faceCascade1.detectMultiScale(gray, 1.4, 5)
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces1:
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]
			corners = cv2.goodFeaturesToTrack(roi_gray,90,0.01,10)
			corners = np.int0(corners)
			# print corners
			for i in corners:
				x1,y1 = i.ravel()
				cv2.circle(frame,(x+x1,y+y1),3,(255,255,255),-1)

		# Display the resulting frame
		cv2.imshow('Video', frame)
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break
		# Release video capture
video_capture.release()
cv2.destroyAllWindows()