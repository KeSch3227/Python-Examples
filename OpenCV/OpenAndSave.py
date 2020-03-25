import cv2
# IMREAD_GRAYSCALE beschreibt einen Modus zum laden des Bildes 
gray_img=cv2.imread('/home/kevin/Schreibtisch/OpenCvTest/Image/lenna.jpg',cv2.IMREAD_GRAYSCALE)
g=cv2.split(gray_img)
cv2.imshow("Graysclae",gray_img)
cv2.imwrite('/home/kevin/Schreibtisch/OpenCvTest/Image/lenna_gray.jpg',gray_img)
cv2.waitKey()
