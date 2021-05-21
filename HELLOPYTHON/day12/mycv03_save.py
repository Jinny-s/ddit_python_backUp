import cv2
 
img = cv2.imread('urimi.jpg', 1)

print(img) 

cv2.imshow('Test Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
cv2.imwrite('urm.jpg', img)