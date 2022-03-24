import cv2 as cv
from cv2 import imread
import numpy as np

img = cv.imread("kawga.jpg")
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

_,img_thresh=cv.threshold(img_gray,70,255,cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(img_thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) # burayı anlamadım,contours noktalarımızı içeren ve nesnenin sınırlarını belirleyen bir liste

cv.drawContours(img, contours, -1, (0,255,0), 3)


cv.imshow('img',img)
cv.imshow('img_thresh',img_thresh)
cv.imshow('img_gray',img_gray)


cv.waitKey(0)
cv.destroyAllWindows()