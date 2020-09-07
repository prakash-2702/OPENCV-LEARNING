# image gradient is a directional change in intensity or color of an image
import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
img=cv2.imread('messi.jpg',cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)# datatye supports negative number
lap=np.uint8(np.absolute(lap))# converting to 8 bit unsigned number
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx=np.uint8(np.absolute(sobelx))
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobely=np.uint8(np.absolute(sobely))
titles=['image','laplacian','sobelx','sobely']
images=[img,lap,sobelx,sobely]
#sobelcombine=cv2.bitwise_or(sobelx,sobely)
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()