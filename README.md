Belended Classic Joint Attention Repository
============================================

<i> Pull requests from members other than that of Red Hen Labs would not be merged here. This is just a repository for temporary work. If you still believe that there is a threat to humanity which this repo may endure, you may send a mail to agarwalsoumitra1504[at]gmail[dot]com. If you wish to contribute to blended joint attention look at [this](https://github.com/RedHenLab/BlendedJointAttentionClean) repository.</i> 

This repository deals with work done by The Distibuted Red Hen Lab towards classification of different instances of blended classic joint attention in various form of print, audio and video media. For more information visit : https://sites.google.com/site/distributedlittleredhen/home/the-cognitive-core-research-topics-in-red-hen/the-barnyard/blended-classic-joint-attention

---------------------------------------------

Sub-repositories:

* Face detection : Detection of number of human faces, possible extensions to their position and orientation


* Emotion recognition : Recognising different emotions (sad, happy, surprised, neutral etc.) using a CNN classifier. To see and example run :

```python webcam-emotions.py --displayWebcam --seeFaces --netFile soumitra.p```

To get best results (and tailored for the person who is using the webcam app), you can use the `webcam-emotions.py` script to record data, as follows,(train happy by replacing sad by happy):

```python webcam-emotions.py --displayWebcam --seeFaces --gather_training_data  --recording_emotion sad```


* Gaze direction recognition : Calculating angle of ones gaze using initial pupil detection and terminal points of eyes.</li>


* Age detection : Categorising a person's age via facial features (outputs a range of possible age values)


* Facial Landmark detection : Detecting major facial landmarks, which is useful for Gaze direction and Emotion recognition.


* Blended CLassic Joint attention : Detectiong instances of BCJA from instances without BCJA


* Reaction Shots : Analyse reaction shots (of surprise, awe etc.) 


* Gesture Recognition : Recognising multimodal gestures


* Head pose : Configuiring head pose to gaze direction and independent head pose stimation

----------------------------------------

Required Packages:

<ol>
	<li> Python 2.7.x </li>
	<li> Numpy </li>
	<li> Bob </li>
	<li> Matplotlib </li>
	<li> OpenCV (One must check compatibility with python and OS) </li>
	<li> DLib </li>
	<li> pympi-ling </li>
	<li> PySceneDetect </li>
</ol>

-----------------------------------------

Authors:

<ol>
 	<li> Dr.Mark Turner </li>
 	<li> Dr.Francis Steen </li>
	<li> <a href = "https://github.com/SoumitraAgarwal" target="_blank">Soumitra Agarwal</a> :neckbeard: </li>
	<li> Debayan Das </li>
</ol>
----------------------------------------
