import numpy as np
import cv2
image1 = np.zeros((300,300),dtype="uint8")
image2 = np.zeros((300,300),dtype="uint8")
cv2.rectangle(image1,(130,130),(170,170),(255),-1)
cv2.circle(image2,(150,150),100,255,-1)
cv2.imshow("And",cv2.bitwise_and(image1,image2))
cv2.imshow("Or",cv2.bitwise_or(image1,image2))
cv2.imshow("XOr",cv2.bitwise_xor(image1,image2))
cv2.imshow("Not 1",cv2.bitwise_not(image1))
cv2.imshow("Not 2",cv2.bitwise_not(image2))
cv2.waitKey(0)