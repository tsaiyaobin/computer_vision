import cv2
import numpy as np

img = cv2.imread("img.jpg")
img = cv2.resize(img,(300,300))

# M=cv2.getPerspectiveTransform(src, dst)
size=img.shape
print(size)
# 原始影像的四個點
a1=[0,0]
b1=[size[0]-1,0]
c1=[0,size[1]-1]
d1=[size[0]-1,size[1]-1]
src1=np.array([a1,b1,c1,d1],dtype="float32")

# 要將原本四個點要移過去的四個座標
a2=[50,0]
b2=[250,0]
c2=[50,size[1]-1]
d2=[250,size[1]-1]
dst1=np.array([a2,b2,c2,d2],dtype="float32")

# 如果做透視轉換是3*3矩陣不能用 warpAffine(2*3) 要用 warpPerspective(3*3)
M=cv2.getPerspectiveTransform(src1, dst1)
img2=cv2.warpPerspective(img,M,(300,300))

cv2.imshow("img",img)
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
