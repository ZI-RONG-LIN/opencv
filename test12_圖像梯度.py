#圖像梯度
#找出圖像的邊界
#opencv提供三種梯度濾波器:sobel、scharr、laplacian

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test18.jpg', 0)
#使用laplacian濾波器
#深度調-1的話，就代表與原圖像的深度保持一致
#有點像中空的感覺，希望得到一個封閉區間
#劃出輪廓
laplacian = cv2.Laplacian(img, -1)
#使用soble濾波器
#深度調-1的話，就代表與原圖像的深度保持一致
#sobel有xy兩個方向，所以合在一起會把xy兩個部分一起濾掉
sobel = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize=5)
#顯示sobel x方向，濾掉y
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
sobelx1 = cv2.Sobel(img, -1, 1, 0, ksize=-1)  # ksize=-1同样可以实现scharr
#顯示sobel y方向，濾掉x
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)
#使用scharr濾波器
#對sobel的優化，再積卷核小的情況下抗噪能力很好
scharr = cv2.Scharr(img, cv2.CV_8U, 0, 1)
scharrx = cv2.Scharr(img, cv2.CV_8U, 1, 0)
scharry = cv2.Scharr(img, cv2.CV_8U, 0, 1)

#生成一個有2*4的子圖大圖，子圖1~8分別如指令表示
plt.subplot(241), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(242), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian')
plt.subplot(243), plt.imshow(sobel, cmap='gray'), plt.title('Sobel')
plt.subplot(244), plt.imshow(sobelx, cmap='gray'), plt.title('Sobel X')
plt.subplot(245), plt.imshow(sobelx1, cmap='gray'), plt.title('Scharr X')
plt.subplot(246), plt.imshow(scharrx, cmap='gray'), plt.title('Scharr X')
plt.subplot(247), plt.imshow(sobely, cmap='gray'), plt.title('Sobel Y')
plt.subplot(248), plt.imshow(scharry, cmap='gray'), plt.title('Scharr Y')

plt.show()