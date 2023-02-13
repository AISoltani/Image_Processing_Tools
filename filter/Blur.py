import cv2
import numpy as np
 
image = cv2.imread('cameraman.tif')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
 
# Creating our 3 x 3 kernel
kernel_3x3 = np.ones((3, 3), np.float32) / 9
 
# We use the cv2.fitler2D to conovlve the kernal with an image 
blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('3x3 Kernel Blurring', blurred)
cv2.waitKey(0)
 
# Creating our 7 x 7 kernel
kernel_7x7 = np.ones((7, 7), np.float32) / 49
 
blurred2 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('7x7 Kernel Blurring', blurred2)
cv2.waitKey(0)
 
cv2.destroyAllWindows()
