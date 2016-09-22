from PIL import Image
from numpy import *
from scipy.ndimage import filters
#彩色转成灰度图
im = array(Image.open('baby_16.jpg').convert('L'))
#灰度图单通道高斯滤波
im2 = filters.gaussian_filter(im,2)
#彩色图多通道高斯滤波
im1 = array(Image.open('baby_16.jpg'))

im3 = zeros(im1.shape)

for i in range(3):
 im3[:,:,i] = filters.gaussian_filter(im1[:,:,i],5)
im3 = uint8(im3)

#显示结果
figure
subplot(2,2,1)
imshow(im)
subplot(2,2,2)
imshow(im2)
subplot(2,2,3)
imshow(im1)
subplot(2,2,4)
imshow(im3)