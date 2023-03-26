import cv2

# 创建摄像头对象
cap = cv2.VideoCapture(0)

# 检查摄像头是否打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 循环读取并显示摄像头中的帧
while True:
    # 从摄像头读取一帧图像
    ret, frame = cap.read()

    # 检查是否成功读取了图像
    if not ret:
        print("无法读取摄像头")
        break

    # 显示图像
    cv2.imshow("Camera", frame)

    # 按下 q 键退出循环
    if cv2.waitKey(1) == ord("q"):
        break

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()
