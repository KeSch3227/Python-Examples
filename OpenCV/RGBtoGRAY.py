import cv2
img=cv2.imread('./Images/lenna.jpg',cv2.IMREAD_COLOR)
gray_img= cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Graysclae",gray_img)
cv2.waitKey()
