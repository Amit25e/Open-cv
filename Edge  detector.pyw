import cv2
img=cv2.imread("bird.jfif")
img_2= cv2.Canny(img , 100 ,100)
cv2.imshow("GrayImage",img_2)
cv2.waitKey(2000)