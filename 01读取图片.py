# 导入cv2模块,别名为cv
import cv2 as cv

# 读取图片
img = cv.imread("face1.jpg")

# 显示窗口到窗口上,窗口名就是read_img
cv.imshow("read_img", img)

# 窗口等待 0为不自动关闭 其他数值为等待时间,单位为毫秒,返回为按键的ASCII
key = cv.waitKey(0)  # 此代码不写会闪现窗口

# 释放内存,销毁窗口
cv.destroyAllWindows()
