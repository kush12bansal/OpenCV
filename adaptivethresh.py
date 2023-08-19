import numpy as np
import cv2

img= cv2.imread('sudoku.jpg',0)
img= cv2.resize(img, (400,400))
cv2.imshow('Original', img)

ret, thresh= cv2.threshold(img,70,255,cv2.THRESH_BINARY)

cv2.imshow("binary basic", thresh)

adaptive_thresh= cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('Adaptive thresh', adaptive_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows