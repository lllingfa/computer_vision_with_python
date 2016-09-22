# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 16:33:45 2016

@author: user
"""
from PIL import Image
from numpy import *
import sys
sys.path.append('../ch4/')
import camera
# load some images
im1 = array(Image.open('../pcv_data/data/Merton1/images/001.jpg'))
im2 = array(Image.open('../pcv_data/data/Merton1/images/002.jpg'))
# load 2D points for each view to a list
points2D = [loadtxt('../pcv_data/data/Merton1/2D/00'+str(i+1)+'.corners').T for i in range(3)]
# load 3D points
points3D = loadtxt('../pcv_data/data/Merton1/3D/p3d').T
# load correspondences
corr = genfromtxt('../pcv_data/data/Merton1/2D/nview-corners',dtype='int')#,missing='*'
# load cameras to a list of Camera objects
P = [camera.Camera(loadtxt('../pcv_data/data/Merton1/2D/00'+str(i+1)+'.P')) for i in range(3)]
