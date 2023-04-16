import os
from tensorflow import keras
from loadlib import user_defined_load
from CNN_module.CNN import create_my_model
from sklearn.utils import shuffle
import cv2
from common import generate_file_name

def training():
    # load data and preprocessing
    user_defined_load()
    (x_train, y_train), (x_test, y_test) ,_= user_defined_load()  # change path and Max picture, go into the user_defined_load
    # shuffle the non-car data and car data
    x_train, y_train = shuffle(x_train, y_train)
    x_test, y_test = shuffle(x_test, y_test)
    # normalization
    x_train = x_train / 255.0
    x_test = x_test / 255.0

    # 定义模型保存路径
    model_path = "model/model_car.h5"
    # 如果已有训练好的模型，则加载该模型
    if os.path.exists(model_path):
        model = keras.models.load_model(model_path)
        print("已加载训练好的模型。")
        history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))
        # 保存模型
        model.save(model_path)
    else:
        # 创建新的模型并训练
        model = create_my_model()
        # training model
        history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))
        # 保存模型
        model.save(model_path)
        print("已训练并保存模型。")
    return
    # 输出 保存

def predict():
    # todo rerwite the loading data
    (x_train, y_train), (X, y_test), raw_img= user_defined_load()
    X = X / 255.0

    # 定义模型保存路径
    model_path = "model/model_car.h5"
    if os.path.exists(model_path):
        model = keras.models.load_model(model_path)
        print("已加载训练好的模型。")
    else:
        print("未在路径内找到模型，请训练模型或更改模型目录")
    y_pred = model.predict(X)
    y_pred = (y_pred > 0.5).astype(int)

    # 找到预测错误的数据
    for i, val in enumerate(y_pred):
        if val == 1:
            img_name = generate_file_name("/Users/leonard/PycharmProjects/opencv/data_predict/car")
            cv2.imwrite(img_name, raw_img[i])
        elif val == 0:
            img_name = generate_file_name("/Users/leonard/PycharmProjects/opencv/data_predict/non_car")
            cv2.imwrite(img_name, raw_img[i])

    return y_pred

if __name__ == "__main__":
    training()
    # print(predict())

