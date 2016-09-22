# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 17:32:45 2016

@author: user
"""
from PIL import Image
from numpy import *
import homography
import warp
# open image to warp
fromim = array(Image.open('../pcv_data/data/sunset_tree.jpg'))
x,y = meshgrid(range(5),range(6))
x = (fromim.shape[1]/4) *x.flatten()
y = (fromim.shape[0]/5) * y.flatten()
# triangulate
tri = warp.triangulate_points(x,y)
# open image and destination points
im = array(Image.open('../pcv_data/data/turningtorso1.jpg'))
tp = loadtxt('../pcv_data/data/turningtorso1_points.txt') # destination points
# convert points to hom. coordinates
fp = vstack((y,x,ones((1,len(x)))))
tp = vstack((tp[:,1],tp[:,0],ones((1,len(tp)))))
# warp triangles
im = warp.pw_affine(fromim,im,fp,tp,tri)
# plot
figure()
imshow(im)
warp.plot_mesh(tp[1],tp[0],tri)
axis('off')
show()