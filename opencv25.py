import cv2
import numpy as np 
img=cv2.imread('shape.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],-1,(0,0,0),5)
    print(approx.ravel())
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    if len(approx)==3:
        cv2.putText(img,'triangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(approx)
        ratio=float(w/h)
        print(ratio)
        if ratio>=0.95 and ratio<=1.05:
            cv2.putText(img,'square',(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
        else:
            cv2.putText(img,'recangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
    elif len(approx)==5:
        cv2.putText(img,'pentagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
    elif len(approx)==6:
        cv2.putText(img,'hexagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
    #else:
        #cv2.putText(img,'circle',(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))    


cv2.imshow('image',img)
cv2.imshow('gary',gray)
cv2.imshow('Thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()