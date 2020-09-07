# histogram gives overall intensity distribution of image
import cv2
import numpy as np 
from matplotlib import pyplot as plt

#img=np.zeros((200,200,3),np.uint8)
#cv2.rectangle(img,(0,100),(200,200),(255,255,255),-1)
#cv2.rectangle(img,(0,0),(50,50),(255,0,0),-1)
img=cv2.imread('expo.jpg',1)
b,g,r=cv2.split(img)

cv2.imshow('image',img)

cv2.imshow('B',b)
cv2.imshow('G',g)
cv2.imshow('R',r)


plt.hist(img.ravel(),256,[0,256])#(image,max no of pixels,range)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

hist=cv2.calcHist([img],[0],None,[256],[0,256])#(image,no of channels,mask,hist,range)
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()