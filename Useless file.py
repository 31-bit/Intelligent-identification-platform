import cv2

# 创建摄像头对象
# cap = cv2.VideoCapture(0，cv2.CAP_FFMPEG)
cap = cv2.VideoCapture(0, cv2.CAP_ANY )
#cv2.CAP_FFMPEG cv2.CAP_GSTREAMER
# 检查摄像头是否打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 循环读取并显示摄像头中的帧
while True:
    # 从摄像头读取一帧图像
    ret, frame = cap.read()
    print(type(frame))
    print(len(frame))
    # 检查是否成功读取了图像
    if not ret:
        print("无法读取摄像头")
        break

    # 显示图像
    cv2.imshow("Camera", frame)
    # 按下 q 键退出循环
    if cv2.waitKey(1) == ord("q"):
        break

# 释放摄像头资源q
cap.release()
cv2.destroyAllWindows()
