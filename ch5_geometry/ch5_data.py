# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 16:23:15 2016

@author: user
"""
from PIL import Image
from numpy import *
import sys
sys.path.append('../ch4/')
import camera
from mpl_toolkits.mplot3d import axes3d
execfile('load_vggdata.py')
# make 3D points homogeneous and project
X = vstack( (points3D,ones(points3D.shape[1])) )
x = P[0].project(X)
# plotting the points in view 1
figure()
imshow(im1)
plot(points2D[0][0],points2D[0][1],'*')
axis('off')

figure()
imshow(im1)
plot(x[0],x[1],'r.')
axis('off')
show()

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(points3D[0],points3D[1],points3D[2],'k.')