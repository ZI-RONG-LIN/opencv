#canny 邊緣檢測

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test27.jpg', 0)
#有幾個參數比較(設定閾值)
#需要一直調整才知道哪個呈現是自己想要的
#可以做trackbar調整閾值
#閾值越小，點會越細，噪點也會高
edges = cv2.Canny(img, 50, 100)
edges2 = cv2.Canny(img, 50, 150)
edges3 = cv2.Canny(img, 50, 200)
edges4 = cv2.Canny(img, 100, 150)
#閾值越大，邊緣有時會較不連貫，注意細節有沒有被濾掉，噪點較低
edges5 = cv2.Canny(img, 200, 250)

plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(232), plt.imshow(edges, cmap='gray'), plt.title('Edge Image 50.100')
plt.subplot(233), plt.imshow(edges2, cmap='gray'), plt.title('Edge Image 100.150')
plt.subplot(234), plt.imshow(edges3, cmap='gray'), plt.title('Edge Image 150.200')
plt.subplot(235), plt.imshow(edges4, cmap='gray'), plt.title('Edge Image 200.250')
plt.subplot(236), plt.imshow(edges5, cmap='gray'), plt.title('Edge Image 250.300')

plt.show()