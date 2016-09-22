from PIL import Image
from numpy import *
from pylab import *
from scipy.misc import imresize
import graphcut

def create_msr_labels(m,lasso=False):
  """ Create label matrix for training from
  user annotations. """
  labels = zeros(im.shape[:2])

# background
  labels[m==0] = -1
  labels[m==20] = -1
# foreground

  if lasso:
     labels[m==255] = 1
  else:
     labels[m==128] = 1

  return labels

# load image and annotation map
im = array(Image.open('../pcv_data/data/alcatraz1.jpg'))
m = array(Image.open('../pcv_data/data/a.png'))

# resize
scale = 0.003
im = imresize(im,scale,interp='bilinear')
m = imresize(m,scale,interp='nearest')

# create training labels
labels = create_msr_labels(m,False)

# build graph using annotations
g = graphcut.build_bayes_graph(im,labels,kappa=2)

# cut graph
res = graphcut.cut_graph(g,im.shape[:2])

# remove parts in background
res[m==0] = 1
res[m==64] = 1


# plot the result
figure()
imshow(res)
gray()
xticks([])
yticks([])
savefig('labelplot.pdf')