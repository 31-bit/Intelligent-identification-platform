import cv2

def fetch_image(camera_id):
    cap = cv2.VideoCapture(camera_id, cv2.CAP_ANY)
    _, image = cap.read()
    # it takes several hundreds to get a none-zero pic
    cnt = 0
    while image.all() == 0:
        _, image = cap.read()
        cnt += 1
        if cnt > 5000:
            print("Failed to read image in limited time")
            break
    else:
        cv2.imshow("camera", image)
        cv2.imwrite("temp_images.jpg", image)
        print("first none zero picture read at",cnt,"trials")
    cap.release()
    return image

# send image to database

# 调试模块用
if __name__ == '__main__':
    # print(cv2.getBuildInformation())
    fetch_image(0)
