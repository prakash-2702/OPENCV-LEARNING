import cv2
img=cv2.imread('expo.jpg',1)

img=cv2.line(img,(255,255),(255,255),(0,0,255),10)
#(image name,starting point,ending point,BGR ,thickness)

img=cv2.arrowedLine(img,(0,255),(255,255),(255,255,255),10)

img=cv2.rectangle(img,(0,0),(255,255),(255,255,255),10)
#first point will be top left point and second point will be bottom right point
#if thickness is -1 then we will get filled rectangle

img=cv2.circle(img,(400,400),40,(0,0,255),-1)

font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
#font face specifying line
img=cv2.putText(img,'OpenCV',(255,255),font,4,(255,255,255),10,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()