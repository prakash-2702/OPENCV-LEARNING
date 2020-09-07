import cv2
import numpy as np
#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)
def click_event(event,x,y,flags,param):
#callback function
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,':',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY=str(x)+','+str(y)
        cv2.putText(img,strXY,(x,y),font,1,(255,255,255),1)
        cv2.imshow('image',img)
    
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        strBGR=str(blue)+','+str(red)+','+str(green)
        print(strBGR)
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(img,strBGR,(x,y),font,1,(255,255,255),1)
        cv2.imshow('image',img)
    

img=cv2.imread('expo.jpg')
# for creating black image
#img=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)  
#window name should be same    
cv2.waitKey(0)
cv2.destroyAllWindows()
        
        
