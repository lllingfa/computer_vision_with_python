import cv2
from numpy import *
# setup video capture
cap = cv2.VideoCapture('../pcv_data/data/v_ApplyEyeMakeup_g01_c01.avi')
frames = []

while True:
  ret,im = cap.read()
  blur = cv2.GaussianBlur(im, (0, 0), 5)
  cv2.imshow('camera blur', blur)
  cv2.imshow('video test',im)
  frames.append(im)
  key = cv2.waitKey(10)
  if key == 27:
     break
  if key == ord(' '):
     cv2.imwrite('vid_result.jpg',im)
frames = array(frames)

# check the sizes
print im.shape
print frames.shape