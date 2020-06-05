import cv2
import numpy as np

img=cv2.imread("./Images/4.2.01.tiff", cv2.IMREAD_GRAYSCALE)

# 127 is the value of the threshold
rest1,img2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
rows,cows= img.shape

laplacian64 =cv2.Laplacian(img2,cv2.CV_64F)

#konvert too uint16 and this is all black by binary image
laplacian16 =cv2.Laplacian(img2,cv2.CV_16U)

cv2.imshow('Original',img)
cv2.imshow('laplacian 64F',laplacian64)
cv2.imshow('laplacian 16U',laplacian16)
cv2.imshow('Black white image',img2)

#the easy way laplacian with threshold
canny= cv2.Canny(img, 50, 255)
cv2.imshow('Canny',canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
