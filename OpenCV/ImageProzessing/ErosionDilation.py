import cv2
import numpy as np

img= cv2.imread('./Images/5.1.13.tiff')

kernel= np.ones((2,2), np.uint8)

img_erosion = cv2.erode(img,kernel,iterations=1)
img_dilation= cv2.dilate(img,kernel,iterations=1)

cv2.imshow('input',img)
cv2.imshow('erosion', img_erosion)
cv2.imshow('Dilation',img_dilation)

cv2.waitKey(0)
