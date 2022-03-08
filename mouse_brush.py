import cv2
from cv2 import imread
from cv2 import EVENT_RBUTTONDBLCLK
import numpy

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(image,(x,y),100,(0,0,255),-1)
        print("RightButtonDoubleClick")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),100,(255,255,255),-1)
        print("LeftButtonDoubleClick")

image = numpy.zeros((512,512,3), numpy.uint8)
cv2.namedWindow("mouse_brush")
cv2.setMouseCallback("mouse_brush",draw_circle)

while(1):
    cv2.imshow('mouse_brush',image)
    if (cv2.waitKey(20) & 0xFF) == 27:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()