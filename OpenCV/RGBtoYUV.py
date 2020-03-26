import cv2
img=cv2.imread('./Images/lenna.jpg',cv2.IMREAD_COLOR)
yvu_img= cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
cv2.imshow("YVU Scale",yvu_img)
cv2.waitKey()

#speratet the three channels
# Alternative 1
y,u,v= cv2.split(yvu_img)
cv2.imshow('Y channel',y)
cv2.imshow('U channel',u)
cv2.imshow('V channel',v)
cv2.waitKey()

# Alteranive 2 (faster)
cv2.imshow('Y channel', yvu_img[:,:,0])
cv2.imshow('U channel', yvu_img[:,:,1])
cv2.imshow('V channel', yvu_img[:,:,2])
cv2.waitKey()


