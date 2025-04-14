import cv2
import numpy as np

img = cv2.imread("img.jpg")
img = cv2.resize(img, (473, 572))
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

# ycrcb 膚色區間
lower = np.array([0, 153, 77])
higher = np.array([255, 173, 127])
mask = cv2.inRange(ycrcb, lower, higher)

res = cv2.bitwise_and(img, img, mask=mask)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    contour = max(contours, key=cv2.contourArea)  # 找最大輪廓
    box = cv2.minAreaRect(contour)
    points = cv2.boxPoints(box)
    points = points.astype(int)

    # 畫在原圖副本上
    dst = cv2.drawContours(img.copy(), [points], 0, (0, 255, 0), 1)

    cv2.imshow('dst', dst)

cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
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
    
    lower = np.array([0, 50, 70])
    higher = np.array([20, 255, 255])
    
    mask=cv2.inRange(hsv,lower,higher)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    _,binary=cv2.threshold(res, 110, 255, cv2.THRESH_BINARY)
    contours, hierarchy=cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    box=cv2.minAreaRect(contours[0])
    points=cv2.boxPoints(box)
    points=points.astype(int)
    dst=cv2.drawContours(frame, [points], 0, (0,255,0),2)
    cv2.imshow('res', dst)
    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

'''
''' 
第 26 行程式碼在做的事
     frame                mask                         res
[[50 90 40 100],      [[0 1 1 0],                [[0  90 40  0],
 [48 95 67 56],        [1 1 1 0],                 [48 95 67  0],
 [30 80 97 101],  *    [0 0 0 0],       =         [0  0  0  0],
 [76 68 55 200]]       [0 0 0 0]]                 [0  0  0  0]] 

'''


