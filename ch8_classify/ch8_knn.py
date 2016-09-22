# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:51:59 2016

@author: user
"""
import sys
sys.path.append('../ch1/')
import pickle
import knn
import imtools
from pylab import *
from numpy import *
# load 2D points using Pickle
with open('points_normal.pkl', 'r') as f:
  class_1 = pickle.load(f)
  class_2 = pickle.load(f)
  labels = pickle.load(f)
model = knn.KnnClassifier(labels,vstack((class_1,class_2)))
# load test data using Pickle

with open('points_normal_test.pkl', 'r') as f:
  class_1 = pickle.load(f)
  class_2 = pickle.load(f)
  labels = pickle.load(f)
  
# test on the first point
print model.classify(class_1[0])
# define function for plotting
def classify(x,y,model=model):
  return array([model.classify([xx,yy]) for (xx,yy) in zip(x,y)])
# plot the classification boundary
  
imtools.plot_2D_boundary([-6,6,-6,6],[class_1,class_2],classify,[1,-1])
show()