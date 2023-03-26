# import cv2
#
# class collector:
#     def  __init__(self):
#         self.cap = cv2.VideoCapture(0)
#         _, self.frame = self.cap.read()
#     def fetch(self):
#         if not self.cap.isOpened():
#             print("无法打开摄像头")
#             exit()
#         # 从摄像头读取一帧图像
#         ret, self.frame = self.cap.read()
#         # 检查是否成功读取了图像
#         if not ret:
#             print("无法读取摄像头")
#             exit()
#             # 释放摄像头资源
#         self.cap.release()
#     def get(self):
#         return self.frame
#     def  __del__(self):
#         self.cap.release()
#
#
# ccc = collector()
# ccc.fetch()
# cv2.imshow("frame", ccc.get())


# def fetch_image():
#     # 创建 videoCapture 对象
#     cap = cv2.VideoCapture(0)
#     while True:
#         if cap.isOpened():
#             cv2.waitKey(50)
#             ret, frame = cap.read()
#             if ret:
#                 cv2.imwrite('image.jpg', frame)
#             # 释放摄像头资源
#             cap.release()
#             break
#
# def get_image():
#     return cv2.imread('')
#
# fetch_image()
import cv2
import time


class Collector:
    def __init__(self, camera_id):
        self.camera_id = camera_id
        self.camera = cv2.VideoCapture(camera_id)

    def capture_image(self):
        _, image = self.camera.read()
        # print(len(image),len(image[0]))
        return image

    # def send_image_to_database(self, image):

    # send image to database

    def run(self):
        image = self.capture_image()
        cv2.imshow("camera", image)
        # self.send_image_to_database(image)
        # time.sleep(5)
        # while(1):
        #     pass
    def release(self):
        self.camera.release()

# 调试模块用
if __name__ == '__main__':
    coll = Collector(0)
    coll.run()

# cv2.destroyAllWindows()
