import cv2 as cv
import numpy as np

img = cv.imread('maymun.jpeg')
pyr = cv.pyrDown(img)
pyr2 = cv.pyrUp(img)

pyr_resize = cv.resize(pyr,(img.shape[1],img.shape[0]))
pyr2_resize = cv.resize(pyr,(img.shape[1],img.shape[0]))
print(pyr_resize.shape)

cv.imshow("original",img)
cv.imshow("pyr down",pyr)
cv.imshow("pyr up",pyr2)
cv.imshow("pyr_resize",pyr_resize)
cv.imshow("pyr2_resize",pyr2_resize)
cv.waitKey(0)
cv.destroyAllWindows()