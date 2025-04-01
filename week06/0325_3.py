import cv2
import numpy as np

img = cv2.imread("img.jpg")
img = cv2.resize(img,(300,300))

#cv2.getRotationMatrix2D(center, angle, scale)
M=cv2.getRotationMatrix2D((150,150), 45,1)
img2=cv2.warpAffine(img,M,(300,300))

cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
