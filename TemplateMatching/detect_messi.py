import cv2
import numpy as np




full_pic=cv2.imread('messi.png')
gray_image=cv2.cvtColor(full_pic,cv2.COLOR_BGR2GRAY)

cv2.imshow("full",gray_image)

print(gray_image.shape)




face=cv2.imread('face.png',0)

print(face.shape)
w,h=face.shape[::-1]
cv2.imshow("face",face)



result=cv2.matchTemplate(gray_image, face, cv2.TM_CCORR_NORMED)

thres=0.95

loc=np.where(result >= thres)



for pt in zip(*loc[::-1]):
    cv2.rectangle(full_pic,pt,(pt[0]+w,pt[1]+h),(0,255,0),3)

cv2.imshow("Match", full_pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
