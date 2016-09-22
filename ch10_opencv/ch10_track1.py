import lktrack
from PIL import Image
from numpy import *
from pylab import *

##imnames = ['viff.000.ppm', 'viff.001.ppm',
  #  'viff.002.ppm', 'viff.003.ppm', 'viff.004.ppm']
imnames = ['../pcv_data/data/Merton1/images/001.jpg','../pcv_data/data/Merton1/images/002.jpg','../pcv_data/data/Merton1/images/003.jpg']
# track using the LKTracker generator
lkt = lktrack.LKTracker(imnames)
for im,ft in lkt.track():
    print 'tracking %d features' % len(ft)

# plot the tracks
figure()
imshow(im)
for p in ft:
   plot(p[0],p[1],'bo')
for t in lkt.tracks:
  plot([p[0] for p in t],[p[1] for p in t])
axis('off')
show()