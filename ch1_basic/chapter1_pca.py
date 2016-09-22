# -*- coding: utf-8 -*-
'''
from PIL import Image
from numpy import *
from pylab import *
import pca


imlist=['baby.jpg','baby1.jpg']
im = array(Image.open(imlist[1])) # open one image to get size
m,n = im.shape[0:2] # get the size of the images
print m,n
imnbr = len(imlist) # get the number of images
# create matrix to store all flattened images
immatrix = array([array(Image.open(im1)).flatten() for im1 in imlist],'f')
V,S,immean = pca.pca(immatrix)
# show some images (mean and 7 first modes)
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
   subplot(2,4,i+2)
   imshow(V[i].reshape(m,n))
   
show()       

'''
from PIL import Image
from numpy import *
from pylab import *
import cPickle as pickle
import os
'''主成分分析：输入：矩阵 X，其中该矩阵中存储训练数据，每一行为一返回：投影矩阵（按照维度的重要性排序）、方差和均值'''
def pca(X):
 
# 获取维数
 num_data,dim = X.shape
# 数据中心化
 mean_X = X.mean(axis=0)
 X = X - mean_X
 if dim>num_data:
# PCA- 使用紧致技巧
  M = dot(X,X.T) # 协方差矩阵
  e,EV = linalg.eigh(M) # 特征值和特征向量
  tmp = dot(X.T,EV).T # 这就是紧致技巧
  V = tmp[::-1] # 由于最后的特征向量是我们所需要的，所
  S = sqrt(e)[::-1] # 由于特征值是按照递增顺序排列的，
  for i in range(V.shape[1]):
   V[:,i] /= S 
  else:
# PCA- 使用 SVD 方法
   U,S,V = linalg.svd(X)
   V = V[:num_data] # 仅仅返回前 nun_data 维的数据才合理

# 返回投影矩阵、方差和均值
 return V,S,mean_X


def get_imlist(path):

# 返回目录中所有JPG图像的文件名列表
 return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

path = r"D:\\Users\\user\\Anaconda2\\Scripts\\python\\CHapter\\ch1"
imlist = get_imlist(path)
im = array(Image.open(imlist[0])) # 打开一幅图像，获取其大小
im = array(Image.open(imlist[0])) # 打开一幅图像，获取其大小
m,n = im.shape[0:2] # 获取图像的大小
print m,n
imnbr = len(imlist) # 获取图像的数目
print imnbr
# 创建矩阵，保存所有压平后的图像数据
immatrix = array([array(Image.open(im1)).flatten()
                          for im1 in imlist],'f')
# 执行 PCA 操作
V,S,immean = pca(immatrix)
# 显示一些图像（均值图像和前 7 个模式）
figure()
gray()
subplot(2,4,1)
#变平时注意通道数
imshow(immean.reshape(m,n,-1))
axis('off')
for i in range(2):
 subplot(2,4,i+2)
 imshow(V[i].reshape(m,n,-1))
 axis('off')
show()
#加载数据，保存数据
f = open('font_pca_modes.pkl', 'wb')
pickle.dump(immean,f)
pickle.dump(V,f)
f.close()
f = open('font_pca_modes.pkl', 'rb')
immean = pickle.load(f)
V = pickle.load(f)
f.close()
#加载保存数据
savetxt('test.txt',im,)
im = loadtxt('test.txt')