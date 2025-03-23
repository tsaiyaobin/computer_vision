import cv2

# HSV 轉 RGB
# RGB 轉 HSV
# RGB 轉 YCvCr
# luminance:亮度 / chrominance:彩度

image = cv2.imread("img.jpg")

B,G,R = cv2.split(image)
print(B+G+R)
# 正規化後較不受光源影響
b = B / (B+G+R+1e-6)
g = G / (B+G+R+1e-6)
r = R / (B+G+R+1e-6)
img2 = cv2.merge((b,g,r)) 
    
# Hue [0,179] / Saturation [0,255] / Value : HSV [0,255]


