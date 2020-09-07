import cv2 
import numpy as np 
#template matching is a method of searching and finding the location of template inside larger image
img=cv2.imread('messi.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template=cv2.imread('template.jpg',o)#here consider the image is face of messi
w,h=template.shape[::-1]# to get in reverse order

res=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
print(res)#it gives pixel matrix
threshold=0.8;
loc=np.where(res>=threshold)
print(loc)#it will give a filtered points of res starting with the greater values
for pt in zip(*loc[::-1]):# for greater than one template
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()