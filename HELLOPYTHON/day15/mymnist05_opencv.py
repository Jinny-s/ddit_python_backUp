from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
import numpy as np
import cv2

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
(train_images_org, train_labels_org), (test_images_org, test_labels_org) = mnist.load_data()

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=128)

predictions = model.predict(test_images)


cnt = 0
for i, pred in enumerate(predictions):
    # if int(np.where(test_labels[i]==1)[0]) != pred.argmax():
    if test_labels_org[i] != pred.argmax():
        cv2.imwrite('miss/'+str(predictions[i].argmax())+'_'+str(test_labels_org[i])+'_'+str(i)+'.jpg', test_images_org[i])
        cnt += 1

print('틀린개수 :', cnt, '/ 정답개수 :', len(predictions) - cnt)
print('정답률 :', (len(predictions) - cnt) / len(predictions) * 100,'%')

# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print('test_acc: ', test_acc)
