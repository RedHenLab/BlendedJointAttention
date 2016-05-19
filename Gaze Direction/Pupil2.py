import cv2
import numpy as np
def pupil_detect():
	faceCascade1 = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
	faceCascade2 = cv2.CascadeClassifier('haarcascades/haarcascade_profileface.xml')
	eyecascade1 = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
	eyecascade2 = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')
