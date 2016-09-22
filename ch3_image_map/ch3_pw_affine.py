# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:41:10 2016

@author: user
"""
from PIL import Image
from numpy import *
import matplotlib.delaunay as md
x,y = array(random.standard_normal((2,100)))
centers,edges,tri,neighbors = md.delaunay(x,y)
figure()
for t in tri:
  t_ext = [t[0], t[1], t[2], t[0]] # add first point to end
  plot(x[t_ext],y[t_ext],'r')
plot(x,y,'*')
axis('off')
show()
