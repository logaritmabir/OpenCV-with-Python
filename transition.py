from cv2 import imread, imshow
import numpy as np
import cv2 as cv

k = 0.1

sheep = imread("Kuzu.jpg")
graysheep = imread("Grikuzu.jpg")
blacksheep = np.zeros(sheep.shape,np.uint8)
monkey = imread("maymun.jpeg")
backg = imread("backscreen.jpg")
rows,cols,channels = sheep.shape
roibackg = backg[0:rows,0:cols]
# imshow("roiMonkey",roiMonkey)
# imshow("monkey",monkey)

cv.namedWindow("RESULT")

for i in range(10):
    res = cv.addWeighted(sheep,k,roibackg,1-k,0)
    cv.imshow("RESULT",res)
    k+=0.1
    cv.waitKey(150)


cv.waitKey(0)
cv.destroyAllWindows()