import numpy as np
import matplotlib.pyplot as plt
import tkinter
import cv2
#Plot Histogram
image = cv2.imread("color.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
hist = cv2.calcHist(gray,[0],None,[256],[0,256])
plt.figure()
plt.title("Histogram Of This Image")
plt.xlabel("Bins")
plt.ylabel("Sharp(#) Of Pixels")
plt.plot(hist)
plt.xlim([0,256])

#Normalizing Histogram
hist /=hist.sum()
plt.figure()
plt.title("Normalaized Histogram Of This Image")
plt.xlabel("Bins")
plt.ylabel("Sharp(#) Of Pixels")
plt.plot(hist)
plt.xlim([0,256])
#Color Histogram
plt.figure()
colors = ("b","g","r")
chans = cv2.split(image)
for (color,chan) in zip(colors,chans):
    hist = cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist,color=color)
    plt.xlim([0,256])

plt.show()