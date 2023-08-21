import cv2



# 圖片顯示
"""
img = cv2.imread( 'colorcolor.jpg' )
img = cv2.resize( img, (0, 0), fx = 0.5, fy = 0.5 )
cv2.imshow( 'img', img )
cv2.waitKey( 2000 )
"""


# 影片顯示
"""
cap = cv2.VideoCapture( 'wave.mp4' )

while True :
    ret, frame = cap.read()
    frame = cv2.resize( frame, (0, 0), fx=0.4, fy=0.4 )
    if ret : 
        cv2.imshow( 'video', frame )
    else : 
        break
    if cv2.waitKey(10) == ord('q') :
        break
"""

#視訊鏡頭 0為前鏡頭 1為後鏡頭
"""
cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()
    frame = cv2.resize( frame, (0, 0), fx=0.4, fy=0.4 )
    if ret : 
        cv2.imshow( 'video', frame )
    else : 
        break
    if cv2.waitKey(10) == ord('q') :
        break
"""

