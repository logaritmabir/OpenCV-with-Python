from cv2 import imread, imshow
import numpy as np
import cv2 as cv

# img1 = np.zeros((312,500,3),np.uint8)
# img2 = np.zeros((312,500,3),np.uint8)
img3 = imread("Kuzu.jpg")
# img4 = np.zeros((img3.shape),np.uint8)
# img5 = np.zeros((1080,1920,3),np.uint8)
img5 = imread("backscreen.jpg")
rows,cols,channels = img3.shape
roi = img5[0:rows,0:cols]

img3grey = cv.cvtColor(img3,cv.COLOR_BGR2GRAY)
ret,mask = cv.threshold(img3grey, 30,255, cv.THRESH_BINARY)
imshow("mask",mask)

mask_inv = cv.bitwise_not(mask)
imshow("mask_inv",mask_inv)

img5_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

imshow("img5_bg",img5_bg)

img3_fg = cv.bitwise_and(img3,img3,mask = mask)
imshow("img3_fg",img3_fg)
dst = cv.add(img5_bg,img3_fg)
imshow("dst",dst)
img5[0:rows, 0:cols ] = dst
cv.imshow('result',img5)
# imshow("img5",img5)
# imshow("maymun",img3)

# img2[:,:,2] = 255
# img1[:,:,1] = 200

# dst = cv.addWeighted(img1,0.4,img2,0.6,0)
# dst2 = cv.addWeighted(img3,0.7,img4,0.3,0)

# cv.imshow("dst",dst)
# cv.imshow("dst2",dst2)
cv.waitKey(0)
cv.destroyAllWindows()

#14.satırda kanal sayısı THRESH_BINARY kullanabilmek için 1'e düşürülmüştür
#21. ve 25. satırlarda kullanılan bitwise_and fonksiyonunun "mask" parametresi and işleminden sonra maskedeki siyah pixelleri görüntüye oturtur
#27. satırda pixeller toplanarak pikseller toplandı