# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:18:14 2016

@author: user
"""
from PIL import Image
from numpy import *
from scipy import ndimage
im = array(Image.open('../ch1/baby_1.jpg').convert('L'))
H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
im2 = ndimage.affine_transform(im,H[:2,:2],(H[0,2],H[1,2]))
figure()
gray()
imshow(im2)
show()
