import cv2
from cv2 import BORDER_REFLECT
from cv2 import BORDER_REFLECT101
from cv2 import BORDER_TRANSPARENT
from cv2 import BORDER_WRAP
import numpy

image = cv2.imread("Kuzu.jpg")
print("toplam piksel sayısı : " + str(image.size))
print("dtype : " + str(image.dtype))
print("Resmin ölçüleri : " + str(image.shape)) #genişlik yükseklik kanal sayısı

#image[1,1] = [0,0,0]

#for i in range(100):
#    for k in range(50):
#        image[k,i] = [0,0,0] #[y,x]

#image[:,:,2] = 20 # 0 mavi 1 yeşil 2 kırmızı BGR,tüm alana uygula bu efekti
#image[0:69,0:120,0] =123

mirror = cv2.copyMakeBorder(src = image,bottom = 75,top = 175, right = 75, left = 75, borderType= cv2.BORDER_REFLECT)
stretch = cv2.copyMakeBorder(src = image,bottom = 75,top = 175, right = 75, left = 75, borderType= cv2.BORDER_REPLICATE)
mirror2 = cv2.copyMakeBorder(src = stretch,bottom = 75,top = 175, right = 75, left = 75, borderType= cv2.BORDER_REFLECT)
repeat = cv2.copyMakeBorder(src = image,bottom = image.shape[0],top = image.shape[0], right = image.shape[1], left = image.shape[1], borderType= cv2.BORDER_WRAP)
border = cv2.copyMakeBorder(src = image,bottom = 75,top = 175, right = 75, left = 75, borderType= cv2.BORDER_CONSTANT,value=[23,11,232])
# rectangle = cv2.rectangle(image,pt1=(320,20),pt2 = (520,250),color=[140,100,23],thickness=4) # (x,y)
# rectangle = cv2.rectangle(image,pt1=(320,20),pt2 = (500,200),color=[40,100,23],thickness=4)
# rectangle = cv2.rectangle(image,pt1=(20,120),pt2 = (60,20),color=[40,100,23],thickness=4) #20 birim sağa git 120 birim asağı in,60 sağa ve 20 aşağı
cv2.line(image,(30,60),(60,60),[200,100,30],4)

cv2.circle(image,(450,300),40,[30,154,255],40)
cv2.ellipse(image,(256,256),(100,50),0,0,180,255,30)
# cv2.imshow("mirror",mirror)
# cv2.imshow("mirror2",mirror2)
# cv2.imshow("repeat",repeat)
# cv2.imshow("border",border)
# cv2.imshow("replicate",stretch)
cv2.imshow("orginal",image)
#cv2.imshow("rectangle",rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()