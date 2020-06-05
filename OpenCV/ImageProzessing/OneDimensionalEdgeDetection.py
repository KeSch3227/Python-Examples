import cv2
import numpy as np

#img=cv2.imread("./Images/5.1.12.tiff")
img=cv2.imread("./Images/4.2.01.tiff")

kernel_identity= np.array([[-1,0,1]])

output=cv2.filter2D(img,-1,kernel_identity)
cv2.imshow("Filter ",output)

cv2.waitKey(0)
