import cv2
import numpy as np

img = cv2.imread("img.jpg")
img = cv2.resize(img,(300,300))

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

