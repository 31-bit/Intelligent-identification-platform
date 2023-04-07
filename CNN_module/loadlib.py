import cv2
import os
import numpy as np
# from PIL import Image
#
# def read_images(folder_path):
#     x_train = []
#     y_train = []
#     for file_name in os.listdir(folder_path):
#         if file_name.endswith(".jpg") or file_name.endswith(".png"):
#             image_path = os.path.join(folder_path, file_name)
#             # 使用Pillow库读取图像
#             img = Image.open(image_path)
#             # 将图像转换为numpy数组并缩放至相同大小
#             img_array = np.array(img.resize((224, 224)))
#             # 将图像数据添加到x_train列表中
#             x_train.append(img_array)
#             # 将标签添加到y_train列表中，这里假设文件名中包含标签信息
#             label = file_name.split("_")[0] # 假设标签信息在文件名中的第一个下划线前面
#             y_train.append(label)
#     return np.array(x_train), y_train

def load_data(data_dir, y_label, MAX_capcacity = float('inf')):
    x_train = []
    y_train = []
    for subdir, _, files in os.walk(data_dir):
        cnt = 0
        for file in files:
            if file.endswith(".jpg")or file.endswith(".png"):
                img_path = os.path.join(subdir, file)
                img = cv2.imread(img_path)
                if file.endswith(".png"): # opencv read png with BGR default
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # enable when input image format is BGR
                img = cv2.resize(img, (224, 224))
                x_train.append(img)
                y_train.append(y_label)
                cnt+=1
            if cnt > MAX_capcacity:
                break
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    return x_train, y_train

# 调试模块用
if __name__ == '__main__':
    load_data("/Users/leonard/PycharmProjects/opencv/Stanford_dataset/cars_train", 1,200)
    load_data("/Users/leonard/PycharmProjects/opencv/data/vehicles", 1,200)
