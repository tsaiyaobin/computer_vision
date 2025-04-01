import cv2
import numpy as np
import matplotlib.pyplot as plt
# bin 是 x 的每一數值稱為 bin
# np.histogram() 計算直方圖
# cv2.calcHist(images, channels, mask, histSize, ranges) 計算直方圖
# channels: gray[0] ; color image,B:[0] G:[1] R:[2]
# 直方圖可以用來做影像匹配
img=cv2.imread("img3.jpg",0)
img=cv2.resize(img,(300,300))
hist=cv2.calcHist([img],[0],None,[256],[0,256])


plt.hist(img.ravel(),256)
plt.show()

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
