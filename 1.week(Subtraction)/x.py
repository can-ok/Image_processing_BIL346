import cv2
import numpy as np

img=cv2.imread('xx.png')
img2=cv2.imread('1.png')

width,height=img.shape[:2]
sub=cv2.subtract(img2,img)

print("Widh:",width)
for i in range(0,width):
    for y in range(0,height):
        img[i][y]=img[i][y]-img2[i][y]

cv2.imshow('Sonuc1',img)

cv2.imshow('Sonuc2',sub)

cv2.waitKey(0)
