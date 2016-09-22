# -*- coding: utf-8 -*-
from PIL import Image
from numpy import *
import os
from scipy.ndimage import measurements,morphology
pil_im = Image.open('baby1.jpg')
#保存其他图片格式"""
Image.open('baby1.jpg').save('baby.bmp')
out = pil_im.rotate(45)
out.show()
pil_im.show()
#转成灰度图像"""
pil_im = Image.open('baby1.jpg').convert('L')
'''修剪图像'''
box = (100,100,400,400)
region = pil_im.crop(box)
region.show()
out = region.rotate(180)
out.show()
'''旋转再粘贴'''
region = region.transpose(Image.ROTATE_180)
pil_im.paste(out,box)
region.show()
pil_im.show()
"""压缩图片的尺寸"""
pil_im.thumbnail((128,128))
pil_im.show()
#pil_im.show()
path='D:\\Users\\user\\Anaconda2\\Scripts\\python\\CHapter'
 #for f in os.listdir(path) 
print os.listdir(path) 
#打印目录下的以jpg结尾的绝对路径"""
print get_imlist(path)
def get_imlist(path):
    """    Returns a list of filenames for 
        all jpg images in a directory. """
        
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
 