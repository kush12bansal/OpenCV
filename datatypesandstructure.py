import numpy as np 
import cv2


# firslt in [], put size of the image and type of image
black= np.zeros([905, 1280, 3], 'uint8') #this command will indicate how many zeroes pixels have

cv2.imshow('Black', black)
print(black[0,0,:])


ones= np.ones([905, 1280, 3], 'uint8')
cv2.imshow('Ones', ones)
print(ones)


cv2.waitKey(0)
cv2.destroyAllWindows()