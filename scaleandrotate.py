import numpy as np
import cv2

img= cv2.imread('flag.jpg')
img = cv2.resize(img, (400,400))

#scale
img_half= cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img_stretch= cv2.resize(img,(600,600))
img_stretchnear= cv2.resize(img, (600,600), interpolation= cv2.INTER_NEAREST)

cv2.imshow('Half',img_half)
cv2.imshow('stretch',img_stretch)
cv2.imshow('stretch near',img_stretchnear)

#rotation

M= cv2.getRotationMatrix2D((0,0), -30, 1)
rotated= cv2.warpAffine(img,M, (img.shape[1],img.shape[0]))
cv2.imshow('Rotated', rotated)



cv2.waitKey(0)
cv2.destroyAllWindows
 
 