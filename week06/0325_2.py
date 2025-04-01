import cv2
import numpy as np

img = cv2.imread("img.jpg")
img = cv2.resize(img,(300,300))

# 仿射變換要求 : 直線轉換後還是直線，原本平行的轉換後還是要平行
# cv2.warpAffine(src,M,dsize) ---> dsize=size of output image (width,height)
# M:scaling, translation, rotation

#平移
tx,ty=50,100
M=np.array([[1,0,tx],[0,1,ty]],dtype="float64")
img2=cv2.warpAffine(img,M,(300,300))

#旋轉90度
M=np.array([[0,1,0],[1,0,0]],dtype="float64")
img3=cv2.warpAffine(img,M,(300,300))

cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
