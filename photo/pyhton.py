import cv2


img=cv2.imread("left3.png")

img=cv2.bitwise_not(img)
cv2.imshow("imgg",img)

print(img)
##cv2.imwrite("logo_hover.jpg",img)
