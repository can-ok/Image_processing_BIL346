import cv2


cap=cv2.VideoCapture(0)


while True:
    ret,frame=cap.read()
    canny_edge=cv2.Canny(frame, 150, 200)
    cv2.imshow("canny live",canny_edge)
    key=cv2.waitKey(1)
    if(key==120):# ascii code X=120
        break

cap.release()
cv2.destroyAllWindows()
