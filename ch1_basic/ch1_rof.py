# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 21:14:44 2016

@author: user
"""

from numpy import *
from numpy import random
from pylab import *
from scipy.ndimage import filters
import rof
# create synthetic image with noise
im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300,200:300] = 255
'''add in noise'''
im = im + 30*random.standard_normal((500,500))
imshow(im)
U,T = rof.denoise(im,im)
G = filters.gaussian_filter(im,10)
im1 = array(Image.open('baby_1.jpg').convert('L'))
U,T = rof.denoise(im1,im1)
figure()
gray()
imshow(U)
axis('equal')
axis('off')
show()
# save the result
import scipy.misc
scipy.misc.imsave('synth_rof.pdf',U)
scipy.misc.imsave('synth_gaussian.pdf',G)