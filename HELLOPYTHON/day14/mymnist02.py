import tensorflow as tf

# 1. MNIST �뜲�씠�꽣�꽬 �엫�룷�듃
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. �뜲�씠�꽣 �쟾泥섎━
x_train, x_test = x_train/255.0, x_test/255.0

# 3. 紐⑤뜽 援ъ꽦
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# 4. 紐⑤뜽 而댄뙆�씪
model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

# 5. 紐⑤뜽 �썕�젴
model.fit(x_train, y_train, epochs=20)

# 6. 紐⑤뜽 ���옣
model.save('model1.h5')