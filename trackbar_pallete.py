from ast import Pass
import cv2
import numpy

def NEXT(x):
    pass

img = numpy.zeros((300,512,3),numpy.uint8)
cv2.namedWindow("tracebar")
cv2.createTrackbar("Red","tracebar",0,255,NEXT)
cv2.createTrackbar("Green","tracebar",0,255,NEXT)
cv2.createTrackbar("Blue","tracebar",0,255,NEXT)

while(1):
    cv2.imshow("tracebar",img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27: #ESC
        break
    r = cv2.getTrackbarPos("Red","tracebar")
    g = cv2.getTrackbarPos("Green","tracebar")
    b = cv2.getTrackbarPos("Blue","tracebar")

    img[:] = [b,g,r]
cv2.destroyAllWindows()