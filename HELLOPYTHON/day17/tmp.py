from tensorflow.keras import datasets, layers, models
import cv2
import numpy as np

cifar10 = datasets.cifar10 
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

train_images_refine = train_images.reshape((50000, 32, 32, 3))
train_images_refine = train_images_refine / 255.0

print(train_images_refine)





img = cv2.imread('cifar1.jpg', 1)
img_resize = cv2.resize(img, dsize=(32,32))
img_refine = img_resize.reshape(1, 32, 32, 3)
print(img_refine)

# cv2.imshow('img', img_resize)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()