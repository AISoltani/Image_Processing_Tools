import  numpy as np
import cv2

image=cv2.imread("mycoins.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#ksize ro mitoni kamo ziad koni
blur=cv2.GaussianBlur(gray,(7,7),0)
canny=cv2.Canny(blur,50,200)
cv2.imshow("Canny",canny)
cv2.waitKey(0)
