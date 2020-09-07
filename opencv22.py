import cv2
# image blending is merging of images
import numpy as np 
apple=cv2.imread('apple.jpg')
orange=cv2.imread('orange.jpg')
# rows columns and alpha channels should be same
apple_orange=np.hstack((apple[:,:256],orange[:,256:]))
# generate gaussian pyramid
apple_copy=apple.copy()
gp_apple=[apple_copy]
for i in range(6):
    apple_copy=cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
orange_copy=orange.copy()
gp_orange=[orange_copy]
for i in range(6):
    orange_copy=cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)
# generate laplacian pyramid
#.........
#now add left and right halves of images at each level
appple_orange_pyramid=[]
n=0
for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    n+=1
    cols,rows,ch=apple_lap.shape
    laplacian=np.hstack((apple_lap[:,:int(cols/2)],orange_lap[:,int(cols/2):]))
    appple_orange_pyramid.append(laplacian)
# now reconstruct
appple_orange_reconstuct=appple_orange_pyramid[0]
for i in range(1,6):
     appple_orange_reconstuct=cv2.pyrUp(appple_orange_reconstuct)
     appple_orange_reconstuct=cv2.add(appple_orange_pyramid[i],appple_orange_reconstuct)

cv2.imshow('apple_orange_reconstruct',appple_orange_reconstuct)
cv2.waitKey()
cv2.destroyAllWindows()