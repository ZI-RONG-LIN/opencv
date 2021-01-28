import cv2
#簡寫numpy為np
import numpy as np
#分別把RGB三個通道獨立出來看
img = cv2.imread('test.jpg',1)
r=cv2.imread('test.jpg',1)
b=cv2.imread('test.jpg',1)
g=cv2.imread('test.jpg',1)
b[:,:,1]=0
b[:,:,2]=0
g[:,:,2]=0
g[:,:,0]=0
r[:,:,1]=0
r[:,:,0]=0

#儲存圖檔，前面為儲存的檔名及格式，後面則是要儲存的圖檔來源
# cv2.imwrite('t1.png',img)


#讓顯示出來的圖可以調整視窗大小，否則就會照存的圖大小顯示，可能會太大或太小
# cv2.namedWindow('test',cv2.WINDOW_NORMAL)
#顯示圖片img，以'test'做為標題
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)

#要輸入下面兩行才會有照片視窗
#意思為當按按鍵之後才會關掉視窗，否則照片就會顯示不出來，因為直接關掉了
#waitkey後面放要等待的時間，如果輸入0則無限等待
cv2.waitKey(0)
cv2.destroyAllWindows()