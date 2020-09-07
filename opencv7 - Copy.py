import cv2
import datetime
cap=cv2.VideoCapture(0)
#every property has a no in opencv
cap.set(3,600)
#width 
cap.set(4,600)
#height
#if this value exceeds then camera will use its default resolution
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        #fonr face specifying line
        text='WIDTH:'+str(cap.get(3))+'HEIGHT:'+str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,50),font,1,(255,255,255),1,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()
