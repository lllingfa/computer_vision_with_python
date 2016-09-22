# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:34:57 2016

@author: user
"""
from PIL import Image
from numpy import *
from pylab import *
from matplotlib.figure import Figure
import sys
sys.path.append('../ch1/')
sys.path.append('../ch2/')
sys.path.append('../ch3/')
import os, sift,pca,bayes,imtools
from svmutil import *
import os
from pylab import plot, ginput, show, axis
def compute_feature(im):
  """ Returns a feature vector for an
  ocr image patch. """
# resize and remove border
  norm_im = imtools.imresize(im,(30,30))
  norm_im = norm_im[3:-3,3:-3]
  
  return norm_im.flatten()

def load_ocr_data(path):
  """ Return labels and ocr features for all images
  in path. """
  
# create list of all files ending in .jpg
  imlist = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
# create labels
  labels = [int(imfile.split('/')[-1][0]) for imfile in imlist]
  
# create features from the images
  features = []
  for imname in imlist:
    im = array(Image.open(imname).convert('L'))
    features.append(compute_feature(im))
  return array(features),labels

# TRAINING DATA
features,labels = load_ocr_data('../pcv_data/data/sudoku_images/sudoku_images/ocr_data/training/')
# TESTING DATA
test_features,test_labels = load_ocr_data('../pcv_data/data/sudoku_images/sudoku_images/ocr_data/testing/')
# train a linear SVM classifier

features = map(list,features)
test_features = map(list,test_features)

prob = svm_problem(labels,features)
param = svm_parameter('-t 0')

m = svm_train(prob,param)

# how did the training do?
res = svm_predict(labels,features,m)

# how does it perform on the test set?
res = svm_predict(test_labels,test_features,m)

from scipy.ndimage import measurements
def find_sudoku_edges(im,axis=0):
  """ Finds the cell edges for an aligned sudoku image. """
# threshold and sum rows and columns
  trim = 1*(im<128)
  s = trim.sum(axis=axis)
  
# find center of strongest lines
  s_labels,s_nbr = measurements.label(s>(0.5*max(s)))
  m = measurements.center_of_mass(s,s_labels,range(1,s_nbr+1))
  x = [int(x[0]) for x in m]
  
# if only the strong lines are detected add lines in between
  if len(x)==4:
    dx = diff(x)
    x = [x[0],x[0]+dx[0]/3,x[0]+2*dx[0]/3,
        x[1],x[1]+dx[1]/3,x[1]+2*dx[1]/3,
        x[2],x[2]+dx[2]/3,x[2]+2*dx[2]/3,x[3]]
        
    if len(x)==10:
       return x
    else:
       raise RuntimeError('Edges not detected.')
#aligned image   
imname = '../pcv_data/data/sudoku_images/sudoku_images/sudokus/sudoku18.jpg'
vername = '../pcv_data/data/sudoku_images/sudoku_images/sudokus/sudoku18.sud'
im = array(Image.open(imname).convert('L'))

# find the cell edges
x = find_sudoku_edges(im,axis=0)
y = find_sudoku_edges(im,axis=1)

# crop cells and classify
crops = []
for col in range(9):
   for row in range(9):
     crop = im[y[col]:y[col+1],x[row]:x[row+1]]
     crops.append(compute_feature(crop))
     
res = svm_predict(loadtxt(vername),map(list,crops),m)[0]
res_im = array(res).reshape(9,9)

print 'Result:'
print res_im

#non-aligned image
from scipy import ndimage
import homography

imname = '../pcv_data/data/sudoku_images/sudoku_images/sudokus/sudoku8.jpg'
im = array(Image.open(imname).convert('L'))

# mark corners
figure()
imshow(im)
gray()

x = ginput(4)

# top left, top right, bottom right, bottom left
fp = array([array([p[1],p[0],1]) for p in x]).T
tp = array([[0,0,1],[0,1000,1],[1000,1000,1],[1000,0,1]]).T

# estimate the homography
H = homography.H_from_points(tp,fp)

# helper function for geometric_transform
def warpfcn(x):
  x = array([x[0],x[1],1])
  xt = dot(H,x)
  xt = xt/xt[2]
  return xt[0],xt[1]
  
# warp image with full perspective transform
im_g = ndimage.geometric_transform(im,warpfcn,(1000,1000))
#imshow(im_g)