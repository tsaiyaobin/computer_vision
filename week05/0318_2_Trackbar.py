import cv2


# 滑竿 cv2.createTrackbar('滑竿名稱', '視窗名稱', min, max, fn)
# cv2.getTrackbarPos('<Trackbar_name>','<Window_name>')
# min 最小值, max 最大值

def nothing(x):
    pass
img = cv2.imread('img.jpg')

cv2.namedWindow('image')

cv2.createTrackbar('B', 'image', 0, 255, nothing)

cv2.createTrackbar('G', 'image', 0, 255, nothing)

cv2.createTrackbar('R', 'image', 0, 255, nothing)
switch='0:OFF \n1 :ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while (1):
    cv2.imshow('image',img)
    q=cv2.waitKey(1)
    if q == ord("q"):
        break
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
cv2.destroyAllWindows()
