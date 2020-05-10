import cv2
import numpy as np

cap =cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow("Frame", frame)
    frame2=cv2.GaussianBlur(frame, (3,3), 0)
    canny_edge=cv2.Canny(frame2,65,150)

    cv2.imshow("canny_edge", canny_edge)
    key=cv2.waitKey(1)
    if(key==120):# ascii code X=120
        break


cap.release()
cv2.destroyAllWindows()
