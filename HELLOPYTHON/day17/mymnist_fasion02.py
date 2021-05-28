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

model.fit(train_images_refine, train_labels, epochs=10)

for i, img in enumerate(train_images):
    print(i)
    cv2.imwrite('image_train/'+str(train_labels[i])+'_'+class_names[(train_labels[i])]+'_'+str(i)+'.jpg', img)

for i, img in enumerate(test_images):
    print(i)
    cv2.imwrite('image_test/'+str(test_labels[i])+'_'+class_names[(test_labels[i])]+'_'+str(i)+'.jpg', img)

# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
# print('\nTest accuracy:', test_acc)
#
# predictions = model.predict(test_images)
# print(predictions[0])
# print(np.argmax(predictions[0]))
# print(class_names[np.argmax(predictions[0])])
