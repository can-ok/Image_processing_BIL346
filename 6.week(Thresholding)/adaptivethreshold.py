import cv2
import numpy as np



img_gray=cv2.imread("Dot_Blot.jpg",0)

mean_c = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 71, 12)

cv2.imshow("thresed",mean_c)
cv2.waitKey()
