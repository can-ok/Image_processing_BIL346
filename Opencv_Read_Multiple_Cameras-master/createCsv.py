import cv2
import csv


cap0=cv2.VideoCapture(0)
#Set frame size
cap0.set(cv2.CAP_PROP_FRAME_WIDTH, 250)
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT, 250)

counter=0
with open('log.csv','w',newline='') as f:

    while True:
        ret0,frame0=cap0.read()

        filedname=['center']
        thewriter=csv.DictWriter(f,fieldnames=filedname)
        thewriter.writeheader()
        img_path="/home/canok/Desktop/Car/CaptureWebcam/CreateIMG/IMG/image"+str(counter)+".jpg"

        cv2.imshow('frame3',frame0)
    
        cv2.imwrite(img_path,frame0)

    #save the csv

        thewriter.writerow({'center':img_path})
        counter+=1
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break
