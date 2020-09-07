import cv2
import numpy as np
img1=cv2.imread('bin1.png')
img2=cv2.imread('bin2.png')
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
bitand=cv2.bitwise_and(img1,img2)
#bitwise and operation black 0 and white 1
bitor=cv2.bitwise_or(img1,img2)
#bitwise or
bitxor=cv2.bitwise_xor(img1,img2)
#bitwise xor
bitnot=cv2.bitwise_not(img1)
#bitwise not
cv2.imshow('not',bitnot)
cv2.imshow('and',bitand)
cv2.imshow('or',bitor)
cv2.imshow('xor',bitxor)
cv2.waitKey(0)
cv2.destroyAllWindows()