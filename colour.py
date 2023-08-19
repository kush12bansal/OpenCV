import numpy as np
import cv2

colour= cv2.imread('flag.jpg')
colour= cv2.resize(colour, (400,400)) #(lenght,width)
cv2.imshow('Image',colour)

cv2.moveWindow('Image',0,0)
print(colour.shape)
height,width,channel= colour.shape

b,g,r= cv2.split(colour)
rgb_split= np.empty([height,width*3,3], 'uint8')


rgb_split[:,0:width]= cv2.merge([b,b,b])
rgb_split[:, width:width*2]= cv2.merge([g,g,g])
rgb_split[:, width*2:width*3]= cv2.merge([r,r,r])

# HSV colour concatenation(changing) 
#h- hue, s- saturation, v-value

hsv= cv2.cvtColor(colour,cv2.COLOR_BGR2HSV)

h,s,v= cv2.split(hsv)
hsv_split= np.concatenate((h,s,v), axis=1)
cv2.imshow('hsv Split', hsv_split)




cv2.imshow("Channels", rgb_split)
cv2.moveWindow('Channels',0,0)
cv2.waitKey(0)
cv2.destroyAllWindows()