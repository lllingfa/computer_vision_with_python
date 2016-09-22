import cv2
# read image
im = cv2.imread('../pcv_data/data/empire.jpg')
h,w = im.shape[:2]
print h,w
# save image
cv2.imwrite('result.png',im)
# create a grayscale version
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

# read image
im1 = cv2.imread('../pcv_data/data/fisherman.jpg')
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

# compute integral image
intim = cv2.integral(gray)

# normalize and save
intim = (255.0*intim) / intim.max()
cv2.imwrite('result.jpg',intim)

