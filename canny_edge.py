#Canny kenar bulma algoritmasi için öncelikle görüntüdeki gürültüyü kaldır(Gaussian Blur)
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
cv.namedWindow('edges')

while(1):
    _,frame = cap.read()


    edges = cv.Canny(frame,140,200)
    cv.imshow('edges',edges)

    k = cv.waitKey(20) & 0xFF
    if k == ord('m'):
        break


cv.destroyAllWindows()