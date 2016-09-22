# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 16:51:25 2016

@author: user
"""
from PIL import Image
from numpy import *
from mpl_toolkits.mplot3d import axes3d
fig = figure()
ax = fig.gca(projection="3d")
# generate 3D sample data
X,Y,Z = axes3d.get_test_data(0.25)
# plot the points in 3D
ax.plot(X.flatten(),Y.flatten(),Z.flatten(),'o')
show()