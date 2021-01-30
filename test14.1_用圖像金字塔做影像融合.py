#用圖像金字塔做影像融合

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 圖像尺寸最好是2的整次冪，如256,512等
# 否則在金字塔向上的過程中圖像的尺寸會不等
# 這會導致在拉普拉斯金字塔處理時由於不同尺寸矩陣相減而出错
A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')

# 將蘋果進行高斯金字塔處理，總共六级處理 降階6次
#複製A到G參數
G = A.copy()
gpA = [G]
#降階6次
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# 將橘子進行高斯金字塔處理，總共六级處理 降階6次
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

#將蘋果進行拉普拉斯金字塔處理，總共5級處理，升階5次
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1], GE)
    lpA.append(L)

# 將橘子進行拉普拉斯金字塔處理，總共5級處理，升階5次
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1], GE)
    lpB.append(L)
# 將兩個圖像的矩陣的左半部分和右半部分拼接到一起
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols//2], lb[:, cols//2:]))
    LS.append(ls)

# 採用金字塔拼接方法的图像 降階後再合成
#依光影做區分兩部分，而不是直接切一半拼接
ls_ = LS[0]  # 這里LS[0]为高斯金字塔的最小圖片
for i in range(1, 6):  # 第一次循环的圖像为高斯金字塔的最小圖片，依次通過拉普拉斯金字塔恢復到大圖像
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# 直接拼接 兩張照片各取一半
real = np.hstack((A[:, :cols//2], B[:, cols//2:]))

plt.subplot(221), plt.imshow(cv2.cvtColor(A, cv2.COLOR_BGR2RGB)), plt.title('Apple')
plt.subplot(222), plt.imshow(cv2.cvtColor(B, cv2.COLOR_BGR2RGB)), plt.title('Orange')
#兩張照片各取一半
plt.subplot(223), plt.imshow(cv2.cvtColor(real, cv2.COLOR_BGR2RGB)), plt.title('Direct')
#降階後再合成
plt.subplot(224), plt.imshow(cv2.cvtColor(ls_, cv2.COLOR_BGR2RGB)), plt.title('Pyramid')
plt.show()
