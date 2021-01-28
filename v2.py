#錄影片
#owvid會把架構自動生成，再改一些參數就可以
#會開啟視訊頭，並且錄影，關閉之後會把這期間錄的影像存在專案資料夾內

import numpy as np
#Import only if not previously imported
import cv2
# Create a Video Reader Object.
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("Error in opening video stream or file")
#Define the codec for the Video
# fourcc = cv2.VideoWriter_fourcc("Fourcc Codec Eg-XVID")
#*'XVID' 此為預設編碼
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#Create Video Writer Object
# "test.avi" 寫入影片名稱
writer = cv2.VideoWriter('test.avi',fourcc, 30, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        writer.write(frame)
        cv2.imshow("Frame",frame)
        # Exit on pressing esc
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()