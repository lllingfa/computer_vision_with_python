# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *
from numpy import *
from scipy.ndimage import measurements,morphology
# read image to array
im = array(Image.open('baby1.jpg'))
# plot the image
'''画图，加点，加线，可用来标记兴趣点、相关性和目标检测'''
imshow(im)
# some points
x = [100,100,200,200]
y = [100,200,200,100]
# plot the points with red star-markers
plot(x,y,'ks:')

# line plot connecting the first two points
plot(x[0:2],y[0:2])
# add title and show the plot
title('Plotting: "baby1.jpg"')
axis('off')
show()