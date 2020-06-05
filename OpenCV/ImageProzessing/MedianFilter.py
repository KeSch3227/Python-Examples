import cv2
import numpy as np

img = cv2.imread('./Images/5.1.09.tiff')
output = cv2.medianBlur(img, ksize=5)
cv2.imshow('Input',img)
cv2.imshow('Median filter', output)
cv2.waitKey()
