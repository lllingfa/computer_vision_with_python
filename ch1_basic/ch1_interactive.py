# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *

im = array(Image.open('baby1.jpg'))
imshow(im)
print im.shape,im.dtype
value=im[1,1,1]
print value
'''生成浮点型的数据'''
im = array(Image.open('baby1.jpg').convert('L'),'f')
print im.shape,im.dtype
pil_im = Image.open('baby1.jpg')
'''用25行的数据换成250行的数据'''
im[25,:] = im[250,:]
imshow(im)
'''将某一列设为相同值'''
im[:,25] = 100
imshow(im)
'''把前100行和前50列求总和'''
print im[:100,:50].sum()
'''某一行的平均值'''
print im[25].mean()
'''最后一列'''
print im[:,-1]
'''倒数第二行'''
imshow(im[-2:])

#pil_im.show()
print 'Please click 3 points'
'''可以在图中选点'''
#x = ginput(3)
#print 'you clicked:',x
show()