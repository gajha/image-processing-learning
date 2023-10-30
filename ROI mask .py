import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('/pexels-pixabay-207496.jpg', cv2.IMREAD_GRAYSCALE)#reading an image
plt.title("Histogram for given Image'  ")#initial histogram of an image
plt.xlabel("Value")
plt.ylabel("pixels Frequency")
#hist function is used to plot the histogram of an image.
plt.hist(img)

ret,ROImg = cv2.threshold(img,150,255,cv2.THRESH_BINARY)#setting a thireshold value in order to determine the ROI

histr = cv2.calcHist(ROImg,[0],None,[256],[0,256])#histogram calculation of the ROI image
plt.plot(histr)
plt.show()
plt.imshow(img, cmap='gray')
plt.imshow(ROImg, cmap='gray')#final ROI mapped image
