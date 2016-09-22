import lktrack

#imnames = ['bt.003.pgm', 'bt.002.pgm', 'bt.001.pgm', 'bt.000.pgm']
imnames = ['../pcv_data/data/Merton1/images/001.jpg','../pcv_data/data/Merton1/images/002.jpg','../pcv_data/data/Merton1/images/003.jpg']
# create tracker object
lkt = lktrack.LKTracker(imnames)

# detect in first frame, track in the remaining
lkt.detect_points()
lkt.draw()
for i in range(len(imnames)-1):
  lkt.track_points()
  lkt.draw()