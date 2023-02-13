import cv2
import numpy as np
 
image = cv2.imread('cameraman.tif')
 
M = np.ones(image.shape, dtype = "uint8") * 100
 
cv2.imshow("Original", image)
cv2.waitKey(0)
 
added = cv2.add(image, M)
cv2.imshow("Added", added)
 
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
