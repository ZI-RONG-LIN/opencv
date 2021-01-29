#圖像梯度調深度
#從黑到白的導數是整數
#從白到黑的導數則是負整數
#如果原圖的深度是np.int8的話，所有負值的部分都會被截斷變成0
#因此如果兩種邊界都想偵側到，就須要先把導數轉成絕對值之後再輸出

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('test8.jpg', 0)
img2 = cv2.imread('test9.jpg', 0)

sobelx8u1 = cv2.Sobel(img1, cv2.CV_8U, 1, 0, ksize=5)
sobelx64f1 = cv2.Sobel(img1, cv2.CV_64F, 1, 0, ksize=5)
# 把導數轉成絕對值之後再輸出
abs_sobel64f1 = np.absolute(sobelx64f1)
sobel_8u1 = np.uint8(abs_sobel64f1)

sobelx8u2 = cv2.Sobel(img2, cv2.CV_8U, 1, 0, ksize=5)
sobelx64f2 = cv2.Sobel(img2, cv2.CV_64F, 1, 0, ksize=5)
# 把導數轉成絕對值之後再輸出
abs_sobel64f2 = np.absolute(sobelx64f2)
sobel_8u2 = np.uint8(abs_sobel64f2)

plt.subplot(231), plt.imshow(img1, cmap='gray'), plt.title('Original')
plt.subplot(232), plt.imshow(sobelx8u1, cmap='gray'), plt.title('Sobel CV_8U')
plt.subplot(233), plt.imshow(sobel_8u1, cmap='gray'), plt.title('Sobel abs(CV_64F)')
plt.subplot(234), plt.imshow(img2, cmap='gray'), plt.title('Original')
plt.subplot(235), plt.imshow(sobelx8u2, cmap='gray'), plt.title('Sobel CV_8U')
plt.subplot(236), plt.imshow(sobel_8u2, cmap='gray'), plt.title('Sobel abs(CV_64F)')

plt.show()