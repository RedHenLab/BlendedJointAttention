from matplotlib import pyplot
from bob.ip.flandmark import *
from bob.ip.draw import box, cross
from bob.ip.color import rgb_to_gray

def get_data(f):
  from os.path import join
  from pkg_resources import resource_filename
  from bob.io.base import load
  import bob.io.image
  return load(resource_filename('bob.ip.flandmark', join('data', f)))

lena = get_data('lena.jpg')
lena_gray = rgb_to_gray(lena)
x, y, width, height = [214, 202, 183, 183] #or from OpenCV
localizer = Flandmark()
keypoints = localizer.locate(lena_gray, y, x, height, width)

# draw the keypoints and bounding box
box(lena, (y, x), (height, width), (255, 0, 0)) # red bounding box
for k in keypoints:
  cross(lena, k.astype(int), 5, (255, 255, 0)) # yellow key points

# pyplot.imshow(lena.transpose(1, 2, 0))