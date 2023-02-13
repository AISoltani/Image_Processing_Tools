from skimage.filters import threshold_otsu, threshold_adaptive
import cv2

image = cv2.imread("1-7.jpg")
gray = image#cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Simple thresholding

#(T,thresh) = cv2.threshold(gray.copy(),100,255,cv2.THRESH_BINARY)
#(T2,thresh1) = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
#cv2.imshow("Simple Thresholding",thresh)
#cv2.imshow("Simple Thresholding_INV",thresh1)
#cv2.waitKey(0)
#print("Threshold Value",T)
#cv2.destroyAllWindows()


#Otsu thresholding

#(T2,thresh2) = cv2.threshold(gray.copy(),0,255,cv2.THRESH_OTSU)
#cv2.imshow("Otsu Thresholding",thresh2)
#cv2.waitKey(0)
#print("Threshold Otsu Value:",T2)
#cv2.destroyAllWindows()


#Adaptive Thresholding

#thresh3=cv2.adaptiveThreshold(gray.copy(),255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,35,10)
#cv2.imshow("Adaptive Threshold",thresh3)
#cv2.imshow("Adaptive Threshold Bitwise",cv2.bitwise_not(thresh3))
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#Scikit Image Thresholding

thresh4 = (threshold_adaptive(gray.copy(),35,offset=10)).astype("uint8")*255
cv2.imshow("Scikit Thresholding",thresh4)
cv2.imshow("Scikit Thresholding Bitwise",cv2.bitwise_not(thresh4))
cv2.waitKey(0)
cv2.destroyAllWindows()


#Show Forground


cv2.imshow("Forground",cv2.bitwise_and(image.copy(),image.copy(),mask = cv2.bitwise_not(thresh4)))
cv2.waitKey(0)
cv2.destroyAllWindows()























