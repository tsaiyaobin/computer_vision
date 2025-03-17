import cv2

img = cv2.imread("img.jpg",1)
img2 = cv2.imread("img.jpg",1)

# 框出感興趣的區域
ROI=img[1500:1640,50:330]

img2[1250:1390,410:690]=ROI

cv2.imshow("roi",ROI)
cv2.imshow("ROI",img2)
cv2.imwrite("ROi.jpg",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
