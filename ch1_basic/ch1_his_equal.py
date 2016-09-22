# -*- coding: utf-8 -*-

from PIL import Image
from imtools import *
'''直方图均衡化'''
im = array(Image.open('baby1.jpg').convert('L'))
#imshow(im)
im2,cdf= histeq(im)
imshow(im2)
print cdf
'''计算一组图像的均值'''
imlist=['baby.jpg','baby1.jpg']
im3=compute_average(imlist)
imshow(im3)
