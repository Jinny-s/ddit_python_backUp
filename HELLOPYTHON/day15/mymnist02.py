import cv2
from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()



for i, img in enumerate(test_images):
    print(i)
    cv2.imwrite('test/'+str(test_labels[i])+'_'+str(i)+'.jpg', img)
    if i > 100:
        break