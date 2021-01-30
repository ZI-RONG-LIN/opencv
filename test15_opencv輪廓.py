#opencv 找輪廓

#找輪廓前要先進行閾值化或是canny輪廓檢測
#繪製輪廓
import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('test21_1.jpg')
img = src.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#設閾值
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# findContours 找輪廓
#用閾值找輪廓，放到contours這裡面
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]
# drawContours 畫輪廓
#用綠色畫，粗細10
#第三個參數counterIDx=-1的話則是顯示整個輪廓，0的話則會顯示第一個輪廓(第一個點)
draw = cv2.drawContours(img, cnt, -1, (0, 255, 0), 10)

plt.subplot(121), plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB)), plt.title('Src')
plt.subplot(122), plt.imshow(cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)), plt.title('image')
plt.show()