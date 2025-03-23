import cv2
import numpy as np
img = cv2.imread("img.jpg")
ycrcb = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)

# ycrcb 的膚色檢測門檻
lower = np.array([ 0, 153, 77])
higher = np.array([ 255, 173, 127])

mask=cv2.inRange(ycrcb,lower,higher)

res=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow('frame', img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()