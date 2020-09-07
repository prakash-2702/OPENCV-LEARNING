import cv2
import numpy as np 
'''
pyramid representation is a type of multi scale signal 
representation in which a signal or image is subject to repeated 
smoothing and subsampling
'''
# two types are gaussain and laplacian pyramid
# Gaussain pyramid is repeat filtering and subsampling of image
# gaussian pyramid:pyrUp and pyrDown methods
# laplacian pyramid are formed by difference between that level 
# in gaussian pyramid and expanded version of its upper level in gaussian pyramid
# laplacian pyramid looks like edge detection
img=cv2.imread('bubble.jpeg')
layer=img.copy()
gp=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)
layer=gp[5]
cv2.imshow('upper level',layer)
lp=[layer]
#for i in range(5,0,-1):
i=3
gaussian_extended=cv2.pyrUp(gp[i])
laplacian=cv2.subtract(gp[i-1] , gaussian_extended)
cv2.imshow(str(i),laplacian)
cv2.imshow('original',img)
cv2.waitKey(0) 
cv2.destroyAllWindows()