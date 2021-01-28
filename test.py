import cv2
#簡寫numpy為np
import numpy as np
#照片存在同一個專案資料夾中
#讀圖片檔案，'test.jpg'檔名，IMREAD_COLOR 讀彩色檔
img = cv2.imread('test.jpg',cv2.IMREAD_COLOR)



#顯示圖片img，以'test'做為標題
cv2.imshow('test',img)
#要輸入下面兩行才會有照片視窗
cv2.waitKey(0)
cv2.destroyAllWindows