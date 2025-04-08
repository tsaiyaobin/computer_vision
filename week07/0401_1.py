import cv2
import numpy as np
import matplotlib.pyplot as plt
# 直方圖缺位置資訊
# bin 是 x 的每一數值稱為 bin
# np.histogram() 計算直方圖
# cv2.calcHist(images, channels, mask, histSize, ranges) 計算直方圖
# channels: gray[0] ; color image,B:[0] G:[1] R:[2]
# 直方圖可以用來做影像匹配

img=cv2.imread("img.jpg",0)
img=cv2.resize(img,(300,300))
hist1=cv2.calcHist([img],[0],None,[256],[0,256]) # 計算直方圖

img2=cv2.imread("img2.jpg",0)
img2=cv2.resize(img2,(300,300))
hist2=cv2.calcHist([img2],[0],None,[256],[0,256])

img3=cv2.imread("img3.jpg",0)
img3=cv2.resize(img3,(300,300))
hist3=cv2.calcHist([img3],[0],None,[256],[0,256])

plt.hist(img.ravel(),256)
plt.show()
plt.hist(img2.ravel(),256)
plt.show()
plt.hist(img3.ravel(),256)
plt.show()

# 比較直方圖
# 兩張圖要做比對，bin 數要相同
# itersection:交集越小越不像(每個bin都去算交集)，越大越好
# correl(相關係數):越大越好
# chisqr(卡方):越小越好
# bhattacharyya(巴氏距離):越小越好
chi_sqr12=cv2.compareHist(hist1,hist2,cv2.HISTCMP_CHISQR)
bhatta12=cv2.compareHist(hist1,hist2,cv2.HISTCMP_BHATTACHARYYA)

chi_sqr13=cv2.compareHist(hist1,hist3,cv2.HISTCMP_CHISQR)
bhatta13=cv2.compareHist(hist1,hist3,cv2.HISTCMP_BHATTACHARYYA)


print(f'第一跟第二張:chi_sqr:{chi_sqr12},bhatta:{bhatta12}')
print(f'第一跟第三張:chi_sqr:{chi_sqr13},bhatta:{bhatta13}')




