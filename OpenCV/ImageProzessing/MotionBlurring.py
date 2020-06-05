import cv2
import numpy as np

img=cv2.imread("./Images/4.2.01.tiff")
cv2.imshow('Original',img)

size =15

# 15x15 matrix with zeros 
kernel_motion_blur= np.zeros((size,size))

# in row 7 only ones
kernel_motion_blur[int((size-1)/2),:]= np.ones(size)

# divided by the number of ones (total values) 
kernel_motion_blur = kernel_motion_blur/size

#appyling the Kernel to the input image
kernelImage= cv2.filter2D(img,-1,kernel_motion_blur)

cv2.imshow('Motion Blur', kernelImage)
cv2.waitKey()
