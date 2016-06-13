import argparse
import cv2
import os
import scipy
import signal
import sys
import time

import face_detection
import ignoreoutput
import emotionrecognition
import cPickle as pickle

# We need this to import other modules
sys.path.append("..")

from lib import deepbelief

WINDOW_NAME = "Emotion recognition"
TIME_BETWEEN_FACE_CHECKS = 0.1

parser = argparse.ArgumentParser(description=("Live emotion recognition from the webcam"))
parser.add_argument('--displayWebcam', action='store_const', const=True,
                    help="determines if the image from the webcam is displayed")
parser.add_argument('--gather_training_data', action='store_const', const=True,
                    default=False,
                    help=("if false, detects emotions by using the trained network "
                          "given by netFile. If this flag is set to true, this script "
                          "is used to collect training data. In that case, the "
                          "recording_emotion flag needs to be set."))
parser.add_argument("--seeFaces", action='store_const', const=True,
                    help=("If passed as argument, the webcam image will show the "
                          "detected faces. Note that this automatically ensures "
                          "that the camera will be displayed."))
parser.add_argument('--recording_emotion',
                     help="the emotion for which to record training data. "
                          "used only when this script is used for recording "
                          "training data. Example: happy. The user sitting in front "
                          "of the webcam should display this emotion while the program "
                          "is running and recording data.",
                     type=str,
                     default="")
parser.add_argument('--emotions',
                    nargs='+',
                    help=('The emotions labels that were used to train the network. '
                          'These should be strings to associate to the integer classes '
                          'given by the network. For example, if the network should output '
                          '0 when the input face displays a happy emotion and 1 otherwise, '
                          'this map should be \'happy neutral\''),
                    type=str)
parser.add_argument("--frequency", type=float, default=TIME_BETWEEN_FACE_CHECKS,
                    help="How often should the camera be queried for a face")
parser.add_argument("--netFile",
                     help=("pickle file from which to read the network for testing the camera stream."
                           "Used only if the gather_training_data flag is set to False."))


args = parser.parse_args()

# Parse the user given arguments
displayCam = args.displayWebcam
frequency = args.frequency
displayFaces = args.seeFaces

emotion_to_text = {0: "HAPPY",
  1: "SAD",
  2: "SUPRISED"}

if args.emotions:
  for index, emotion in enumerate(args.emotions):
    emotion_to_text[index] = emotion

# Person by Catherine Please from The Noun Project
HAPPY_IMAGE = cv2.imread("icon_4895withoutalpha.png", cv2.IMREAD_GRAYSCALE)
# Sad by Cengiz SARI from The Noun Project
SAD_IMAGE = cv2.imread("icon_39345withoutalpha.png", cv2.IMREAD_GRAYSCALE)
# Surprise designed by Chris McDonnell from the thenounproject.com
SUPRISED_IMAGE = cv2.imread("icon_6231withoutalpha.png", cv2.IMREAD_GRAYSCALE)

# EMOTION_TO_IMAGE = {
#   0: HAPPY_IMAGE,
#   1: SAD_IMAGE,
#   2: SUPRISED_IMAGE
# }

# When user presses Control-C, gracefully exit program
def signal_handler(signal, frame):
  print "The emotion recognition program will terminate."
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def getCameraCapture():
  with ignoreoutput.suppress_stdout_stderr():
    # 0 is supposed to detected any webcam connected to the device
    capture = cv2.VideoCapture(0)
    if not capture:
      print "Failed VideoCapture: unable to open device 0"
      sys.exit(1)
    return capture


def showFrame(frame, faceCoordinates, emotion=None, draw=False):
  if draw and faceCoordinates:
    #  Draw emotions here as well
    face_detection.drawFace(frame, faceCoordinates, emotion,
                              emotion_to_text)

  cv2.imshow(WINDOW_NAME, frame)


def readNetwork():
  with open(args.netFile, "rb") as f:
    net = pickle.load(f)
  return net


def recogintionWork(image, faceCoordinates, net):
  return emotionrecognition.testImage(image, faceCoordinates, net)


def saveFaceImage(capture, frequency, display, drawFaces):
  img_count = 0

  # Create the directory in which we record the training examples.
  if not os.path.exists(args.recording_emotion):
    os.makedirs(args.recording_emotion)

  while True:
    flag, frame = capture.read()

    if flag:
      faceCoordinates = face_detection.getFaceCoordinates(frame)
    if faceCoordinates:
      image = emotionrecognition.preprocess(frame, faceCoordinates)
      # Save the image that will later be used for training.
      scipy.misc.imsave(os.path.join(args.recording_emotion,
                                     args.recording_emotion + str(img_count) + '.png'),
                        image)

      if display:
        showFrame(frame, faceCoordinates, None, drawFaces)
      img_count = img_count + 1

    time.sleep(frequency)


# Draw faces argument is only taken into account if display was set as true.
def detectedAndDisplayFaces(capture, net, display=False, drawFaces=False):
  recognition = True
  # Flag gives us some information about the capture
  # Frame is the webcam frame (a numpy image)
  flag, frame = capture.read()
  # Not sure if there is an error from the cam if we should lock the screen
  if flag:
    faceCoordinates = face_detection.getFaceCoordinates(frame)
    if faceCoordinates and recognition:
      emotion = recogintionWork(frame, faceCoordinates, net)
    else:
      emotion = None
    if display:
      showFrame(frame, faceCoordinates, emotion, drawFaces)
    if faceCoordinates:
      return True
  else:
    return True


def detectEmotions(capture, frequency, display=False, drawFaces=False):
  net = readNetwork()

  while True:
    detectedAndDisplayFaces(capture, net, display, drawFaces)
    time.sleep(frequency)


def main():
  global frequency

  if displayFaces:
    showCam = True
  else:
    showCam = displayCam

  capture = getCameraCapture()

  if showCam:
    cv2.startWindowThread()
    cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WND_PROP_FULLSCREEN)

  if args.gather_training_data:
    print 'Recording training data for emotion:', args.recording_emotion
    print 'Please try to display that emotion during the recording.'
    saveFaceImage(capture, frequency, showCam, displayFaces)
  else:
    print 'Detection emotions from net ', args.netFile
    detectEmotions(capture, frequency, showCam, displayFaces)

if __name__ == '__main__':
  main()
