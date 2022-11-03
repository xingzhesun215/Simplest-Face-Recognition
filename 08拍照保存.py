import cv2 as cv

# 打开摄像头
cap = cv.VideoCapture(0)

count = 1

while (cap.isOpened()):  # 检测摄像头是否开启
    ret_flag, Vshow = cap.read()  # 得到每帧数据
    cv.imshow("Capture", Vshow)  # 显示预览

    k = cv.waitKey(1) & 0xFF  # 按键判断
    if (k == ord('s')):
        cv.imwrite(str(count) + "_camera.jpg", Vshow)  # 保存
        print("Success to save " + str(count) + "_camera.jpg\n")
        count += 1
    elif k == ord(" "):  # 退出
        break
# 释放摄像头
cap.release()
# 释放窗口内存
cv.destroyAllWindows()
