# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:16:12 2016

@author: user
"""
from PIL import Image
from numpy import *
from pylab import *
import sys
sys.path.append('../ch1/')
sys.path.append('../ch2/')
import os, sift,pca,bayes
def read_gesture_features_labels(path):
    # create list of all files ending in .dsift
  featlist = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.dsift')]
# read the features
  features = []
  for featfile in featlist:
    l,d = sift.read_features_from_file(featfile)
    features.append(d.flatten())
  features = array(features)
# create labels
  labels = [featfile.split('/')[-1][0] for featfile in featlist]
  return features,array(labels)


def convert_labels(labels,transl):
    """ Convert between strings and numbers. """
    return [transl[l] for l in labels]


def print_confusion(res,labels,classnames):
  n = len(classnames)
  
# confusion matrix
  class_ind = dict([(classnames[i],i) for i in range(n)])
  
  confuse = zeros((n,n))
  for i in range(len(test_labels)):
    confuse[class_ind[res[i]],class_ind[test_labels[i]]] += 1
    
  print 'Confusion matrix for'
  print classnames
  print confuse

features,labels = read_gesture_features_labels('../pcv_data/data/handgesture/train/')

test_features,test_labels = read_gesture_features_labels('../pcv_data/data/handgesture/test/')

classnames = unique(labels)

V,S,m = pca.pca(features)
# keep most important dimensions
V = V[:50]
features = array([dot(V,f-m) for f in features])
test_features = array([dot(V,f-m) for f in test_features])
# test kNN
k = 1
knn_classifier = knn.KnnClassifier(labels,features)
res = array([knn_classifier.classify(test_features[i],k) for i in
          range(len(test_labels))])

# accuracy
acc = sum(1.0*(res==test_labels)) / len(test_labels)
print 'Accuracy by knn:', acc
print_confusion(res,test_labels,classnames)

# test Bayes
bc = bayes.BayesClassifier()
blist = [features[where(labels==c)[0]] for c in classnames]

bc.train(blist,classnames)
res = bc.classify(test_features)[0]

acc = sum(1.0*(res==test_labels)) / len(test_labels)
print 'Accuracy by bayes:', acc
print_confusion(res,test_labels,classnames)

#test svm
features = map(list,features)
test_features = map(list,test_features)

# create conversion function for the labels
transl = {}
for i,c in enumerate(classnames):
  transl[c],transl[i] = i,c
# create SVM
prob = svm_problem(convert_labels(labels,transl),features)
param = svm_parameter('-t 0')

# train SVM on data
m = svm_train(prob,param)

# how did the training do?
res = svm_predict(convert_labels(labels,transl),features,m)

# test the SVM
res = svm_predict(convert_labels(test_labels,transl),test_features,m)[0]
res = convert_labels(res,transl)

acc = sum(1.0*(res==test_labels)) / len(test_labels)
print 'Accuracy:', acc

print_confusion(res,test_labels,classnames)