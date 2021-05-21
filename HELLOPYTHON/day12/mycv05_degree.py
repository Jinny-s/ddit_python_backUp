import cv2
 
img = cv2.imread('urimi.jpg', 1)

height, width, channel = img.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), -30, 1)
rotated = cv2.warpAffine(img, matrix, (width, height))

cv2.imshow('Test Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()