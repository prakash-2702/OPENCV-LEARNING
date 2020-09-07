import cv2
from matplotlib import pyplot as plt
# matplotlib reads image in RGB format
# morphological transformation are some simple operations based on image shape
# it is normlly performed on binary images
# a kernel tells you how to change the value of any given pixel by combining it with
# different amounts of neighboring pixels
import numpy as np
img=cv2.imread('bubble.jpeg',cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
kernal=np.ones((5,5),np.uint8)#white image
# it is the that we want to apply on image
dilation=cv2.dilate(mask,kernal,iterations=4)
erosion=cv2.erode(mask,kernal,iterations=4)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)#erosion followed by dilation
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)#dilation followed by erosion
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
titles=['image','mask','dilation','erosion','opening','closing','gradient']
images=[img,mask,dilation,erosion,opening,closing,mg]
for i in range(7):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

