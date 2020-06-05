import cv2
import numpy as np

img = cv2.imread('./Images/4.2.01.tiff')

img_gaussian= cv2.GaussianBlur( img, (13,13),0)
img_bilateral= cv2.bilateralFilter(img,13,70,50)

cv2.imshow('input', img)
cv2.imshow('Gaussian filter', img_gaussian)
cv2.imshow('Bilateral fiöter', img_bilateral)
cv2.waitKey()
