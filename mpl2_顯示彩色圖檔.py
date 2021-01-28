# 用matplotlib顯示彩色圖檔，如果不修改會是以BGR顯示出來的圖，照片會錯


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()


#-------------------------------------------
#另一種寫法

import cv2
#簡寫numpy為np
import numpy as np
#匯入matplotlib套件，裏頭有各種繪圖方法
from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt
img = cv2.imread('test.jpg',1)
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img1)
#顯示xy座標值的顏色
plt.xticks([]),plt.yticks([])
plt.show()