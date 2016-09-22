# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *

im = array(Image.open('baby1.jpg').convert('L'),'f')
imshow(im)
'''反转图像'''
#im2 = 255 - im
#imshow(im2)
'''保证数据在100-200间'''
#im3 = (1.0/255) * im + 0
#imshow(im3)
#im4 = 255.0 * (im/255.0)**3
#imshow(im4)
print int(im.min()), int(im.max())
#print int(im3.min()), int(im3.max())
'''转换数据类型图像'''
pil_im = Image.fromarray(im)
pil_im.show()
'''数据格式返回无符号整型'''
pil_im = Image.fromarray(uint8(im))
#imshow(pil_im)