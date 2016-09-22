# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 21:37:23 2016

@author: user
"""
from PIL import Image
from pylab import *
from numpy import *

import dsift,sift
dsift.process_image_dsift('../pcv_data/data/empire.jpg','empire.sift',90,40,True)
l,d = sift.read_features_from_file('empire.sift')

im = array(Image.open('../pcv_data/data/empire.jpg'))
sift.plot_features(im,l,True)
show()