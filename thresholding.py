import numpy as np
import cv2

bw= cv2.imread('flag.jpg',0)
bw= cv2.resize(bw, (400,400))
height, width= bw.shape[0:2]
cv2.imshow('Original BW', bw)


#this is the logic

binary= np.zeros([height,width,1],'uint8')
threshold= 85

for row in range(0,height):
    for col in range(0,width):
        if bw[row][col]> threshold:
            binary[row][col] = 255

# threshold= cv2.threshold(bw,threshold,255,cv2.THRESH_BINARY) this is the direct inbuilt function

cv2.imshow('SLow Binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows

