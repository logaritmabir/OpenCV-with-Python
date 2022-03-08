import numpy 
import cv2 

mode = 1
drawing = False
ox,oy = -1,-1

def draw_mouse(event,x,y,flags,param):
    global ox,oy,mode,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ox,oy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == 1:
            cv2.rectangle(image,(ox,oy),(x,y),(0,255,0))
        elif mode == 2:
            cv2.rectangle(image,(ox,oy),(x,y),(0,255,255),-1)
    elif event == cv2.EVENT_MOUSEMOVE:
        print("Mouse move" + str(mode))


image = numpy.zeros((512,512,3), numpy.uint8)
cv2.namedWindow("mouse_brush")
cv2.setMouseCallback("mouse_brush",draw_mouse)

while(1):
    cv2.imshow("mouse_brush",image)
    temp = cv2.waitKey(20) & 0xFF
    if temp == ord('1'):
        mode = 1
    elif temp == ord('2'):
        mode = 2


cv2.destroyAllWindows()