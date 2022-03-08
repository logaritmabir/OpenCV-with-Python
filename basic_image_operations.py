from email.mime import image
import cv2 as cv
from cv2 import imread
import numpy as np
from matplotlib import pyplot as plt

img = imread("Kuzu.jpg")

# head = img[30:140,60:210]
# img[10:120,200:350] = head
replicate = cv.copyMakeBorder(img,200,200,200,200,cv.BORDER_REPLICATE) #ekmeğe çokokrem sürer gibi
reflect = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REFLECT) # yansıma
reflect101 = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REFLECT_101) # bi fark göremiyorum lanet olsun
wrap = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_WRAP) # 6 lı vesikalık fotoğraf
constant = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_CONSTANT) #dış sınır ekle (margin)


# cv.imshow("orginal",img)
# cv.imshow("replicate",replicate)
# cv.imshow("reflect",reflect)
# cv.imshow("reflect101",reflect101)
# cv.imshow("wrap",wrap)
# cv.imshow("constant",constant)


plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray',alpha=0.4),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,alpha=0.6),plt.title('CONSTANT')
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()

