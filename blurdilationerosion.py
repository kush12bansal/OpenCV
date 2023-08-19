import numpy as np
import cv2

image = cv2.imread('flag.jpg')
image= cv2.resize(image,(400,400))
cv2.imshow('Original', image)

blur= cv2.GaussianBlur(image, (5,55), 1)

kernel= np.ones((10,10), 'uint8')

dilate= cv2.dilate(image,kernel,iterations=1)
erode= cv2.erode(image,kernel, iterations=1)
 
cv2.imshow('Dilate',dilate)
cv2.imshow('Erode', erode) 
cv2.imshow('Blur', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

