import cv2



cap = cv2.VideoCapture(1)

while True :
    ret, frame = cap.read()
    frame = cv2.resize( frame, (0, 0), fx=0.4, fy=0.4 )
    if ret : 
        cv2.imshow( 'video', frame )
    else : 
        break
    if cv2.waitKey(10) == ord('q') :
        break