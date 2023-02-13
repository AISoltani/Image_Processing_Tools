import numpy as np
import cv2

image=cv2.imread('cameraman.tif')
m=np.float32([[1,0,35],[0,1,40]])
cv2.warpAffine(image,m,(image.shape[1],image.shape[0]),image)
#or
image=cv2.warpAffine(image,m,(image.shape[1],image.shape[0]))
cv2.imshow("Transition",image)
cv2.waitKey(0)
