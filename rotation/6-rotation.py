import numpy as np
import cv2

image = cv2.imread("cameraman.tif")
(h,w) = image.shape[:2
x = w/2
y = w/2
m = cv2.getRotationMatrix2D((x,y),-90,1)
cv2.warpAffine(image,m,(w,h),image)
cv2.imshow("Rotate",image)
cv2.waitKey(0)