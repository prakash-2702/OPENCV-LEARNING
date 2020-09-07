import cv2
import numpy as np 
# contours is a python list of all contours in image.
# each contour is a numpy array of x,y coordinates of boundary points of object
img=cv2.imread('logo.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,255,0),3)# -1 to draw all contours
cv2.imshow('image',img)
cv2.imshow('gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()