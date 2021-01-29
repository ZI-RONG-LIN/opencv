#***圖像處理
#轉換顏色
#像是前面有提到的把BGR轉RGB功能算是其中一種功能
#調整HSL(色相、飽和度、亮度)、HSV(色相、飽和度、明度)色彩空間

#顯示所有色彩處理的相關函數
# import cv2
# flag=[i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flag)


#物體捕捉
#從視訊影像中抓特定顏色的物件出來
#有光影打到的部分會有雜訊，又稱噪音，之後會教怎麼降噪
#要有鏡頭，抓藍色物件
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
# 獲取每一偵
    ret,frame=cap.read()
#如果直接抓RGB的話會偵測不到，如果要抓黃色，抓到紅色也會抓到黃色，最後出來的顏色就會不太對
# 轉換到HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
# 設定藍色的閾值，閾值越低的話，只要有一點偏藍就會抓到，閾值高的話則要完全符合該藍色範圍才會捕捉到
#可以上網找顏色的HSV範圍在哪
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
# 根據閾值構建掩模
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
# 對原圖像和掩模進行位運算
    res=cv2.bitwise_and(frame,frame,mask=mask)
# 顯示圖像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
# 關閉窗口
cv2.destroyAllWindows()