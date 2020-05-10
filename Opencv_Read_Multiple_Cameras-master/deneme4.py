from threading import Thread
import cv2



def video(id):
    cap0=cv2.VideoCapture(id)
#Set frame size
    cap0.set(cv2.CAP_PROP_FRAME_WIDTH, 250)
    cap0.set(cv2.CAP_PROP_FRAME_HEIGHT, 250)

    while True:
        ret0,frame0=cap0.read()
        #ret1,frame1=cap1.read()

        cv2.imshow('frame',frame0)

        #cv2.imshow('frame2',frame1)

        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    camera1 = Thread(target = video, args = (1))
    

    camera1.start()
    