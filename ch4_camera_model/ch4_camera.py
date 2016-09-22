# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 20:58:52 2016

@author: user
"""
from PIL import Image
from numpy import *
import camera
# load points
points = loadtxt('../pcv_data/data/3D/house.p3d').T
points = vstack((points,ones(points.shape[1])))
# setup camera
P = hstack((eye(3),array([[0],[0],[-10]])))
cam = camera.Camera(P)
x = cam.project(points)
# plot projection
figure()
plot(x[0],x[1],'k.')
show()
# create transformation
r = 0.05*random.rand(3)
rot = camera.rotation_matrix(r)
# rotate camera and project
figure()
for t in range(20):
  cam.P = dot(cam.P,rot)
  x = cam.project(points)
  plot(x[0],x[1],'k.')
show()
K = array([[1000,0,500],[0,1000,300],[0,0,1]])
tmp = camera.rotation_matrix([0,0,1])[:3,:3]
Rt = hstack((tmp,array([[50],[40],[30]])))
cam = camera.Camera(dot(K,Rt))
print K,Rt
print cam.factor()