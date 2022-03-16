import cv2 as cv
from cv2 import MORPH_GRADIENT
from cv2 import MORPH_TOPHAT
import numpy as np

img = cv.imread('morp_blackbg.png')
img2 = cv.imread('morp.png')
img3 = cv.imread('noisy.png')
kernel = np.ones((5,5),np.uint8)

erosion = cv.erode(img,kernel,iterations = 1)
erosion2 = cv.erode(img2,kernel,iterations = 1)

dilation = cv.dilate(img,kernel,iterations = 1) #beyaz sınırın genişletilmesi,başka bir değişle 1 katmanının genişlemesi,1 olmayan her şey 0 dır bu işlemlerde
dilation2 = cv.dilate(img2,kernel,iterations = 1)

opening = cv.morphologyEx(img,cv.MORPH_OPEN,kernel,iterations=1)#önce aşındır,aşınan görüntüyü genişlet.siyah fon içindeki küçük beyazları silmede kullanılabilir
closing = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)# önce genişlet,genişleyen görüntüyü aşındır.beyaz fon içindeki renkleri silmek için uygun olabilir
increase_opening = cv.dilate(opening,kernel,iterations=3)
gradient = cv.morphologyEx(img,MORPH_GRADIENT,kernel,iterations=1)
tophat = cv.morphologyEx(img,MORPH_TOPHAT,kernel,iterations=1)
# cv.imshow("opening",opening)
# cv.imshow("closing",closing)
# cv.imshow("original",img)
# cv.imshow("increase_opening",increase_opening)
# # cv.imshow("original2",img2)
# cv.imshow("erosion",erosion)
# cv.imshow("dilation",dilation)
# # cv.imshow("erosion2",erosion2)
# # cv.imshow("dilation2",dilation2)
cv.imshow('gradient',gradient)
cv.imshow('tophat',tophat)

cv.waitKey(0)
cv.destroyAllWindows()