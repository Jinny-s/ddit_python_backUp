import cv2
 
img = cv2.imread('urimi.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(gray) 

cv2.imshow('Test Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# 이미지 다른 파일로 저장
# cv2.imwrite('test2.png', img)