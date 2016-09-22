from PIL import Image
from pylab import *
'''求图像的轮廓'''
# read image to array
im = array(Image.open('baby1.jpg').convert('L'))
# create a new figure
figure()
# don’t use colors
gray()
# show contours with origin upper left corner,以原来的图像的起点画图
contour(im, origin='image')
#以左上方为零点
#contour(im)
#与原图像一样大小
axis('equal')
axis('off')
'''直方图显示点的分布'''
figure()
hist(im.flatten(),128)
show()
