# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:05:22 2016

@author: user
"""
from PIL import Image
from numpy import *
import sys
sys.path.append('../ch2/')
import sift
import homography
featname = ['../pcv_data/data/Univ'+str(i+1)+'.sift' for i in range(5)]
imname = ['../pcv_data/data/Univ'+str(i+1)+'.jpg' for i in range(5)]
l = {}
d = {}
for i in range(5):
  sift.process_image(imname[i],featname[i])
  l[i],d[i] = sift.read_features_from_file(featname[i])
matches = {}
for i in range(4):
  matches[i] = sift.match(d[i+1],d[i])
  # visualize the matches (Figure 3-11 in the book)
for i in range(4):
    im1 = array(Image.open(imname[i]))
    im2 = array(Image.open(imname[i+1]))
    figure()
    sift.plot_matches(im2,im1,l[i+1],l[i],matches[i],show_below=True)
    
'''def convert_points(j):
  ndx = matches[j].nonzero()[0]
  fp = homography.make_homog(l[j+1][ndx,:2].T)
  ndx2 = [int(matches[j][i]) for i in ndx]
  tp = homography.make_homog(l[j][ndx2,:2].T)
  return fp,tp'''
  # function to convert the matches to hom. points
def convert_points(j):
    ndx = matches[j].nonzero()[0]
    fp = homography.make_homog(l[j+1][ndx,:2].T) 
    ndx2 = [int(matches[j][i]) for i in ndx]
    tp = homography.make_homog(l[j][ndx2,:2].T) 
    
    # switch x and y - TODO this should move elsewhere
    fp = vstack([fp[1],fp[0],fp[2]])
    tp = vstack([tp[1],tp[0],tp[2]])
    return fp,tp
    
# estimate the homographies
model = homography.RansacModel()
fp,tp = convert_points(1)
H_12 = homography.H_from_ransac(fp,tp,model)[0] #im 1 to 2
fp,tp = convert_points(0)
H_01 = homography.H_from_ransac(fp,tp,model)[0] #im 0 to 1
tp,fp = convert_points(2) #NB: reverse order
H_32 = homography.H_from_ransac(fp,tp,model)[0] #im 3 to 2
tp,fp = convert_points(3) #NB: reverse order
H_43 = homography.H_from_ransac(fp,tp,model)[0] #im 4 to 3

delta = 2000 #for padding and translation
im1 = array(Image.open(imname[1]))
im2 = array(Image.open(imname[2]))
im_12 = warp.panorama(H_12,im1,im2,delta,delta)

im1 = array(Image.open(imname[0]))
im_02 = warp.panorama(dot(H_12,H_01),im1,im_12,delta,delta)

im1 = array(Image.open(imname[3]))
im_32 = warp.panorama(H_32,im1,im_02,delta,delta)

im1 = array(Image.open(imname[4]))
im_42 = warp.panorama(dot(H_32,H_43),im1,im_32,delta,2*delta)

figure()
imshow(array(im_42, "uint8"))
axis('off')
show()
