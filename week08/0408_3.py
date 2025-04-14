'''
contours, hierarchy=cv2.findContours(image, mode, method)

hierarchy:是輪廓的層次信息，他描述了每個輪廓的關西

參數image是待處理的灰階或二值圖像，mode表示輪廓檢測模式，method表示輪廓逼近方法

mode有四種 : cv2.RETR_EXTERNAL：只檢索最外層輪廓；
             cv2.RETR_LIST：檢索所有輪廓，不建立層次關係；
             cv2.RETR_CCOMP：檢索所有輪廓，建立兩層層次關係；
             cv2.RETR_TREE：檢索所有輪廓，建立完整的層次結構。
             
Contour approximation method參數有三種可選：
 cv2.CHAIN_APPROX_NONE：儲存所有輪廓點
 cv2.CHAIN_APPROX_SIMPLE：壓縮水平、垂直和對角方向的點，只儲存端點；
 cv2.CHAIN_APPROX_TC89_KCOS：使用TehChin鏈碼逼近算法。      
'''

'''
image = cv2.drawContours(src_image, contours, contourIdx, 
color, thickness, lineType, hierarchy, maxLevel, offset)

    src_image：要繪製輪廓的圖像。
    contours：findContours所獲得的 list，包含所有的輪廓
    contourIdx：要繪製的輪廓索引，負數表示繪製所有輪廓。
    color：繪製輪廓的顏色，用BGR格式設定顏色。
    thickness：optional, 輪廓線的寬度，負數則填充輪廓區域(實心)。
    lineType：optional，cv2.LINE_4,cv2.LINE_8, or cv2.LINE_AA。
    hierarchy：optional, findContours()輸出的層級信息。
    maxLevel：optional, 繪製最大層次深度, n表示0至n 層。
    offset：optional, 每個輪廓點的偏移量
'''
import cv2
image=cv2.imread('img.jpg',0)
image=cv2.resize(image,(473,572))
contours, hierarchy=cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
dst = cv2.drawContours(image,contours,-1,(0,255,0),5) # 繪製圖形輪廓
cv2.imshow("drawed _contour",dst)
cv2.waitKey()
cv2.destroyAllWindows()
