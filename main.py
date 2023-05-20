import cv2

image = cv2.imread("ai.jpg", cv2.IMREAD_UNCHANGED)

scalepercent = 50

new_hieght = int(image.shape[1] * scalepercent / 100)
new_width =  int(image.shape[0] * scalepercent / 100)


output = cv2.resize(image, (new_hieght, new_width)) #resizing the image


cv2.imwrite('newImage.png', output)

cv2.waitKey(0)