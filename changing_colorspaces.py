import cv2 as cv
from cv2 import imshow
import numpy as np

camera = cv.VideoCapture(0)

while(1):
    _,frame = camera.read()

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_blue = np.array([90,50,70])
    upper_blue = np.array([128,255,255])
    lower_red = np.array([159,50,70])
    upper_red = np.array([180,255,255])

    mask_blue = cv.inRange(hsv, lower_blue, upper_blue) # araliktaysa 255 değilse 0 tresholding,mask belirttiğimiz aralıktaki mavi değerlerin beyaza çevrilmiş halidir gerisi siyah
    mask_red = cv.inRange(hsv, lower_red, upper_red)
    mask_inv_blue  = cv.bitwise_not(mask_blue)
    mask_inv_red = cv.bitwise_not(mask_red)

    mask_combine = cv.bitwise_or(mask_blue,mask_red)
    mask_inv_combine = cv.bitwise_not(mask_combine)

    res = cv.bitwise_and(frame,frame, mask= mask_inv_combine) # mask değişkeni işlem yapılacak alanı belirliyor

    cv.imshow('frame',frame)
    cv.imshow('res',res)
    cv.imshow('mask_red',mask_red)
    cv.imshow('mask_blue',mask_blue)
    cv.imshow('mask_combine',mask_combine)
    # cv.imshow('mask_inv_blue',mask_inv_blue)
    # cv.imshow('mask_inv_red',mask_inv_red)
    print(res)
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()