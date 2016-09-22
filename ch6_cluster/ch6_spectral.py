# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 19:26:16 2016

@author: user
"""
import sys
sys.path.append('../ch1/')
import imtools
from numpy import *
from PIL import Image
import pickle
from scipy.cluster.vq import *

imlist = imtools.get_imlist('../pcv_data/data/selectedfontimages/a_selected_thumbs/')
imnbr = len(imlist)
# load model file
with open('a_pca_modes.pkl','rb') as f:
  immean = pickle.load(f)
  V = pickle.load(f)
# create matrix to store all flattened images
immatrix = array([array(Image.open(im)).flatten()
                          for im in imlist],'f')
    # project on the 40 first PCs
immean = immean.flatten()
projected = array([dot(V[[0,1]],immatrix[i]-immean) for i in range(imnbr)])

n = len(projected)

# compute distance matrix
S = array([[ sqrt(sum((projected[i]-projected[j])**2))
                                 for i in range(n) ] for j in range(n)], 'f')
# create Laplacian matrix
rowsum = sum(S,axis=0)
D = diag(1 / sqrt(rowsum))
I = identity(n)
L = I - dot(D,dot(S,D))
# compute eigenvectors of L
U,sigma,V = linalg.svd(L)
k = 5
# create feature vector from k first eigenvectors
# by stacking eigenvectors as columns
features = array(V[:k]).T
# k-means
features = whiten(features)
centroids,distortion = kmeans(features,k)
code,distance = vq(features,centroids)
# plot clusters
for c in range(k):
    ind = where(code==c)[0]
    figure()
    for i in range(minimum(len(ind),39)):
            im = Image.open(imlist[ind[i]])
            subplot(4,10,i+1)
            imshow(array(im))
            axis('equal')
            axis('off')
show()
n = len(imlist)
# load the similarity matrix and reformat
S = loadtxt('panoramio_matches.txt')
S = 1 / (S + 1e-6)