import cv2
Hieght = 400
Width = 400
image_name = "bird.jfif"
delay = 2 #write in seconds
img = cv2.imread(image_name)
x = delay*1000
img = cv2.resize(img,(width,Hieght))
cv2.imshow("Image resized" , img)
cv2.waitKey(x)