import cv2

scalepercent = 50
source = ai.jpg
destination = newImage.png

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)

new_hieght = int(image.shape[1] * scalepercent / 100)
new_width =  int(image.shape[0] * scalepercent / 100)


output = cv2.resize(image, (new_hieght, new_width)) #resizing the image


cv2.imwrite(destination, output)
cv2.waitKey(0)