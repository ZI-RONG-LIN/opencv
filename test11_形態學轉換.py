#形態學轉換
#根據圖像的形狀進行簡單的操作
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test17.png')
img1 = cv2.imread('test16.png')
# 卷積核
#類似畫筆的大小，越小的話，線條增減幅度會比較小
kernel = np.ones((5, 5), np.uint8)   
# 卷積核
kernel2 = np.ones((10, 10), np.uint8) 

# 腐蝕
#iterations代表腐蝕次數
# 圖像周圍可能有一些雜訊，透過腐蝕方式去除
erosion = cv2.erode(img1, kernel, iterations=1)  
# 膨脹
#iterations代表膨脹次數
#某些地方被腐蝕過頭或是有缺角，透過膨脹把圖塊補齊
dilation = cv2.dilate(img1, kernel, iterations=1)  
# 開運算
#先進行腐蝕再進行膨脹，用來除噪
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)  
# 閉運算
#先膨脹再腐蝕，常用來填充前景物體中的小洞，或前景物體上的小黑點
closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)  
# 形態學梯度
#圖像膨脹後與腐蝕後的圖像差異
#所以會只留下物體的輪廓
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)  
# 禮帽
#原始圖像與進行開運算之後的圖像差異
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel2)  
# 黑帽
# 閉運算與原始圖像之間的圖像差異
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel2)  

plt.subplot(241), plt.imshow(img), plt.title('Original')
plt.subplot(242), plt.imshow(erosion), plt.title('Erosion')
plt.subplot(243), plt.imshow(dilation), plt.title('Dilation')
plt.subplot(244), plt.imshow(opening), plt.title('Opening')
plt.subplot(245), plt.imshow(closing), plt.title('Closing')
plt.subplot(246), plt.imshow(gradient), plt.title('Gradient')
plt.subplot(247), plt.imshow(tophat), plt.title('Tophat')
plt.subplot(248), plt.imshow(blackhat), plt.title('Blackhat')

plt.show()