import cv2

img = cv2.imread("23callalily.jpg",1)

# 替換像素值
img[0:341,512:1024]=[125,125,125]

cv2.imshow('p1',img)

cv2.waitKey(0)
cv2.destroyAllWindows()