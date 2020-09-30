import cv2
img=cv2.imread("bird.jfif")
imgblur=cv2.GaussianBlur(img , (7,7) , 0)
cv2.imshow("Blur Image",imgblur)
cv2.waitKey(2000)