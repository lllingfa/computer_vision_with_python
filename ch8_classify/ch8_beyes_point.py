# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:03:19 2016

@author: user
"""

from pylab import *
from numpy import *
import pickle
import sys
sys.path.append('../ch1/')
import imtools
import bayes

# load 2D example points using Pickle
with open('points_normal.pkl', 'r') as f:
  class_1 = pickle.load(f)
  class_2 = pickle.load(f)
  labels = pickle.load(f)

# train Bayes classifier
bc = bayes.BayesClassifier()
bc.train([class_1,class_2],[1,-1])

# load test data using Pickle
with open('points_normal_test.pkl', 'r') as f:
  class_1 = pickle.load(f)
  class_2 = pickle.load(f)
  labels = pickle.load(f)
# test on some points
print bc.classify(class_1[:10])[0]
# plot points and decision boundary

def classify(x,y,bc=bc):
  points = vstack((x,y))
  return bc.classify(points.T)[0]
imtools.plot_2D_boundary([-6,6,-6,6],[class_1,class_2],classify,[1,-1])
show()