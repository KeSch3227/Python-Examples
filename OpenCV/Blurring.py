import cv2
import numpy as np

img=cv2.imread("./Images/5.1.12.tiff")

rows,cols=img.shape[:2]

#generating the kernel for blurring
kernel_identity= np.array([[0,0,0],[0,1,0],[0,0,0]])
kernel_3x3=np.ones((3,3), np.float32)/9.0
kernel_5x5=np.ones((5,5), np.float32)/25.0

# the original Image
cv2.imshow('Original',img)

output=cv2.filter2D(img,-1,kernel_identity)
cv2.imshow("Identity filter",output)

#the Image with 3x3 low pass filter
output=cv2.filter2D(img,-1,kernel_3x3)
cv2.imshow("3x3 filter",output)

#the Image with 5x5 low pass filter
output=cv2.filter2D(img,-1,kernel_5x5)
cv2.imshow("5x5 filter",output)

cv2.waitKey(0)


