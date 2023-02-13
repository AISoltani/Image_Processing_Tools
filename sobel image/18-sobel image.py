import numpy as np
import cv2

image=cv2.imread("mycoins.jpg")
#Sobel kernel
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gx=cv2.Sobel(gray,ddepth=cv2.CV_64F,dx=1,dy=0)
gy=cv2.Sobel(gray,ddepth=cv2.CV_64F,dx=0,dy=1)

gx=cv2.convertScaleAbs(gx)
gy=cv2.convertScaleAbs(gy)

cv2.imshow("Gx",gx)
cv2.imshow("Gy",gy)

sobel=cv2.addWeighted(gx,0.5,gy,0.5,0)
cv2.imshow("Sobel Image",sobel)
cv2.waitKey(0)