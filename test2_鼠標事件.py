#用滑鼠互動(鼠標事件)

import cv2
import numpy as np
#mouse callback function，滑鼠操作特定條件後，執行後續動作
def draw_circle(event,x,y,flags,param):
    #左邊滑鼠點擊，該位置畫出一個圓
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
# 創建圖像與窗口並將窗口與回調函數綁定
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
#按ESC可以把視窗關掉
cv2.destroyAllWindows()