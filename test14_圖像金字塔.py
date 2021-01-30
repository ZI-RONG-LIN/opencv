#圖像金字塔
#有時候我們不知道目標物件在圖中的大小，所以需要先建立一個子圖集存放各種分辨率(大小、解析度...)的物件
#這樣只要電腦判斷目標圖中有出現子圖集中的物件時，則將其辨識出來
#分成高斯濾波金字塔與拉普拉絲濾波金字塔(影像會較模糊，但融合時看起來比較自然)
#可進行影像合成
#先濾波(降階)之後，再還原回來圖像的邊界會比較清楚一點，之後再做邊緣檢測會比較容易一點
# import cv2
# import numpy as np

# img = cv2.imread('test6.jpg')
# #把照片降一階
# lower = cv2.pyrDown(img)
# #把照片降兩階
# lower1 = cv2.pyrDown(lower)
# #把照片降兩階之後，再升一階
# higher = cv2.pyrUp(lower1)
# #把照片降兩階之後，再升兩階
# higher1 = cv2.pyrUp(higher)
# #顯示照片
# while(1):
#     cv2.imshow('src', img)
#     cv2.imshow('lower', lower)
#     cv2.imshow('lower1', lower1)
#     cv2.imshow('higher', higher)
#     cv2.imshow('higher1', higher1)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()


import cv2
import numpy as np
from matplotlib import pyplot as plt

# 圖像尺寸最好是2的整次冪，如256,512等
# 否則在金字塔向上的過程中圖像的尺寸會不等
# 這會導致在拉普拉斯金字塔處理時由於不同尺寸矩陣相減而出錯
img = cv2.imread('test6.jpg')
# pyrDown尺寸變小，分辨率降低
lower = cv2.pyrDown(img)
lower1 = cv2.pyrDown(lower)
higher = cv2.pyrUp(lower1)
higher1 = cv2.pyrUp(higher)
#原始影像跟降階再還原後的影響相減的差
#清楚的影像-模糊的影像，留下清楚的輪廓邊線
laplace = cv2.subtract(img, higher1)

plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Src')
plt.subplot(122), plt.imshow(cv2.cvtColor(laplace, cv2.COLOR_BGR2RGB)), plt.title('Laplace')
plt.show()
