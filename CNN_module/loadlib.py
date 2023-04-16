import cv2
import os
import numpy as np

def load_data(data_dir, y_label, MAX_capcacity = float('inf')):
    x_train = []
    y_train = []
    raw_img = []  # the image not be resized, used for storing.
    for subdir, _, files in os.walk(data_dir):
        cnt = 0
        for file in files:
            if file.endswith(".jpg")or file.endswith(".png"):
                img_path = os.path.join(subdir, file)
                img = cv2.imread(img_path)
                if file.endswith(".png"): # opencv read png with BGR default
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # enable when input image format is BGR
                img = cv2.resize(img, (224, 224))
                raw_img.append(img)
                x_train.append(img)
                y_train.append(y_label)
                cnt+=1
            if cnt > MAX_capcacity:
                break
    x_train = np.array(x_train)
    y_train = np.array(y_train)

    return x_train, y_train, raw_img

def user_defined_load():
    x_train_temp1, y_train_temp1, _ = load_data("/Users/leonard/PycharmProjects/opencv/data/data_train/vehicles", 1, 200)
    x_train_temp2, y_train_temp2, _= load_data("/Users/leonard/PycharmProjects/opencv/data/data_train/non-vehicles", 0, 200)
    x_train = np.r_[x_train_temp1, x_train_temp2]
    y_train = np.r_[y_train_temp1, y_train_temp2]


    x_test_temp1, y_test_temp1,raw1 = load_data("/Users/leonard/PycharmProjects/opencv/data/data_test/vehicles", 1, 200)
    x_test_temp2, y_test_temp2,raw2= load_data("/Users/leonard/PycharmProjects/opencv/data/data_test/non-vehicles", 0, 200)
    x_test = np.r_[x_test_temp1, x_test_temp2]
    y_test = np.r_[y_test_temp1, y_test_temp2]

    raw1.extend(raw2)
    return (x_train,y_train), (x_test, y_test),raw1

# 调试模块用
if __name__ == '__main__':
    load_data("/Users/leonard/PycharmProjects/opencv/Stanford_dataset/cars_train", 1,200)
    load_data("/Users/leonard/PycharmProjects/opencv/data/vehicles", 1,200)