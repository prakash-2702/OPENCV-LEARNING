import cv2
img=cv2.imread('expo.jpg')
print(img.shape)
#tuple of no of rows,columns,channels
print(img.size)
#total no of pixels
print(img.dtype)
#image datatype
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
cv2.imshow('image',img)  
cv2.waitKey(0)
cv2.destroyAllWindows()
# for region of interest we should know the co-ordinates which is found out by callback function
'''
example 
suppose we want to copy one object in image to another place
so first find out coordinates
like
splitpart=img[100:150,200:250]
img[300:350,400:450]=splitpart

'''

