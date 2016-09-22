# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 19:42:51 2016

@author: user
"""

from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
from scipy.ndimage import measurements,morphology
im = array(Image.open('baby_1.jpg').convert('L'))

#Sobel derivative filters
imx = zeros(im.shape)
#去噪
filters.gaussian_filter(im, (2,2), (0,1), imx)
filters.sobel(im,1,imx)
imy = zeros(im.shape)
filters.gaussian_filter(im, (2,2), (1,0), imy)
filters.sobel(im,0,imy)
magnitude = sqrt(imx**2+imy**2)
figure
subplot(2,2,1)
imshow(im)
subplot(2,2,2)
imshow(magnitude)
subplot(2,2,3)
imshow(imx)
subplot(2,2,4)
imshow(imy)
