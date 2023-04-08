from loadlib import load_data, user_defined_load
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import cifar10
from keras import layers
from sklearn.utils import shuffle


def create_my_model():
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
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model
if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = user_defined_load()  # change path and Max picture, go into the user_defined_load
    # shuffle the non-car data and car data
    x_train, y_train = shuffle(x_train, y_train)
    x_test, y_test = shuffle(x_test, y_test)
    # normalization
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
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    # loss =tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))