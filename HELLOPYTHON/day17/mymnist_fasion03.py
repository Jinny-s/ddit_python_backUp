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

model.fit(train_images_refine, train_labels, epochs=50)

# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
# print('\nTest accuracy:', test_acc)

predictions = model.predict(test_images_refine)

cnt_o = 0
cnt_x = 0
for idx, pred in enumerate(predictions):
    mypred = np.argmax(pred)
    mygool = test_labels[idx]
    if mypred == mygool:
        cnt_o += 1
    else:
        cnt_x += 1
        cv2.imwrite('image_miss/'+str(idx)+'_'+str(mypred)+'_'+str(mygool)+'.jpg', test_images[idx])
    
print('정답개수 :', cnt_o, '/ 틀린개수 :', cnt_x)
print('정답률 :', cnt_o / len(predictions) * 100,'%')