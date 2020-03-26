import cv2
import numpy as np

img=cv2.imread('./Images/lenna.jpg',cv2.IMREAD_COLOR)
nun_rows,nun_cols= img.shape[:2]
translation_matrix=np.float32([[1,0,70],[0,1,100]])
img_translation=cv2.warpAffine(img,translation_matrix, (nun_cols,nun_rows),cv2.INTER_LINEAR)
cv2.imshow('Original', img)
cv2.imshow('Translation', img_translation)
cv2.waitKey()
