# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:00:50 2016

@author: user
"""
from PIL import Image
from numpy import *
from pylab import *

#from svmutil import *
import os
import dsift
# process images at fixed size (50,50)

path = '../pcv_data/data/handgesture/test/'
imlist = []
for filename in os.listdir(path):
    if os.path.splitext(filename)[1] == '.ppm':
        imlist.append(path+filename)


# process images at fixed size (50,50)
for filename in imlist:
    featfile = filename[:-3]+'dsift'
    dsift.process_image_dsift(filename, featfile, 10, 5, resize=(50,50))


# show an image with features
l,d = sift.read_features_from_file(featfile)
im = array(Image.open(filename).resize((50,50)))
print im.shape

figure()
sift.plot_features(im, l, True)
show()

