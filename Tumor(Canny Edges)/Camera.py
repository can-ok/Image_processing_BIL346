import cv2
import numpy as np

cap =cv2.VideoCapture(0)

def x(frame):
    clahe=cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cll=clahe.apply(frame)
    return cll

while True:
    ret,frame=cap.read()

    canny_edge=cv2.Canny(frame,65,150)

    cv2.imshow("Frame",canny_edge)

    cv2.imshow("canny_edge", x(canny_edge))
    key=cv2.waitKey(1)
    if(key==120):# ascii code X=120
        break


cap.release()
cv2.destroyAllWindows()
