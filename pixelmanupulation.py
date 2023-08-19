import numpy as np
import cv2

colour= cv2.imread('flag.jpg')
colour= cv2.resize(colour,(400,400))

grey= cv2.cvtColor(colour, cv2.COLOR_BGR2GRAY)

cv2.imwrite('Grey.jpg', grey )

b= colour[:,:,0]
g= colour[:,:,1]
r= colour[:,:,2]

rgba= cv2.merge((b,g,r,g)) # last g is used for tranparency. 
#transparency is only used in png type as jpeg not supports transparency.

cv2.imwrite('rgba.png', rgba)