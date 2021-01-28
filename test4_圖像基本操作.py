#圖像基本操作


#獲取像素值並修改---------------------
import cv2
#簡寫numpy為np
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('test.jpg',cv2.IMREAD_COLOR)
#抓出指定位置的顏色
px=img[100,100]
print(px)
#更改指定位置的顏色
g=img[101,100]=[255,255,255]
print(g)

# cv2.imwrite('t1.png',img)
# cv2.namedWindow('test',cv2.WINDOW_NORMAL)

# cv2.imshow('test',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#獲取圖像屬性----------------------------

img[102,100]=[255,255,255]
#a.shape獲取圖像形狀，行數、列數、、通道數的元組
print(img.shape,img.size)


#圖像的ROI-----------------
# 把特定區塊挖出來，填到另一個相同大小的空白區塊內
# [y1:y2,x1:x2] (前面放直的，後面放橫的)
#要挖出來的圖塊
roi=img[146:191,460:607]
#要被填入的區塊
img[77:122,641:788]=roi



#imwrite 是opencv的存圖方式，所以是BGR存
cv2.imwrite('ROI_practice.jpg',img)
#但這邊要用matplotlib顯示，所以要再把BGR轉成RGB之後，才會輸出對的圖
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img1)
#顯示xy座標值
plt.xticks([]),plt.yticks([])
plt.show()
