import numpy as np
import cv2

import sys


img=cv2.imread("brainorg.png",0)
clahe=cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cll=clahe.apply(img)

cv2.imwrite("brainorg0.png",cll)
