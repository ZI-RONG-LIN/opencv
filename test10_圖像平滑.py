#圖像平滑，類似濾波，把離平均值或是指定值太遠的波濾掉
# 圖會變模糊，把噪點取消掉
#目的是要框東西，所以要把雜訊篩掉留下輪廓
# 像要去背前須要先辨識出人像輪廓的邊線

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 注意圖片尺寸必須是卷積核的整倍，以下面為例的話，卷積核為5*5，所以圖的大小要是5的倍數*5的倍數，否則會出錯
img = cv2.imread('test14.jpg') 
# #2D卷積濾波
#每一區都變模糊
kernel = np.ones((5, 5), np.float32)/25  # 創建一个5x5的平均濾波器核(卷積核)
dst = cv2.filter2D(img, -1, kernel)

# 平均模糊
blur = cv2.blur(img, (5, 5))

# 高斯滤波
#花紋有保持，邊界直線都清楚
#表現比其他的好，但不絕對
gauss = cv2.GaussianBlur(img, (5, 5), 0)

# 中值滤波
median = cv2.medianBlur(img, 5)

# 雙邊滤波
bila = cv2.bilateralFilter(img, 10, 200, 200)

plt.subplot(231), plt.imshow(img), plt.title('Original')
plt.subplot(232), plt.imshow(dst), plt.title('Filter2D')
plt.subplot(233), plt.imshow(blur), plt.title('Averaging')
plt.subplot(234), plt.imshow(gauss), plt.title('GuassianBlur')
plt.subplot(235), plt.imshow(median), plt.title('MedianBlur')
plt.subplot(236), plt.imshow(bila), plt.title('BilateralFilter')

plt.show()