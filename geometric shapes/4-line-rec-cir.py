import cv2
import numpy as np
black=np.zeros((300,300,3),dtype="uint8")

# cv2.line(black,(150,0),(150,300),(255,255,0),10)
# cv2.rectangle(black,(130,130),(300,170),(0,255,0),-1)
# black[130:170,:]=(-160,255,0)
# (h,w)=black.shape[:2]
# #for i in range(10,120,10):
# #   black2=cv2.circle(black,(int(h/2),int(w/2)),i,(255,0,0),2)
# b=np.random.randint(0,255)
# g=np.random.randint(0,255)
# r=np.random.randint(0,255)
# color=(b,g,r)
# h2=np.random.randint(0,h)
# w2=np.random.randint(0,w)
# cv2.circle(black,(h2,w2),100,color,2)
# cv2.imshow("black",black)


image=cv2.imread("cameraman.tif")
kernel = (7,7)

#simple blue
#simple_blur = cv2.blur(image.copy(),kernel)
#cv2.imshow("Simple Blur",simple_blur)
cv2.imshow("Simple Blur",image)
cv2.waitKey(0)
#Gussian blur

#Median blue


cv2.waitKey(0)
