import cv2
import sys


import numpy as np

from matplotlib import pyplot as plt


img=cv2.imread("brain1.png",0)
plt.hist(img.ravel(),256,(0,256))
plt.show()

equ=cv2.equalizeHist(img)

res=np.hstack((img,equ))

cv2.imwrite("brain1.png ",res)
