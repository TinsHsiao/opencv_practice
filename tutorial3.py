import cv2
import numpy as np

kernel = np.ones( (5, 5), np.uint8 ) # kernel越大 膨脹越
kernel1 = np.ones( (5, 5), np.uint8 )

# 轉灰階圖片
img = cv2.imread('colorcolor.jpg')
img = cv2.resize( img, (0, 0), fx = 0.5, fy = 0.5 )
gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
blur = cv2.GaussianBlur( img, (1, 27), 10 ) # 核大小須要是奇數

canny = cv2.Canny( img, 150, 200 )
# 計算與周圍的像素值大小 若低於前面的數字就不當作邊緣 若大於後面的數字就當作邊緣

# 膨脹圖片
dilate = cv2.dilate( canny, kernel, iterations=1 ) # iteration越大膨脹越大

# 使線條變細
erode = cv2.erode( dilate, kernel1, iterations=1 )

cv2.imshow( 'img', img )
### cv2.imshow( 'gray', gray )
### cv2.imshow( 'blur', blur )
cv2.imshow( 'canny', canny ) 
cv2.imshow( 'dilate', dilate )
cv2.imshow( 'erode', erode )
cv2.waitKey(0)