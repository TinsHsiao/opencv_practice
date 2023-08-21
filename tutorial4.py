import cv2
import numpy as np

img = np.zeros( (600, 600, 3), np.uint8 )
cv2.line( img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 2 )
cv2.rectangle( img, (100, 100 ), (300, 300), (0, 0, 255), cv2.FILLED )
cv2.circle( img, (300, 300), 30, (0, 255, 0 ), cv2.FILLED )
cv2.putText( img, 'Hello', (200, 200),cv2.FONT_HERSHEY_DUPLEX, 1, ( 255, 255, 255), 1   )
# putText不支援中文


cv2.imshow( 'img', img )
cv2.waitKey(0)


