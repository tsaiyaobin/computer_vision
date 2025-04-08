import cv2

#-----------------
#--顯示一般攝影機--
#-----------------

# 這裡要加 x 不然會報錯
def nothing(x): 
    pass 

cap = cv2.VideoCapture(0)
# ret回傳布林值, 取得圖像偵
if not cap.isOpened():
    print("無法打開攝像頭 ")
cv2.namedWindow('image')
cv2.createTrackbar('Bin', 'image', 0, 255, nothing)

while True:
    ret, frame = cap.read()
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 要先轉灰階在做二值
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break    
   
    b = cv2.getTrackbarPos('Bin', 'image') 
    ret2,th=cv2.threshold(frame, b, 255, cv2.THRESH_BINARY)
    cv2.imshow('image', th)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()

cv2.destroyAllWindows()

'''
img=cv2.imread("img.jpg",0)
img=cv2.resize(img,(300,300))

ret,th=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('th',th)
cv2.waitKey()
cv2.destroyAllWindows()
'''