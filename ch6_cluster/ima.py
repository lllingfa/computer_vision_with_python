# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 09:38:16 2016

@author: user
"""

from numpy import *
from PIL import Image
from scipy.ndimage import filters
sys.path.append('../ch1/')
import rof
im = array(Image.open('C:\\Users\\user\\Desktop\\1.jpg').convert('L'))
imshow(im)
im3 = filters.gaussian_filter(im,2)
imshow(im3)
U,T = rof.denoise(im,im)
figure()
gray()
imshow(U)
axis('equal')
axis('off')
show()
'''直方图显示点的分布'''
figure()
hist(im.flatten(),128)
show()
scipy.misc.imsave('rof1.jpg',U)
