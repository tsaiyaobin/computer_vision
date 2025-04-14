import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("img3.jpg",0)
img=cv2.resize(img,(300,300))

# cv2.calcHist(images, channels, mask, histSize, ranges) 計算直方圖
# channels : gray[0] ; color image,B:[0] G:[1] R:[2]
# histSize : BIN count
# ranges : 像素值範圍, Normally, it is [0,256]

hist=cv2.calcHist( [img] , [0] , None , [256] , [0,256] )

plt.hist(img.ravel(),256)
plt.show()

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
