import numpy as np
import cv2


img= cv2.imread("flag.jpg",1)
print(img)
print(len(img))
print(img.shape)
print(img.dtype) #unit is unequal integer of 8
print(img.size)