import os
import glob
import re
def generate_file_name(path):
    folder_path = path
    # 获取已有文件名
    files = glob.glob(folder_path + "/*")
    # 提取数字部分
    nums = []
    for f in files:
        match = re.search(r'\d+', f)
        if match:
            nums.append(int(match.group()))
    # 生成新的文件名
    if not nums:
        new_file_name = "image{}.jpg".format(1)
    else:
        new_file_name = "image{}.jpg".format(max(nums) + 1)
    return new_file_name  # 输出类似 "image3.jpg" 的文件名


if __name__ == "__main__":
    print(generate_file_name("/Users/leonard/PycharmProjects/opencv/data/data_test/non-vehicles"))