import cv2
#簡寫numpy為np
import numpy as np
#照片存在同一個專案資料夾中
#讀圖片檔案，'test.jpg'檔名，也可以貼照片的完整路徑，但路徑中的\要改成\\
#IMREAD_COLOR 以彩色讀入圖檔，可將cv2.IMREAD_COLOR，用1表示
#IMREAD_GRAYSCALE 以灰階讀入圖檔，可將cv2.IMREAD_GRAYSCALE，用0表示
#圖檔是用2維陣列儲存，同時紀錄該座標的顏色(RGB的方式)，以BGR的順序紀錄
img = cv2.imread('test.jpg',cv2.IMREAD_COLOR)
#儲存圖檔，前面為儲存的檔名及格式，後面則是要儲存的圖檔來源
cv2.imwrite('t1.png',img)
#讓顯示出來的圖可以調整視窗大小，否則就會照存的圖大小顯示，可能會太大或太小
cv2.namedWindow('test',cv2.WINDOW_NORMAL)
#顯示圖片img，以'test'做為標題
cv2.imshow('test',img)
#要輸入下面兩行才會有照片視窗
#意思為當按按鍵之後才會關掉視窗，否則照片就會顯示不出來，因為直接關掉了
#waitkey後面放要等待的時間，如果輸入0則無限等待
cv2.waitKey(0)
cv2.destroyAllWindows()