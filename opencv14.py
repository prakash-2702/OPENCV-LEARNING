import cv2
import numpy as np 
# THRESHOLDING is basically segmentation technique used to separte object from its background
# comparing each pixel value with a threshold value
img=cv2.imread('bw.jpg',0)
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
imager=np.zeros(th1.shape,dtype='uint8')
#if value of pixel less than 127 then 0 else 255
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# upto threshold value is not changed and after it attains threshold value
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# less than threshold zero then value remains same
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# less than threshold reamins same then zero
cv2.imshow('image',img)
cv2.imshow('thresh1',th1)
cv2.imshow('thresh2',th2)
cv2.imshow('thresh3',th3)
cv2.imshow('thresh4',th4)
cv2.imshow('thresh5',th5)
cv2.imshow('imager',imager)
cv2.waitKey(0)
cv2.destroyAllWindows() 
# here we have given global value of threshold means value of threshold wil be same for each pixel