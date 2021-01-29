
import cv2
import numpy as np
# The function attached to the trackbar.
def nothing(x):
    pass
img = cv2.imread('test27.jpg', 0)
cv2.imshow('image1',img)
edges = cv2.Canny(img, 50, 100)
cv2.namedWindow('image')
cv2.createTrackbar('minval','image',0,255,nothing)
cv2.createTrackbar('maxval','image',0,255,nothing)

while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    minval=cv2.getTrackbarPos('minval','image')
    maxval=cv2.getTrackbarPos('maxval','image')
    edges = cv2.Canny(img,minval, maxval)
    #如果switch沒打開，則下方顯示黑色，否則顯示讀取到的RGB色]
cv2.destroyAllWindows()