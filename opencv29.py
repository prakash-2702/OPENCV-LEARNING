import cv2
import numpy as np 
img=cv2.imread('sudoko.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,100,apertureSize=3)# aperture is just to get straight lines 
# if we increased it will get scattering lines 
cv2.imshow('image1',edges)
lines=cv2.HoughLines(edges,1,np.pi/180,200)# gives output vector of lines
# lines will be in polar coordinates
# this method is inaccurte because we get infinte lines in image

for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    xo=a*rho
    yo=b*rho
    x1=int(xo+1000*(-b))
    y1=int(yo+1000*(a))
    x2=int(xo-1000*(-b))
    y2=int(yo-1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()