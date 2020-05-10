import cv2

cap0=cv2.VideoCapture(1)
#Set frame size
cap0.set(cv2.CAP_PROP_FRAME_WIDTH, 250)
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT, 250)

#cap1 = cv2.VideoCapture(3)
# set frame kordinat cap1.set(2,160)

while True:
    ret0,frame0=cap0.read()
    #ret1,frame1=cap1.read()

    cv2.imshow('frame',frame0)

    #cv2.imshow('frame2',frame1)

    key = cv2.waitKey(1)
    if key == 27:
        cv2.destroyAllWindows()
        break
