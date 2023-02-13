import numpy as np
import cv2
image = cv2.imread("color.jpeg")
(B,G,R) = cv2.split(image)
cv2.imshow("B",B)
cv2.imshow("G",G)
cv2.imshow("R",R)
cv2.imshow("Image",cv2.merge([B,G,R]))
zeros = np.zeros(image.shape[:2],dtype="uint8")
cv2.imshow("Blue" , cv2.merge([B,zeros,zeros]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Red", cv2.merge([zeros,zeros,R]))
cv2.waitKey(0)
