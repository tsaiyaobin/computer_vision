import cv2

# 加權式相加 cv2.addWeighted(img1,0.7,img2,0.3,0)

img1 = cv2.imread("img.jpg",1)
img2 = cv2.imread("img2.jpg",1)

img3 = cv2.resize(img1,(900,900))
img4 = cv2.resize(img2,(900,900))
wei1=0.00
wei2=1.00
while wei1<1:
    img5 = cv2.addWeighted(img3,wei1,img4,wei2,0)
    wei1+=0.05
    wei2-=0.05
    print(wei1,wei2)
    cv2.imshow('img',img5)
    if cv2.waitKey(500) == ord("k"):
        break
    
cv2.destroyAllWindows()

#cv2.imwrite('add_weight.jpg',img5) 