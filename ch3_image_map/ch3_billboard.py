# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:14:47 2016

@author: user
"""
from PIL import Image
from numpy import *
import warp
import homography
# example of affine warp of im1 onto im2
im1 = array(Image.open('../ch1/baby_1.jpg').convert('L'))
im2 = array(Image.open('../pcv_data/data/alcatraz1.jpg').convert('L'))
# set to points
tp = array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])
tp1 = array([[675,826,826,677],[55,52,281,277],[1,1,1,1]])
im3 = warp.image_in_image(im1,im2,tp1)
figure()
gray()
imshow(im3)
axis('equal')
axis('off')
show()
# set from points to corners of im1
m,n = im1.shape[:2]
fp = array([[0,m,m,0],[0,0,n,n],[1,1,1,1]])
# first triangle
tp2 = tp[:,:3]
fp2 = fp[:,:3]
# compute H
H = homography.Haffine_from_points(tp2,fp2)
im1_t = ndimage.affine_transform(im1,H[:2,:2],
(H[0,2],H[1,2]),im2.shape[:2])
# alpha for triangle
alpha = warp.alpha_for_triangle(tp2,im2.shape[0],im2.shape[1])
im5 = (1-alpha)*im2 + alpha*im1_t
# second triangle
tp2 = tp[:,[0,2,3]]
fp2 = fp[:,[0,2,3]]
# compute H
H = homography.Haffine_from_points(tp2,fp2)
im1_t = ndimage.affine_transform(im1,H[:2,:2],
(H[0,2],H[1,2]),im2.shape[:2])
# alpha for triangle
alpha = warp.alpha_for_triangle(tp2,im2.shape[0],im2.shape[1])
im4 = (1-alpha)*im5 + alpha*im1_t
figure()
gray()
subplot(1,2,1)
imshow(im5)
subplot(1,2,2)
imshow(im4)
axis('equal')
axis('off')
show()