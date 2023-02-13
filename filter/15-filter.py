import numpy as np
import cv2

image=cv2.imread("content.jpg")
kernel = (7,7)

#simple blue
simple_blur = cv2.blur(image,kernel)
cv2.imshow("Simple Blur",simple_blur)
cv2.imshow("Orginal",image)

#Gussian blur
Gussian_blur = cv2.GaussianBlur(image,kernel,0)
cv2.imshow("Gussian Blur",Gussian_blur)

#Median blue
Median_Blur = cv2.medianBlur(image,7)
cv2.imshow("Median Blur,",Median_Blur)
cv2.waitKey(0)

