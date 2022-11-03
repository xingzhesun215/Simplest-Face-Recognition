# 导入cv模块
import cv2 as cv

# 读取图片
img = cv.imread("face1.jpg")
# 灰度转换
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 窗口显示灰度图
cv.imshow("gray", gray_img)
# 保存灰度图
cv.imwrite("face1_gray.jpg", gray_img)
# 显示原图
cv.imshow("img", img)
# 等待
cv.waitKey(0)
# 销毁
cv.destroyAllWindows()
