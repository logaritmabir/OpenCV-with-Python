import cv2 as cv
from cv2 import imshow
import numpy as np

img = cv.imread("kawga.jpg")
img_monkey = cv.imread("")

res = cv.resize(img,None,fx=0.6,fy=0.6,interpolation=cv.INTER_LINEAR_EXACT) #resmi büyütme veya küçültme
res2 = cv.resize(img,None,fx=0.6,fy=0.6,interpolation=cv.INTER_CUBIC)

rows,cols,_ = img.shape

M = np.float32([[1,0,100],[0,1,10]]) # Rotasyon matrisi, 100 x(columns) kaydırma,10 y(rows) kaydırma
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('img',dst)
imshow("res",res)
imshow("res2",res2)

cv.waitKey(0)
cv.destroyAllWindows()