import cv2
import numpy as np
# color object tracking
# 膚色檢測
#-----------------
#--顯示一般攝影機--
#-----------------
cap = cv2.VideoCapture(0)
# ret回傳布林值, 取得圖像偵
if not cap.isOpened():
    print("無法打開攝像頭 ")
    
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower = np.array([0, 70, 70])
    higher = np.array([20, 255, 255])

    
    mask=cv2.inRange(hsv,lower,higher)

    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

''' 
第 26 行程式碼在做的事
     frame                mask                         res
[[50 90 40 100],      [[0 1 1 0],                [[0  90 40  0],
 [48 95 67 56],        [1 1 1 0],                 [48 95 67  0],
 [30 80 97 101],  *    [0 0 0 0],       =         [0  0  0  0],
 [76 68 55 200]]       [0 0 0 0]]                 [0  0  0  0]] 

'''

cap = cv2.VideoCapture(0)
# ret回傳布林值, 取得圖像偵
if not cap.isOpened():
    print("無法打開攝像頭 ")
    
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    ycrcb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCR_CB)
    
    lower = np.array([ 0, 140, 77])
    higher = np.array([ 255, 173, 127])
    
    mask=cv2.inRange(ycrcb,lower,higher)

    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

