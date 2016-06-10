import scenedetect

scene_list = []        # Scenes will be added to this list in detect_scenes().
path = 'test.mp4'  # Path to video file.

# Usually use one detector, but multiple can be used.
detector_list = [
    scenedetect.detectors.ThresholdDetector(threshold = 16, min_percent = 0.9)
]

video_framerate, frames_read = scenedetect.detect_scenes_file(path, scene_list, detector_list)

# scene_list now contains the frame numbers of scene boundaries.
print scene_list

# create new list with scene boundaries in milliseconds instead of frame #.
scene_list_msec = [(1000.0 * x) / float(video_framerate) for x in scene_list]

# create new list with scene boundaries in timecode strings ("HH:MM:SS.nnn").
scene_list_tc = [scenedetect.timecodes.get_string(x) for x in scene_list_msec]