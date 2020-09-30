#code for displaying a picture
#The code may show error but, willl work fine
import cv2 #import open cv package
img = cv2.imread("bird.jfif")# Store the image in a variable
cv2.imshow("output", img)#Display the image. The word output is the name of window and can be changed
cv2.waitKey(0)#delay. (in miliseconds). 0 can be written to keep it for unlimited time