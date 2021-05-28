from tensorflow import keras
from tensorflow.keras import datasets, layers, models
import cv2
 
cifar10 = datasets.cifar10 
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

train_images_refine = train_images.reshape((50000, 32, 32, 3))
test_images_refine = test_images.reshape((10000, 32, 32, 3))

for i, img in enumerate(train_images):
    print(i)
    cv2.imwrite('cifar_train/'+str(train_labels[i][0])+'_'+str(i)+'.jpg', img)
    if i > 100:
        break

for i, img in enumerate(test_images):
    print(i)
    cv2.imwrite('cifar_test/'+str(test_labels[i][0])+'_'+str(i)+'.jpg', img)
    if i > 100:
        break