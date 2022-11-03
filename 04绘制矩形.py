import cv2 as cv

img = cv.imread("face1.jpg")

x, y, w, h = 100, 100, 100, 100
# 坐标轴以横向右为x轴正方向,以纵向下为y轴正方向
# 画矩形框(2个点可以确定一个边与x轴y轴垂直或平行的矩形) color(b,g,r)  thickness厚度
cv.rectangle(img, (x, y, x + w, y + h), color=(0, 0, 255), thickness=1)

# 画圆形(圆点+半径即可画一个圆)
cv.circle(img, center=(x + w, y + h), radius=100, color=(0, 255, 0), thickness=1)

# 显示
cv.imshow("img", img)

while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()
