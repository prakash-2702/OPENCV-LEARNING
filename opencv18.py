import cv2
# smoothing/blurring to reduce noise in image
# homogenous filter each output pixel is the mean of its kernel neighbours
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('salt.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)#homogenous filter
blur=cv2.blur(img,(5,5))# averaging algorithm
gblur=cv2.GaussianBlur(img,(5,5),10)# gaussian method
# sigma x
median=cv2.medianBlur(img,5)
bilateral=cv2.bilateralFilter(img,9,75,75)# for preserving edges
'''
sigmaColor – Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace ) will be mixed together, resulting in larger areas of semi-equal color.
sigmaSpace – Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see sigmaColor ). When d>0 , it specifies the neighborhood size regardless of sigmaSpace . Otherwise, d is proportional to sigmaSpace .
'''
titles=['image','dst','blur','gblur','median','bilateral']

images=[img,dst,blur,gblur,median,bilateral]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
