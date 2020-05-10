import cv2
import numpy as np

img=cv2.imread("x.png",0)
clahe=cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cll=clahe.apply(img)

cv2.imwrite("x0.png",cll)
