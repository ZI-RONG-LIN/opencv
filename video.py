#讀取視訊
#簡寫numpy為np
import numpy as np

#下面這段的架構可以輸入orvid，snippets就會自動生成
#Import only if not previously imported
import cv2
# In VideoCapture object either Pass address of your Video file
# Or If the input is the camera, pass 0 instead of the video file

cap = cv2.VideoCapture(0)
# 視訊鏡頭有打開就會跳出視訊畫面
if cap.isOpened() == False:
    print("Error in opening video stream or file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # Display the resulting frame
        cv2.imshow('Frame',frame)
        # Press esc to exit
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()