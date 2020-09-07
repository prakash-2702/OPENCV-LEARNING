import cv2
cap=cv2.VideoCapture(0)
#every property has a no in opencv
cap.set(3,600)
#width 
cap.set(4,600)
#height
#if this value exceeds then camera will use its default resolution
while(cap.isOpened()):
    ret,frame=cap.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




