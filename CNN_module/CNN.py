from loadlib import load_data
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import cifar10
from keras import layers
from sklearn.utils import shuffle


x_train_temp1, y_train_temp1 = load_data("/Users/leonard/PycharmProjects/opencv/data/data_train/vehicles", 1, 200)
x_train_temp2, y_train_temp2 = load_data("/Users/leonard/PycharmProjects/opencv/data/data_train/non-vehicles", 0, 200)
x_train = np.r_[x_train_temp1,x_train_temp2]
y_train = np.r_[y_train_temp1,y_train_temp2]
x_train,y_train = shuffle(x_train,y_train)

x_test_temp1, y_test_temp1 = load_data("/Users/leonard/PycharmProjects/opencv/data/data_test/vehicles", 1, 200)
x_test_temp2, y_test_temp2 = load_data("/Users/leonard/PycharmProjects/opencv/data/data_test/non-vehicles", 0, 200)
x_test = np.r_[x_test_temp1,x_test_temp2]
y_test = np.r_[y_test_temp1,y_test_temp2]
x_test,y_test = shuffle(x_test,y_test)

x_train = x_train / 255.0
x_test = x_test / 255.0

model = tf.keras.Sequential([
    # 卷积层
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    # 全连接层
    layers.Dense(512, activation='relu'),
    # Dropout层，用于防止过拟合
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss= 'binary_crossentropy',
              metrics=['accuracy'])
# loss =tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
