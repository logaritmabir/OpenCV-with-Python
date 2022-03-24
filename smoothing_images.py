import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.resize(cv.imread("damaged-photo.jpg"),None,fx=1,fy=1,interpolation=cv.INTER_LINEAR_EXACT)
img_median_blur = cv.medianBlur(img,13)
img_gaussian_blur = cv.GaussianBlur(img,(9,9),0) #katarakt gibi bişi 
img_blur = cv.blur(img,(9,9))


# plt.subplot(231),plt.imshow(img,'gray'),plt.title("img")
# plt.subplot(232),plt.imshow(img_median_blur,'gray'),plt.title("img_median_blur")
cv.imshow("img",img)
cv.imshow("img_blur",img_blur)
cv.imshow("img_median_blur",img_median_blur)
cv.imshow("img_gaussian_blur",img_gaussian_blur)

#cv.bilateralFilter() is highly effective in noise removal while keeping edges sharp.
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()