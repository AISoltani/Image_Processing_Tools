import cv2
#Horizontal
image=cv2.imread('cameraman.tif')
cv2.flip(image,1,image)
cv2.imshow("Horizontal",image)


#Vertical
image=cv2.imread('cameraman.tif')
cv2.flip(image,0,image)
cv2.imshow("Vertical",image)

#Both
image=cv2.imread('cameraman.tif')
cv2.flip(image,-1,image)
cv2.imshow("Both",image)
cv2.waitKey(0)
