import cv2
# ADAPTIVE THRESHOLD calculates value for each pixel 
img=cv2.imread('sudoko.jpg',0)
th2 =cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,1)
th3 =cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,1)
cv2.imshow('image',img)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.waitKey(0)
cv2.destroyAllWindows() 