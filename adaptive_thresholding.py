import cv2 as cv
from cv2 import THRESH_MASK
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('threshold.jpg',0) # fotoğrafı tek kanalda yüklüyorum
img_blur = cv.medianBlur(img,5) #blur katsayısı 1 den büyük olmalı ve tek sayı 
img_gaussian_blur = cv.GaussianBlur(img,(5,5),0)

_,normal_th = cv.threshold(img,127,255,cv.THRESH_BINARY)

meanC_th = cv.adaptiveThreshold(img_blur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
meanC_th2 = cv.adaptiveThreshold(img_blur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,4)
meanC_th3 = cv.adaptiveThreshold(img_blur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,21,2)
gaussianC_th = cv.adaptiveThreshold(img_blur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,21,2)
_,otsu_th1 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
_,otsu_th2 = cv.threshold(img_gaussian_blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)


plt.subplot(231),plt.imshow(meanC_th,'gray'),plt.title('meanC_th1')
plt.subplot(232),plt.imshow(meanC_th2,'gray'),plt.title('meanC_th2')
plt.subplot(233),plt.imshow(meanC_th3,'gray'),plt.title('meanC_th3')
plt.subplot(234),plt.imshow(gaussianC_th,'gray'),plt.title('gaussianC_th')
plt.subplot(235),plt.imshow(otsu_th1,'gray'),plt.title('otsu_th1')
plt.subplot(236),plt.imshow(otsu_th2,'gray'),plt.title('otsu_th2')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()