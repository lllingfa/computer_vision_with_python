# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 22:12:20 2016

@author: user
"""

from scipy.misc import imresize
import graphcut
from PIL import Image
from numpy import *
from pylab import *

im = array(Image.open('../pcv_data/data/empire.jpg'))
im = imresize(im,0.03,interp='bilinear')
size = im.shape[:2]

# add two rectangular training regions
labels = zeros(size)
labels[3:8,3:8] = -1
labels[-8:-3,-8:-3] = 1

# create graph
g = graphcut.build_bayes_graph(im,labels,kappa=1)

# cut the graph
res = graphcut.cut_graph(g,size)


figure()
graphcut.show_labeling(im,labels)

figure()
imshow(res)
gray()
axis('off')

show()