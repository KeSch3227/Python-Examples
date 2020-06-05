import cv2
import numpy as np

img=cv2.imread('./Images/4.1.06.tiff')

kernel_emboss_1= np.array([[0,-1,-1],
                           [1,0,-1],
                           [1,1,0]])
kernel_emboss_2= np.array([[-1,-1,0],
                           [-1,0,1],
                           [0,1,1]])
kernel_emboss_3= np.array([[1,0,0],
                           [0,0,0],
                           [0,0,-1]])

#converting to gray
gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

output_1_black= cv2.filter2D(gray_img,-1,kernel_emboss_1)
output_1_gray= cv2.filter2D(gray_img,-1,kernel_emboss_1)+128
output_2= cv2.filter2D(gray_img,-1,kernel_emboss_2)+128
output_3= cv2.filter2D(gray_img,-1,kernel_emboss_3)+128

cv2.imshow('Original', img )
cv2.imshow('Originla in gray', gray_img)
cv2.imshow('Embossing - South West Black',output_1_black)
cv2.imshow('Embossing - South West Gray',output_1_gray)
cv2.imshow('Embossing - South East',output_2)
cv2.imshow('Embossing - North West',output_3)

cv2.waitKey()
