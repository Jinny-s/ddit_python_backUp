import cv2
 
img = cv2.imread('urimi.jpg', 1)
cropped_img = img[0:300,115:330]

print('세로',len(img))
print('가로',len(img[0]))

cv2.imshow('Test Image', cropped_img)
cv2.imwrite('face.jpg', cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows() 