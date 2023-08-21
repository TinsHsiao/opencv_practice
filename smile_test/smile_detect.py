from cgi import test
import cv2
from cv2 import resize

t = cv2.imread( 'test.jpg' )
t = resize( t, (0, 0), fx = 0.5, fy = 0.5 )
gray = cv2.cvtColor( t, cv2.COLOR_BGR2GRAY )
faceCascade = cv2.CascadeClassifier( 'smile_detect.xml' )
faceRect = faceCascade.detectMultiScale( gray, 1.5, 20 )
print(len(faceRect))

for ( x, y, w, h ) in faceRect : 
    cv2.rectangle( t, (x, y), (x+w, y+h), (0 ,255, 0), 2 )



cv2.imshow( 't', t ) 
cv2.waitKey( 0 )