import cv2
import numpy as np

img=cv2.imread("./Images/5.1.13.tiff", cv2.IMREAD_GRAYSCALE)
rows,cows= img.shape

sobel_horizontal_Kernelsize3=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)
sobel_vertical_Kernelsize3=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)

sobel_horizontal_Kernelsize7=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=7)
sobel_vertical_Kernelsize7=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=7)

print(cv2.CV_64F)

cv2.imshow('Original',img)
cv2.imshow('Sobel horizontal 3',sobel_horizontal_Kernelsize3)
cv2.imshow('Sobel vertical 3', sobel_vertical_Kernelsize3)
cv2.imshow('Sobel horizontal 7',sobel_horizontal_Kernelsize7)
cv2.imshow('Sobel vertical 7', sobel_vertical_Kernelsize7)

cv2.waitKey(0)
