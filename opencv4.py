import cv2
cap=cv2.VideoCapture(0)
#you can give video file name also
#we read frame by frame
fourcc=cv2.VideoWriter_fourcc(*'YUY2')
# four byte code for codec which is used for specifying the extension of video format
out=cv2.VideoWriter('output.avi',fourcc,20,(640,480))
#for saving the video
#(name of output file,fourcc code,no of frame per second,size)
print(cap.isOpened())
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        # for writing frames into file
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
cap.release()
out.release()
cv2.destroyAllWindows()



