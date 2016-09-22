# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:01:44 2016

@author: user
"""
from PIL import Image
from numpy import *
import sfm
sys.path.append('../ch4/')
import camera
corr = corr[:,0] # view 1
ndx3D = where(corr>=0)[0] # missing values are -1
ndx2D = corr[ndx3D]
# select visible points and make homogeneous
x = points2D[0][:,ndx2D] # view 1
x = vstack( (x,ones(x.shape[1])) )
X = points3D[:,ndx3D]
X = vstack( (X,ones(X.shape[1])) )
# estimate P
Pest = camera.Camera(sfm.compute_P(x,X))
# compare!
print Pest.P / Pest.P[2,3]
print P[0].P / P[0].P[2,3]
xest = Pest.project(X)
# plotting
figure()
imshow(im1)
plot(x[0],x[1],'b.')
plot(xest[0],xest[1],'r.')
axis('off')
show()