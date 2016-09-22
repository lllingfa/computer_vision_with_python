# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:19:46 2016

@author: user
"""
from PIL import Image
from pylab import *
import harris

im = array(Image.open('../ch1/baby_16.jpg').convert('L'))
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim,6)
harris.plot_harris_points(im, filtered_coords)
imshow(im)
wid = 5
im1 = array(Image.open('../ch1/baby_1.jpg').convert('L'))
harrisim = harris.compute_harris_response(im1,5)
filtered_coords1 = harris.get_harris_points(harrisim,wid+1)
d1 = harris.get_descriptors(im1,filtered_coords1,wid)
im2 = array(Image.open('../ch1/baby_16.jpg').convert('L'))
harrisim = harris.compute_harris_response(im2,5)
filtered_coords2 = harris.get_harris_points(harrisim,wid+1)
d2 = harris.get_descriptors(im2,filtered_coords2,wid)
print 'starting matching'
matches = harris.match_twosided(d1,d2)
figure()
gray()
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches)
show()