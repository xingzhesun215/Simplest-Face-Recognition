import cv2 as cv

# 读取原图
img = cv.imread("face1.jpg")

# 修改尺寸
resize_img = cv.resize(img, dsize=(200, 200))
# 显示原图
cv.imshow("img", img)
# 显示修改图,最大化也是修改后的图
cv.imshow("resize_img", resize_img)

# 打印修改前后的图片尺寸信息
print("未修改", img.shape)
print("修改后", resize_img.shape)

# 按键为q时退出窗口等待
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存,销毁窗口
cv.destroyAllWindows()
