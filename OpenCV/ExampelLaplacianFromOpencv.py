import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./Images/4.1.06.tiff',0)

#Laplacian Filter with 64F 
laplacian = cv2.Laplacian(img,cv2.CV_64F)

# Sobelfilter with 1 Kernel size and 64F
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

# Original in gray
plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

#Sobel filter with unit8 conversion
plt.subplot(2,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])

#Sobel filter with 64F with absolute to unit8 conversion
plt.subplot(2,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

#Laplacian filter output
plt.subplot(2,3,4),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian CV_64F'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,5),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X '), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,6),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
