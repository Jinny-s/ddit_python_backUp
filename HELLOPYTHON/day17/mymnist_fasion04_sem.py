import tensorflow as tf
import cv2
import numpy as np

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['Shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images_refine = train_images / 255.0
test_images_refine = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images_refine, train_labels, epochs=1)

img = cv2.imread('test4.jpg', cv2.IMREAD_GRAYSCALE)
img_resize = cv2.resize(img, dsize=(28,28))
cv2.imshow('img', img_resize)
img_refine = (255-img_resize) / 255.0
img_refine = img_refine.reshape((1,28,28))


predictions = model.predict(img_refine)
print(predictions)
print(np.argmax(predictions))
print(class_names[np.argmax(predictions)])

cv2.waitKey(0)
cv2.destroyAllWindows()