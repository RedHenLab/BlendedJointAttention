To see and example run :

```python webcam-emotions.py --displayWebcam --seeFaces --netFile soumitra.p```

To get best results (and tailored for the person who is using the webcam app), you can use the `webcam-emotions.py` script to record data, as follows,(train happy by replacing sad by happy):

```python webcam-emotions.py --displayWebcam --seeFaces --gather_training_data  --recording_emotion sad```