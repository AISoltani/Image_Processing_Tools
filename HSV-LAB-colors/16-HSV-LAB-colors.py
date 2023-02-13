import numpy as np
import cv2

image = cv2.imread("color.jpg")
#HSV Image
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("Orginal Image",image)
cv2.imshow("HSV Image",hsv_image)
for (name,chan) in zip("HSV",cv2.split(hsv_image)):
    cv2.imshow(name,chan)
#LAB Image
lab_image = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow("LAB Image",lab_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

for (name,chan) in zip("LAB",cv2.split(lab_image)):
    cv2.imshow(name,chan)

    
cv2.waitKey(0)