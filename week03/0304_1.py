import cv2
import sys

img = cv2.imread('jia.jpg')
if img is None:
    sys.exit("could not read the image")

img2 = cv2.resize(img,(236,512))
print('original shpae',img2.shape)

b,g,r = cv2.split(img2)
print('g channel=1',g.shape)
cv2.imshow('gray photo',g)
q = cv2.waitKey(0)
cv2.destroyAllWindows()

img3 = cv2.merge((b,g,r)) 
print('all color shpae1',img3.shape)
cv2.imshow('my photo',img3)
q = cv2.waitKey(0)
cv2.destroyAllWindows()

#單獨秀出藍色通道
r[:] = 0
g[:] = 0
g_color=cv2.merge((b,g,r))
print('g channel=3',g.shape) 
cv2.imshow('green photo',g_color)
cv2.waitKey(0)

'''
除存影像
if q == ord("q"):
    cv2.imwrite("new_photo.jpg",img2)
'''
cv2.destroyAllWindows()


























