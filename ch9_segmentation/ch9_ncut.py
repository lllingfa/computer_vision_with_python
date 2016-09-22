import ncut
from scipy.misc import imresize
from PIL import Image
from numpy import *
from pylab import *
import sys
sys.path.append('../ch1/')
import rof

im2= array(Image.open('../pcv_data/data/C-uniform03.ppm'))
im1 = array(Image.open('../pcv_data/data/alcatraz1.jpg'))
im = array(Image.open('../pcv_data/data/ceramic-houses_t0.png').convert("L"))
U,T = rof.denoise(im,im,tolerance=0.001)
t = 0.4 #threshold
m,n = im.shape[:2]

# resize image to (wid,wid)
wid = 50
rim = imresize(im,(wid,wid),interp='bilinear')
rim = array(rim,'f')

# create normalized cut matrix
A = ncut.ncut_graph_matrix(rim,sigma_d=1,sigma_g=1e-2)

# cluster
code,V = ncut.cluster(A,k=3,ndim=3)

# reshape to original image size
codeim = imresize(code.reshape(wid,wid),(m,n),interp='nearest')

# plot result
figure()
imshow(codeim)
gray()
show()

import scipy.misc
scipy.misc.imsave('result.pdf',U < t*U.max())