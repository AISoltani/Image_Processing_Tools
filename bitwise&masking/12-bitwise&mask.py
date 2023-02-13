import numpy as np
import cv2

image = cv2.imread("cameraman.tif")
mask1 = np.zeros((image.shape[:2]),dtype="uint8")
mask2 = np.zeros((image.shape[:2]),dtype="uint8")

#rectange or circle mask
cv2.rectangle(mask1,(100,100),(156,156),255,-1)
cv2.circle(mask2,(int(mask2.shape[1]/2),int(mask2.shape[0]/2)),50,255,-1)
cv2.imshow("Mask 1",mask1)
cv2.imshow("Mask 2",mask2)
cv2.imshow("Filter 1",cv2.bitwise_and(image.copy(),image.copy(),mask=mask1))
cv2.imshow("Filter 2",cv2.bitwise_and(image,image,mask=mask2))

cv2.waitKey(0)
cv2.destroyAllWindows()
