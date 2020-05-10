import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv.imread('messi.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('messi.png',0)
w, h = template.shape[::-1]
result = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv.rectangle(img_rgb,max_val,top_left,bottom_right, (0,0,255), 2)


cv.imwrite('res.png',img_rgb)
