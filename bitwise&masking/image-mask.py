import cv2 
import numpy as np

# You can use any input format...

image = cv2.imread('cow.jpg')
cropped = image[100:600 , 150:650]
cv2.imshow("Beautiful Cow!", cropped)
cv2.waitKey(0)
 
circle = np.zeros((500,500,3), np.uint8)
cv2.circle(circle, (250, 250), 250, (255,255,255), -1) 
cv2.imshow("Circle", circle)
cv2.waitKey(0)
 
output_image = cv2.bitwise_and(cropped, circle)
cv2.imshow("Output Image", output_image)
cv2.waitKey(0)
 
cv2.destroyAllWindows()
