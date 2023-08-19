import numpy as np
import cv2

img= cv2.imread('shape.png', 1)
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray= cv2.resize(gray,(200,200))
thresh= cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1)

cv2.imshow('Binary', thresh)

contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2= img.copy()
img2= cv2.resize(img2, (200,200))
index= -1
thickness= 2
colour= (255,0,255)

cv2.drawContours(img2,contours,index, colour, thickness)

cv2.imshow('Contours', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



