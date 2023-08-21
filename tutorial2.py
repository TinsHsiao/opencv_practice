import cv2
import numpy as np # 取名為np
import random

"""
img = cv2.imread( "colorcolor.jpg" )
#print( type(img) ) # nd是多維
print( img.shape )
# R  G  B
# 紅 綠 藍
# B  G  R in opencv
[
    [ [0, 255, 0], [255, 0,0 ], [0, 0, 255], ... 700 ],
    [ [], [], [], ... 700 ],
    [ [], [], [], ... 700 ],
    ...1015
]
"""


"""
# 創建一張random的圖片
img = np.empty( (300, 300, 3), np.uint8 ) # 創建多維陣列 各個維度 0-255 => 8 bits uint 正整數
for row in range(300) :
    for col in range(img.shape[1]) :
        img[row][col] = [random.randint( 0, 255),random.randint( 0, 255),random.randint( 0, 255)]

cv2.imshow( 'img', img )
cv2.waitKey(1000)
"""


"""
# 將照片的前300列改成random的顏色
img = cv2.imread( "colorcolor.jpg" )

for row in range(300) :
    for col in range(img.shape[1]) :
        img[row][col] = [random.randint( 0, 255),random.randint( 0, 255),random.randint( 0, 255)]

cv2.imshow( 'img', img )
cv2.waitKey(1000)
"""

img = cv2.imread( "colorcolor.jpg" )

newImg = img[:150, 200:400]
cv2.imshow( 'img', img)
cv2.imshow( 'newImg', newImg )
cv2.waitKey(0)