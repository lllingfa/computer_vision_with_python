# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:38:07 2016

@author: user
"""
from PIL import Image
from numpy import *
import stereo

im_l = array(Image.open('scene1.row3.col3.ppm').convert('L'),'f')
im_r = array(Image.open('scene1.row3.col4.ppm').convert('L'),'f')
# starting displacement and steps
steps = 12
start = 4
# width for ncc
wid = 9
res = stereo.plane_sweep_ncc(im_l,im_r,start,steps,wid)
import scipy.misc
scipy.misc.imsave('depth.png',res)