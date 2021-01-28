#檔案命名不能跟套件名相同
#用matplotlib顯示灰階圖檔

import cv2
#簡寫numpy為np
import numpy as np
#匯入matplotlib套件，裏頭有各種繪圖方法
from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt

img = cv2.imread('test.jpg',0)
#用灰階
plt.imshow(img, cmap ='gray', interpolation = 'bicubic')
#顯示xy座標值的顏色
plt.xticks([]),plt.yticks([])
plt.show()