# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:05:05 2016

@author: user
"""
import sys
sys.path.append('../ch1/')
import imtools
from numpy import *
from PIL import Image
import pickle
from scipy.cluster.vq import *
# get list of images
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
# k-means
projected = whiten(projected)
centroids,distortion = kmeans(projected,4)
code,distance = vq(projected,centroids)
# plot clusters
for k in range(4):
  ind = where(code==k)[0]
  figure()
  gray()
  for i in range(minimum(len(ind),40)):
    subplot(4,10,i+1)
    imshow(immatrix[ind[i]].reshape((25,25)))
    axis('off')
show()
from PIL import Image, ImageDraw
import hcluster 
# height and width
h,w = 1200,1200
# create a new image with a white background
img = Image.new('RGB',(w,h),(255,255,255))
draw = ImageDraw.Draw(img)
# draw axis
draw.line((0,h/2,w,h/2),fill=(255,0,0))
draw.line((w/2,0,w/2,h),fill=(255,0,0))
# scale coordinates to fit
projected = array([dot(V[[0,1]],immatrix[i]-immean) for i in range(imnbr)])
#m=V[[0,1]]
#n= array([dot(V[[0,1]],immatrix[0]-immean)])


scale = abs(projected).max(0)
scaled = floor(array([ (p / scale) * (w/2-20,h/2-20) +
                         (w/2,h/2) for p in projected]))
w=(projected[0]/scale)
# paste thumbnail of each image
for i in range(imnbr):
  nodeim = Image.open(imlist[i])
  #small picture
  nodeim.thumbnail((25,25))
  ns = nodeim.size
  #根据图像的位置确定25*25的边界
  box=(int(scaled[i][0]-ns[0]//2),int(scaled[i][1]-ns[1]//2),
                 int(scaled[i][0]+ns[0]//2+1),int(scaled[i][1]+ns[1]//2+1))
  img.paste(nodeim,box)
                  #  tree = hcluster.hcluster(projected)
#hcluster.draw_dendrogram(tree,imlist,filename='fonts.png')

figure()
imshow(img)
axis('off')
img.save('pca_font.jpg')
show()