import cv2
import numpy as np
# RGB 轉 HSV : cv2.COLOR_BGR2HSV
# RGB 轉 YCrCb : cv2.COLOR_BGR2YCR_CB

img=cv2.imread('img.jpg')
img = cv2.resize(img,(300,300))

img1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # hsv

img2=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB) # ycbcr

h,s,v=cv2.split(img1)

cv2.imshow('h',h)
cv2.imshow('s',s)
cv2.imshow('v',v)
cv2.imshow('image',img1)


if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()
    
# 加入滑桿
def nothing(x):
    pass

# 讀取圖片
img1 = cv2.imread('img.jpg')
if img1 is None:
    print("無法讀取圖片，請檢查檔案路徑")
    exit()

# 調整圖片大小（可選）
img1 = cv2.resize(img1, (300, 300))

# 建立名為 "image" 的視窗
cv2.namedWindow('image')

# 建立三個 HSV 軌跡條
cv2.createTrackbar('H', 'image', 0, 179, nothing)
cv2.createTrackbar('S', 'image', 0, 255, nothing)
cv2.createTrackbar('V', 'image', 0, 255, nothing)

while True:
    # 取得各軌跡條的數值
    h = cv2.getTrackbarPos('H', 'image')
    s = cv2.getTrackbarPos('S', 'image')
    v = cv2.getTrackbarPos('V', 'image')
    
    img1[:] = [h, s, v]
    
    cv2.imshow('image', img1)
    
    # 按下 'k' 鍵離開
    if cv2.waitKey(1) & 0xFF == ord("k"):
        break

cv2.destroyAllWindows()
