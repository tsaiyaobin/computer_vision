import cv2

img=cv2.imread("img.jpg",0)
img=cv2.resize(img,(300,300))
# ostu加二值化
ret,th=cv2.threshold(img,127,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret2,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('th',th)
print('cv2.THRESH_BINARY + cv2.THRESH_OTSU:',ret)
cv2.imshow('th',th2)
print('cv2.THRESH_BINARY:',ret2)
cv2.waitKey()
cv2.destroyAllWindows()