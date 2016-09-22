# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:19:28 2016

@author: user
"""

from PIL import Image
from pylab import *
from numpy import *
sys.path.append('../ch1/')
import imtools, pca

# Get list of images and their size
imlist = imtools.get_imlist('../pcv_data/data/selectedfontimages/a_selected_thumbs/') # fontimages.zip is part of the book data set
im = array(Image.open(imlist[0])) # open one image to get the size 
m,n = im.shape[:2]

# Create matrix to store all flattened images
immatrix = array([array(Image.open(imname)).flatten() for imname in imlist],'f')

# Perform PCA
V,S,immean = pca.pca(immatrix)

# Show the images (mean and 7 first modes)
# This gives figure 1-8 (p15) in the book.
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))
show()
#加载数据，保存数据
f = open('a_pca_modes.pkl', 'wb')
pickle.dump(immean,f)
pickle.dump(V,f)
f.close()
'''
f = open('font_pca_modes.pkl', 'rb')
immean = pickle.load(f)
V = pickle.load(f)
f.close()
'''