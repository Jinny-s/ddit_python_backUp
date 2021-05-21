import cv2
 
img = cv2.imread('urimi.jpg', 1)

print(img) 

cv2.imshow('Test Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# 이미지 다른 파일로 저장
# cv2.imwrite('test2.png', img)