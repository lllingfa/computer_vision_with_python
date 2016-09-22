# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 21:00:45 2016

@author: user
"""
import sys
sys.path.append('../ch2/')
import sift
from numpy import *
from PIL import Image
import pickle
import vocabulary
import imtools

imlist = imtools.get_imlist('../pcv_data/data/ukbench/thumbnails/') 
#nbr_images = len(imlist)
nbr_images=100
featlist = [ imlist[i][:-3]+'sift' for i in range(nbr_images)]
for i in range(nbr_images):
  sift.process_image(imlist[i],featlist[i])
voc = vocabulary.Vocabulary('ukbenchtest')
voc.train(featlist,1000,10)
# saving vocabulary
with open('vocabulary.pkl', 'wb') as f:
  pickle.dump(voc,f)
print 'vocabulary is:', voc.name, voc.nbr_words