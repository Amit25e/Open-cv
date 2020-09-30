import cv2
img=cv2.imread("bird.jfif")
img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImage",img_gray)
cv2.waitKey(2000)