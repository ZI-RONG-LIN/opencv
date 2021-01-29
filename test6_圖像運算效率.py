#圖像處理程序檢測及優化

#計算程式碼處處理的時間，類似tiktok功能---
import cv2
import numpy as np
#紀錄執行起始時間
e1 = cv2.getTickCount()
# 跑的程式碼放在這邊!!!
#紀錄執行結束的時間
e2 = cv2.getTickCount()
#計算經過的秒數，否則只會顯示時間點而已
time = (e2 - e1)/ cv2.getTickFrequency()


#優化----------
#硬體加速等機制


