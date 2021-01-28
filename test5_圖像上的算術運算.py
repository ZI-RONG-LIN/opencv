#圖像上的算術運算
#圖像混合(兩張圖大小要一樣!)
#疊圖的效果

import cv2
import numpy as np
img = cv2.imread('test.jpg',cv2.IMREAD_COLOR)
#要挖出來的圖塊
roi_1=img[146:591,460:807]
#要被填入的區塊
roi_2=img[77:522,641:988]
#調整兩張圖的權重，類似調透明度
dst=cv2.addWeighted(roi_1,0.3,roi_2,0.7,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindow()

