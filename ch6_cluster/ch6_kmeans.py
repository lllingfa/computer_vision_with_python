# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:47:52 2016

@author: user
"""

from scipy.cluster.vq import *
#产生两列数组
class1 = 1.5 * randn(100,2)+array([3,3])
#产生加上[5,5]的数组
class2 = randn(100,2) + array([5,5])
print array([5,5])
print class2.shape
features = vstack((class1,class2))
#kmeans
centroids,variance = kmeans(features,3)
code,distance = vq(features,centroids)
print class1[:]
print (class1[:,0])
print class1[:][0]
#visualize the result
figure()
plot ((class1[:,0]),(class1[:,1]),'*')
plot((class2[:,0]),(class2[:,1]),'r.')
axis('off')
show()
figure()
ndx = where(code==0)[0]
plot(features[ndx,0],features[ndx,1],'*')
ndx = where(code==1)[0]
plot(features[ndx,0],features[ndx,1],'r.')
plot(centroids[:,0],centroids[:,1],'go')
ndx = where(code==2)[0]
plot(features[ndx,0],features[ndx,1],'b.')
plot(centroids[:,0],centroids[:,1],'go')
axis('off')
show()
