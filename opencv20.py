import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
img=cv2.imread('messi.jpg',cv2.IMREAD_GRAYSCALE)
'''
canny edge detection:(lesser noise)
1.noise reduction
2.gradient calculation
3.non maximum suppression
4.double threshold
5.edge tracking by hysteresis
'''
canny=cv2.Canny(img,10,20)
titles=['image','canny']
images=[img,canny]

for i in range(2):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()