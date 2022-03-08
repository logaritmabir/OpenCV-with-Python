import cv2 as cv
from cv2 import imshow
import numpy as np

img = cv.imread("kawga.jpg")

res = cv.resize(img,None,fx=0.6,fy=0.6,interpolation=cv.INTER_LINEAR_EXACT)
res2 = cv.resize(img,None,fx=0.6,fy=0.6,interpolation=cv.INTER_CUBIC)
imshow("res",res)
imshow("res2",res2)

cv.waitKey(0)
cv.destroyAllWindows()