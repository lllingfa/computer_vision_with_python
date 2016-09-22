# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:48:14 2016

@author: user
"""

import pickle
import sift
import imagesearch
import homography
# load image list and vocabulary
with open('ukbench_imlist.pkl','rb') as f:
  imlist = pickle.load(f)
  featlist = pickle.load(f)
  
nbr_images = len(imlist)
with open('vocabulary.pkl', 'rb') as f:
   voc = pickle.load(f)
   
src = imagesearch.Searcher('test.db',voc)
# index of query image and number of results to return
q_ind = 50
nbr_results = 20
# regular query
res_reg = [w[1] for w in src.query(imlist[q_ind])[:nbr_results]]
print 'top matches (regular):', res_reg

# load image features for query image
q_locs,q_descr = sift.read_features_from_file(featlist[q_ind])
fp = homography.make_homog(q_locs[:,:2].T)
# RANSAC model for homography fitting
model = homography.RansacModel()

rank = {}
# load image features for result
for ndx in res_reg[1:]:
  locs,descr = sift.read_features_from_file(featlist[ndx])
# get matches
  matches = sift.match(q_descr,descr)
  ind = matches.nonzero()[0]
  ind2 = matches[ind]
  tp = homography.make_homog(locs[:,:2].T)
# compute homography, count inliers. if not enough matches return empty list
  try:
     H,inliers = homography.H_from_ransac(fp[:,ind],tp[:,ind2],model,match_theshold=4)
  except:
     inliers = []
# store inlier count
  rank[ndx] = len(inliers)
# sort dictionary to get the most inliers first
sorted_rank = sorted(rank.items(), key=lambda t: t[1], reverse=True)
res_geom = [res_reg[0]]+[s[0] for s in sorted_rank]
print 'top matches (homography):', res_geom
# plot the top results
imagesearch.plot_results(src,res_reg[:8])
imagesearch.plot_results(src,res_geom[:8])