import cv2
img1=cv2.imread('expo.jpg')
img2=cv2.imread('messi.jpg')
img1=cv2.resize(img1,(512,512))
img2=cv2.resize(img2,(512,512))
#size should be same oherwise it will show error
#img=cv2.add(img1,img2)
#img=cv2.addWeighted(img1,0.9,img2,0.1,100)
#(image1,priority,image2,priority,scalar)
#img=saturate(image1*ALPHA+image2*BETA+SCALAR)
#scalar gives hazy look
img=cv2.absdiff(img1,img2)
cv2.imshow('image',img)  
cv2.waitKey(0)
cv2.destroyAllWindows()
