import cv2
# uint8 => u:只有正數 int:整數 8:8its => 只有正整數(含 0 )
img = cv2.imread("23callalily.jpg",1)
img2 = cv2.imread("23callalily.jpg",2)

size = img.shape
print("彩色圖:",size) #(682, 1024, 3)=>(高, 寬, 通道)

px=img[440,320]
print("彩色[440,320]的像素:",px)
# 彩色圖: (682, 1024, 3)
# 彩色[440,320]的像素: [42 61 58]

size2 = img2.shape
print("灰色圖:",size2) #(682, 1024, 3)=>(高, 寬, 通道)

px2 = img2[440,320]
print("灰色[440,320]的像素:",px2)
# 灰色圖: (682, 1024)
# 灰色[440,320]的像素: 58


cv2.imshow('p1',img)
cv2.imshow('p2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
