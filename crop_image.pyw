import cv2
img = cv2.imread("bird.jfif")
img_cropped = img[0:200,0:200]
cv2.imshow("Original image", img)
cv2.imshow("Cropped image", img_cropped)
cv2.waitKey(2000)