import cv2

cap= cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError ("Cannot open Webcam")

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,None,fx=1,fy=1, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input',frame)
    c= cv2.waitKey(1)
    #ASCII 27 is ESC
    if c==27:
        break
    
cap.release()
cv2.destroyAllWindows()
