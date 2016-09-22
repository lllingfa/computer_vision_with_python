# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 20:37:01 2016

@author: user
"""
from PIL import Image
from numpy import *
from pylab import *
import scipy.io  
import scipy.misc
from scipy.ndimage import filters
from scipy.ndimage import measurements,morphology
im = array(Image.open('baby_1.jpg').convert('L'))
'''save to .mat'''
data = {}
data['im'] = im
scipy.io.savemat('test.mat',data)

'''load mat'''
data = scipy.io.loadmat('test.mat')
im2= 1*(im<128)
'''save im2 to jpg'''
scipy.misc.imsave('binary.jpg',im2)
lena = scipy.misc.lena()
scipy.misc.imsave('lena.jpg',lena)
labels, nbr_objects = measurements.label(im2)
print "Number of objects:", nbr_objects
im_open = morphology.binary_opening(im2,ones((9,5)),iterations=1)
labels_open, nbr_objects_open = measurements.label(im_open)
print "Number of objects:", nbr_objects_open
figure
subplot(2,2,1)
imshow(im2)
subplot(2,2,2)
imshow(im_open)
subplot(2,2,3)
imshow(lena)