import cv2
import numpy as np

img = cv2.imread("img.jpg")
img = cv2.resize(img, (473, 572))
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

# ycrcb 膚色區間
lower = np.array([0, 153, 77])

higher = np.array([255, 173, 127])

mask = cv2.inRange(ycrcb, lower, higher)

res = cv2.bitwise_and(img, img, mask=mask) 

contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    
    contour = max(contours, key=cv2.contourArea)  # 找最大輪廓
    # 包圍矩形
    (x, y, w, h) = cv2.boundingRect(contour)
    dst = cv2.rectangle(img.copy(), (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('dst', dst)
    
    # 最小包圍矩形
    box = cv2.minAreaRect(contour)
    points = cv2.boxPoints(box)
    points = points.astype(int)
    dst1 = cv2.drawContours(img.copy(), [points], 0, (0, 255, 0), 1)
    cv2.imshow('dst1', dst1)
    
    # 最小包圍圓形
    ((x, y), radius) = cv2.minEnclosingCircle(contour)
    dst2 = cv2.circle(img.copy(), (int(x), int(y)), int(radius), (0, 255, 0), 2)
    cv2.imshow('dst2', dst2)
    
    # 最優擬合橢圓
    ellipse = cv2.fitEllipse(contour)
    dst3 = cv2.ellipse(img.copy(), ellipse, (0, 255, 0), 2)
    cv2.imshow('dst3', dst3)


cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()


