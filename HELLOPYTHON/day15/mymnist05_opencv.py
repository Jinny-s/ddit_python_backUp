from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
import numpy as np
import cv2

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images_refine = test_images.reshape((10000, 28 * 28))test_images_refine = test_images_refine.astype('float32') / 255

train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=20, batch_size=128)

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
        cv2.imwrite('miss/'+str(idx)+'_'+str(mypred)+'_'+str(mygool)+'.jpg', test_images[idx])
    
print('틀린개수 :', cnt_o, '/ 정답개수 :', cnt_x)
print('정답률 :', cnt_o / len(predictions) * 100,'%')

# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print('test_acc: ', test_acc)
