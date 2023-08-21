import cv2

img = cv2.imread( 'face_test.jpg' )
gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
faceCascade = cv2.CascadeClassifier( 'face_detect.xml' )
faceRect = faceCascade.detectMultiScale( gray, 1.1, 24 )
print(len(faceRect))

for ( x, y, w, h ) in faceRect : 
    cv2.rectangle( img, (x, y), (x+w, y+h), (0 ,255, 0), 2 )

img = cv2.resize( img, (0, 0), fx = 0.5, fy = 0.5)

cv2.imshow( 'img', img ) 
cv2.waitKey( 0 )