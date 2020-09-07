import cv2
from matplotlib import pyplot as plt
# matplotlib reads image in RGB format
import numpy as np
img=cv2.imread('bubble.jpeg',1)
cv2.imshow('image',img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows() 
'''
for i in range(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
'''

