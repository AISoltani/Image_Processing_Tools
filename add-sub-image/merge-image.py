import cv2
import numpy as np
 
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')
 
cv2.imshow("ml", img1)
cv2.imshow("opencv", img2)
 
cv2.waitKey(0)
 
output_image = cv2.add(img1,img2)
cv2.imshow("out", output_image)
 
 
print(img1.shape)
print(img2.shape)
print(output_image.shape)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
