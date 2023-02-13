import cv2
import numpy as np
 
# Load our new image
image = cv2.imread('cameraman.tif', 0)
 
cv2.imshow('Original', image)
cv2.waitKey(0) 
 
# Values below 127 goes to 0 (black, everything above goes to 255 (white)
ret,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh1)
cv2.waitKey(0) 
 
 
 
# Using adaptiveThreshold
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY, 3, 5) 
cv2.imshow("Adaptive Mean Thresholding", thresh) 
cv2.waitKey(0) 
 
# Using adaptiveThreshold + GaussianBlur
blur = cv2.GaussianBlur(image,(5,5),0)
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY, 3, 5) 
cv2.imshow("Adaptive Mean Thresholding with GaussianBlur", thresh) 
cv2.waitKey(0) 
 
 
ret2,th2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("Otsu's Thresholding", th2) 
cv2.waitKey(0) 
 
# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(image,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("Guassian Otsu's Thresholding", th3) 
cv2.waitKey(0)
 
cv2.destroyAllWindows()
