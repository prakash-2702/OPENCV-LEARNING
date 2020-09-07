import cv2
img=cv2.imread('new.jpg',0)
#0 for gary scale
#1 for colour scale
#-1 for alpha channel
cv2.imshow('image',img)
k=cv2.waitKey(0) & 0xFF
#just a syantax for 64 bit machine
if k==27:
    cv2.destroyAllWindows()
elif k==ord('q'):
    cv2.imwrite('expo1.png',img)
    # for making copy of image
    cv2.destroyAllWindows()
