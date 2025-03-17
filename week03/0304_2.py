import cv2

#-----------------
#--顯示一般攝影機--
#-----------------
cap = cv2.VideoCapture(0)
# ret回傳布林值, 取得圖像偵
if not cap.isOpened():
    print("無法打開攝像頭 ")
fourcc=cv2.VideoWriter_fourcc(*'mp4v')
video=cv2.VideoWriter('output_video.mp4',fourcc,30,(640,480))    
    
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imshow('frame', frame)
    
    video.write(frame) # 視訊存成影片
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
video.release() #影片釋放
cv2.destroyAllWindows()
#--------------------------------
#--開第二次攝影機，只顯示紅色通道--
#--------------------------------
cap = cv2.VideoCapture(0)
# ret回傳布林值, 取得圖像偵
if not cap.isOpened():
    print("無法打開攝像頭 ")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #影片是由每個frame組成 所以對每個frame的bg都拿掉就只會剩下r
    b,g,r = cv2.split(frame) # 把 b g r 分開
    b[:]=0 # 
    g[:]=0 #
    r_color=cv2.merge((b,g,r))
    cv2.imshow('r channel',r_color)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
# ret回傳布林值, 取得圖像偵
if not cap.isOpened():
    print("無法打開攝像頭 ")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    b,g,r = cv2.split(frame) 
    # cv2 的排序是 bgr 所以我把原圖的bg交換就可以做到交換藍綠通道
    gbr_color=cv2.merge((g,b,r)) 
    cv2.imshow('b g change',gbr_color)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()