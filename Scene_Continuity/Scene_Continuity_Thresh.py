import cv2

cam = cv2.VideoCapture("test.mp4")
cam.set(3,640)
cam.set(4,480)
video_capture = cam
frame_num = 0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
    	frame = frame+1
    	if frame_num == 1:
    		firstFrame = frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (21, 21), 0)
		frameDelta = cv2.absdiff(firstFrame, gray)
		thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
		# Display the resulting frame
		cv2.imshow('Video', thresh)
		cv2.imshow('Video',	frameDelta)
		cv2.imshow('Video', gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
