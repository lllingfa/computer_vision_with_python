# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:00:35 2016

@author: user
"""
import sys
sys.path.append('../ch1/')
sys.path.append('../ch2/')
import pickle
import sift
import imagesearch
import imtools
import vocabulary
#nbr_images = len(imlist)
#cause of the memory error,we choose to use 100 pictures 
imlist = imtools.get_imlist('../pcv_data/data/ukbench/thumbnails/') 

nbr_images=100
featlist = [ imlist[i][:-3]+'sift' for i in range(nbr_images)]
for i in range(nbr_images):
  sift.process_image(imlist[i],featlist[i])
voc = vocabulary.Vocabulary('ukbenchtest')
voc.train(featlist,1000,10) 
with open('vocabulary.pkl', 'wb') as f:
  pickle.dump(voc,f)
print 'vocabulary is:', voc.name, voc.nbr_words
# load vocabulary
with open('vocabulary.pkl', 'rb') as f:
     voc = pickle.load(f)
# create indexer
indx = imagesearch.Indexer('test.db',voc)
indx.create_tables()
# go through all images, project features on vocabulary and insert
for i in range(nbr_images)[:100]:
   locs,descr = sift.read_features_from_file(featlist[i])
   indx.add_to_index(imlist[i],descr)
# commit to database
indx.db_commit()
from pysqlite2 import dbapi2 as sqlite
con = sqlite.connect('test.db')
print con.execute('select count (filename) from imlist').fetchone()
(1000,)
print con.execute('select * from imlist').fetchone()
(u'ukbench00000.jpg',)
src = imagesearch.Searcher('test.db')
locs,descr = sift.read_features_from_file(featlist[0])
iw = voc.project(descr)

print 'ask using a histogram...'
print src.candidates_from_histogram(iw)[:10]
src = imagesearch.Searcher('test.db')
print 'try a query...'
print src.query(imlist[0])[:10]