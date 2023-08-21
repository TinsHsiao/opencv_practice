from calendar import c
import cv2
from cv2 import RETR_EXTERNAL
import numpy as np
img = cv2.imread( 'shape.jpg')
imgContour = img.copy()
img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
canny = cv2.Canny( img, 150, 200 )
# 偵測輪廓
contours, hierarchy = cv2.findContours( canny, RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )

"""
for cnt in contours :
    cv2.drawContours( imgContour, cnt, -1, (255, 0, 0 ), 2 )
    print( cv2.contourArea( cnt ) )
    print( cv2.arcLength( cnt, True ) )
    peri = cv2.arcLength( cnt, True )
    vertices = cv2.approxPolyDP( cnt, peri *0.02, True )
    print( len(vertices) )
"""
for cnt in contours :
    cv2.drawContours( imgContour, cnt, -1, (255, 0, 0 ), 2 )
    area = cv2.contourArea( cnt ) 
    if area > 500 :
        # print( cv2.arcLength( cnt, True ) )
        peri = cv2.arcLength( cnt, True )
        vertices = cv2.approxPolyDP( cnt, peri *0.02, True )
        corner = len(vertices)
        x, y, w, h = cv2.boundingRect( vertices )
        cv2.rectangle( imgContour, (x, y), (x+w, y+h ), ( 0, 0, 255 ), 4 )
        if corner == 3 :
            cv2.putText(imgContour, 'triangle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2 )
        elif corner == 4 :
            cv2.putText(imgContour, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2 )
        elif corner == 5 :
            cv2.putText(imgContour, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2 )
        elif corner >= 6 :
            cv2.putText(imgContour, 'circle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2 )



cv2.imshow( 'img', img )
cv2.imshow( 'canny', canny )
cv2.imshow( 'imgContour', imgContour )
cv2.waitKey( 0 )