#圖像幾何變化
#ex 縮放、移動、旋轉、鏡像翻轉等等

#縮放尺寸
import cv2
import numpy as np
#如果照片在其他專案資料夾，則輸入路徑'../image/test.jpg'，前面..代表返回到image之前的檔案路徑，之後再走到image裡面取那張圖出來
img=cv2.imread('test.jpg')

#縮放方法一

# 下面的None本應該是輸出圖像的尺寸，但是因為後面我們設置了縮放因子
# 因此這裡為 None
#interpolation 如果圖像放大，中間多出來的範圍用差值補色，讓顏色比較平滑一點
#如果圖像縮小，則是挑幾個點位像素值作為代表，需決定哪幾個為圖的代表點
#如果輸出的圖有鋸齒狀，表示像素值有缺
#fx=2,fy=2 X軸跟Y軸各放大兩倍
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

#縮放方法二
#OR
# 這裡直接設置輸出圖像的尺寸，所以不用設置縮放因子
height,width=img.shape[:2]
res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
while(1):
    cv2.imshow('res',res)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()

#平移圖像----------------------
import cv2
import numpy as np

img = cv2.imread('test.jpg', 0)  # 以單通道灰階圖像讀入
rows, cols = img.shape
# 平移矩陣M：[[1,0,x],[0,1,y]]
M = np.float32([[1, 0, 200], [0, 1, 100]])
dst = cv2.warpAffine(img, M, (cols, rows))

while(1):
    cv2.imshow('dst', dst)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()

#旋轉圖像-------------------------

import cv2
import numpy as np
img=cv2.imread('messi5.jpg',0)
rows,cols=img.shape
# 第一個參數為旋轉中心，第二個參數為旋轉角度，第三個為旋轉後的縮放因子
# 可以通過設置旋轉中心，縮放因子，以及窗口大小來防止旋轉後超出邊界的問題
M=cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)
# 第三個參數是輸出圖像的尺寸中心
dst=cv2.warpAffine(img,M,(2*cols,2*rows))
while(1):
    cv2.imshow('img',dst)
    if cv2.waitKey(1)&0xFF==27:
        break
cv2.destroyAllWindows()

#仿射變換
#希望俯視圖上的點，轉換到其他向量時相對位置依舊不變
#轉換圖的向量
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('drawing.png')
rows,cols,ch=img.shape
#指定A圖中三個點的相對位置
pts1=np.float32([[50,50],[200,50],[50,200]])
#指定A圖中三個點要放在B圖中的哪三個位置
pts2=np.float32([[10,100],[200,50],[100,250]])
#getAffineTransform會自動計算要移轉的程度，其他點就照這個去轉
M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(cols,rows))
#把圖放在同一個視窗，指定位置及標題
plt.subplot(121,plt.imshow(img),plt.title('Input'))
plt.subplot(121,plt.imshow(img),plt.title('Output'))
plt.show()


#透視變換
# 視角轉變，當視角不是俯視而是有包含角度時，校正角度及遠小近大的影響
# ex從斜上拍一個方塊的照片，正確取出該方塊的位置並轉換成俯視圖


import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('sudokusmall.png')
rows,cols,ch=img.shape
#設置標記點pts1和目標點pts2，各取四個點
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
#生成透視矩陣，需放入float32型態的資料
M=cv2.getPerspectiveTransform(pts1,pts2)
#轉換成幾成幾的圖，前面為x軸長度，後面為y軸長度
dst=cv2.warpPerspective(img,M,(300,300))
#製作子圖
plt.subplot(121,plt.imshow(img),plt.title('Input'))
plt.subplot(121,plt.imshow(img),plt.title('Output'))
plt.show()

#可以參考老師的test9，就可以直接透過點擊圖中要取的4個點(順時針依序取)，直接取得該點的座標值
#就不用先取得點的xy位置
