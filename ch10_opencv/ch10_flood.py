import cv2
from numpy import *

# read image
filename = '../pcv_data/data/fisherman.jpg'
im = cv2.imread(filename)
h,w = im.shape[:2]
# flood fill example
diff = (6,6,6)
mask = zeros((h+2,w+2),uint8)
cv2.floodFill(im,mask,(10,10), (255,255,0),diff,diff)
# show the result in an OpenCV window
cv2.imshow('flood fill',im)
cv2.waitKey()
# save the result
cv2.imwrite('result_flood.jpg',im)