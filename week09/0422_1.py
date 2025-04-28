import cv2
import numpy as np

img1=cv2.imread('img.jpg',0)
shape=img1.shape

# 加胡椒鹽雜訊
img=cv2.resize(img1, (int(shape[1]*0.5),int(shape[0]*0.5)))
b = np.random.randint(0, 9, (int(shape[0]*0.5), int(shape[1]*0.5))) 

for i in range(int(shape[0]*0.5)-1):
    for j in range(int(shape[1]*0.5)-1):
        if b[i][j]==1:
            img[i][j]=0
        elif b[i][j]==2:
            img[i][j]=255

# 均值濾波
blur=cv2.blur(img,(5,5),0)
# 高斯濾波
gau=cv2.GaussianBlur(img,(5,5),0)
# 中值
med=cv2.medianBlur(img,5,0)

cv2.imshow('img1',img1)
cv2.imshow('img',img)
cv2.imshow('blur',blur)
cv2.imshow('gau blur',gau)
cv2.imshow('med blur',med)

cv2.waitKey()
cv2.destroyAllWindows()