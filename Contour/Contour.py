from skimage.filters import threshold_otsu, threshold_adaptive
import cv2

image = cv2.imread("shapes.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(t,thresh) = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
cv2.imshow("Thresh",thresh)

#Contour

(_,cnts,_) = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for (i, c) in enumerate(cnts):
    cv2.drawContours(image,[c],-1,(0,255,0),2)

cv2.imshow("Contours",image)
cv2.waitKey(0)
