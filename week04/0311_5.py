import numpy as np
import cv2

img1 = cv2.imread("img.jpg",1)
img2 = cv2.resize(img1,(900,900))
img3 = cv2.resize(img1,(900,900))

# 黑色畫布
img=np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(512,512),(0,255,0),4)

# 線
cv2.line(img3,(0,0),(900,900),(0,0,255),4)
cv2.line(img3,(900,0),(0,900),(0,0,255),4)

# 矩形
#cv2.rectangle(img3,(550,550),(900,750),(0,255,0),4)
# 圓形
cv2.circle(img3,(450,450),50,(0,255,0),-1)

# 寫字
# putText(圖片, "<寫字>", 座標, 字形, 字體大小, 線的顏色
#           , 線的大小, cv2.LINE_AA (抗拒齒) )
cv2.putText(img3,"have a nice day",(350,700),cv2.FONT_HERSHEY_COMPLEX,1,
            (0,255,255),1,cv2.LINE_AA)

#cv2.imshow('line',img)
cv2.imshow('rectangle',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
