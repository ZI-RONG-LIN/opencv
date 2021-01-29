#圖像閾值
#當顏色超過某值之後，直接顯示為指定顏色，否則顯示另一個顏色
#ex 如果圖中顏色為由淺到深漸層呈現，則將該圖中的顏色轉成圖塊呈現
#或是超過某值不顯示，不超過的話就呈現數值
#或是只顯示超過某值的圖像，其他不呈現

# #簡單閾值----------------------------
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('test11.jpg',0)
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


#自適應閾值 除噪
#去除掉光影影響
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test13.jpg', 0)
img = cv2.medianBlur(img, 5)  # 中值濾波
#直接設定閾值
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 11 為 Block size(用來計算閾值的區域大小)，用11*11的大小作判別，這個太小的話會增加處理時間，太大則是會降低影像處理的品質
# 2 為 C 值，用來決定閾值，閾值為平均值或是加權平均值-C
#電腦根據平均決定閾值
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#電腦根據高斯決定閾值
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
titles = ['Original Image',
          'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


#Otsu's二值化

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test14.jpg', 0)
# global thresholding
#小於127顯示白色，否則顯示黑色，但會有很多雜訊
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Otsu's thresholding
#只用Otsu's
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
#用Otsu's+高斯模糊化，把比較相鄰近的濾掉
# （9,9）为高斯核的大小，8 为標準差，高斯核的大小、標準差降低一點的話，會保留比較多細節。但如果保留太多細節也會增加雜訊!!!
#能夠對圖像進行平滑運算，較好的保留影像的細節
blur = cv2.GaussianBlur(img, (9, 9), 8)
# 阈值一定要設為 0！
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# plot all the images and their histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)', 'Original Noisy Image',
          'Histogram', "Otsu's Thresholding", 'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
# 這里使用了 pyplot 中畫直方圖的方法，plt.hist, 要注意的是它的参數是一维數组
# 所以這里使用了（numpy）ravel 方法，將多维數组轉化成一维，也可以使用 flatten 方法
# ndarray.flat 1-D iterator over an array.
# ndarray.flatten 1-D array copy of the elements of an array in row-major order
for i in range(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()