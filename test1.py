#--------------------------
#繪圖函數

import cv2
#簡寫numpy為np
import numpy as np

img=np.zeros((512,512,3), np.uint8)

#oline畫線功能
#Import only if not previously imported
import cv2
# Coordinates must be a tuple - (x,y)
# cv2.line(img,(起始位置),(結束位置),(B,G,R),線的粗細(粗細-1的話則是填滿))   
cv2.line(img,(0,0),(500,500),(0,0,255),5)                   #Color is by default black

#orec畫矩形
# cv2.rectangle(image,(topLeftCoor),(bottomRightCoor),(0,0,0),thickness) 
cv2.rectangle(img,(100,100),(200,200),(0,255,0),3)  


#ocircle畫圓
# Coordinates must be a tuple - (x,y)
# cv2.circle(image,(CenterCoordinates), radius, (0, 0, 0) ,thickness)   
cv2.circle(img,(210,200), 100, (255, 255, 0) ,5) 
#-------------------------
#opoly 畫橢圓
# cv2.polylines(image,[coordinates],Boolean(True if closed polygon),(0,0,0))                   #Color is by default black
#要先指定點的LIST
points = np.array([[200, 200], [300, 100], [400, 200], [400, 400], [200, 400]], np.int32)
#如果第三個布林值是false，則最後得到的圖形頭尾不會相連
cv2.polylines(img,[points],True,(0,0,100),3)    
#-----------------------------
#畫橢圓
cv2.ellipse(img,(256,256),(100,50),0,0,360,255,1)
#--------------------------
#otext 在圖片中添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, "輸入甚麼字(不能輸中文，要輸的話要改程式碼)", (座標),字形, 字的大小, (B, G, R),粗細)
cv2.putText(img, "text", (200,100),font, 2, (0, 0, 200),3)
#-----------------------------------
cv2.imshow('line',img)
#要輸入下面兩行才會有照片視窗
#意思為當按按鍵之後才會關掉視窗，否則照片就會顯示不出來，因為直接關掉了
#waitkey後面放要等待的時間，如果輸入0則無限等待
cv2.waitKey(0)
cv2.destroyAllWindows()