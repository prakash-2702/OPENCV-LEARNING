import cv2
import numpy as np
# HSV (HUE ,SATURATION,VALUE)
# hue corresponds to color component (0-360)
# saturation corresponds to amount of color(0-100%)
# value is basically brihtness of color(0-100%)
# cv2.namedWindow('tracking')
while (1):
    frame=cv2.imread('bubble.jpeg',1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_b=np.array([110,50,50])
    u_b=np.array([130,255,255])
    mask=cv2.inRange(hsv,l_b,u_b)
    '''
    we can create trackbar for deciding l_b and u_b values
    we can create trackbar for lower and upper values  for hue , saturation and value
    its application in video capture for detecting particular color
    In OpenCV, a mask image is of type uint8_t .
    Pixels of value 0xFF are true and pixels of value 0 are false. 
    A mask can be applied on an image of the same dimensions, but of any type. 
    By applying a mask M on an image I , the pixels of I whose corresponding pixel in M are true are copied into a new image
   
    '''
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    key=cv2.waitKey(0)
    if key==27:
        break

cv2.destroyAllWindows()

