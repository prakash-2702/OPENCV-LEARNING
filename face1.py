import cv2
# positive ad negative images
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# classifier is trained to detect positive images(objects that we want to detect)
# scalefactor-parameter specifying how much image size is reduced at image scale
# minneighbors-parameter specifying how many neighbors each candidate rectangle should have to retain it
eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    _,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
         break
cap.release() 