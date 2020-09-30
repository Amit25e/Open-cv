import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)#here 0 means default webcam

cap.set(3, frameWidth)#used to give the width of the video needed
cap.set(4, frameHeight)#used to give the Hieght of the video needed
cap.set(10,150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break