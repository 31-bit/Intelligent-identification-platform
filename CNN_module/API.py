import os
from tensorflow import keras
from loadlib import user_defined_load
from CNN_module.CNN import create_my_model
from sklearn.utils import shuffle

def training():
    # load data and preprocessing
    user_defined_load()
    (x_train, y_train), (x_test, y_test) = user_defined_load()  # change path and Max picture, go into the user_defined_load
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

    # 输出 保存

def predict():
    # todo rerwite the loading data
    (x_train, y_train), (X, y_test) = user_defined_load()
    X = X / 255.0

    # 定义模型保存路径
    model_path = "model/model_car.h5"
    if os.path.exists(model_path):
        model = keras.models.load_model(model_path)
        print("已加载训练好的模型。")
    else:
        print("未在路径内找到模型，请训练模型或更改模型目录")
    predictions = model.predict(X)
    return predictions

if __name__ == "__main__":
    print(predict())
