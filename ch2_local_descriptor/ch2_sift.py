# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:10:37 2016

@author: user
"""
from PIL import Image
from pylab import *

from numpy import *

import sift
imname ='baby_1.jpg'
im1 = array(Image.open(imname).convert('L'))
imshow(im1)
sift.process_image(imname,'baby.sift') 
l1,d1 = sift.read_features_from_file('baby.sift')
figure()
gray()
sift.plot_features(im1,l1,circle=True)
show()
imname1 = 'climbing_1_small.jpg'
imname2 = 'climbing_2_small.jpg'

# process and save features to file
sift.process_image(imname1, imname1+'.sift')
sift.process_image(imname2, imname2+'.sift')

# read features and match
l2,d2 = sift.read_features_from_file(imname1+'.sift')
l3,d3 = sift.read_features_from_file(imname2+'.sift')
matchscores = sift.match_twosided(d2, d3)

# load images and plot
im1 = array(Image.open(imname1))
im2 = array(Image.open(imname2))

sift.plot_matches(im1,im2,l2,l3,matchscores,show_below=True)
show()
