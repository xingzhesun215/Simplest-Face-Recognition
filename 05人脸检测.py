import cv2 as cv


# 检测函数 检索
def face_detect_demo():
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 转为灰度图片
    #电脑本地路径为E:/2022soft/py310/Lib/site-packages/cv2/data
    face_detect = cv.CascadeClassifier("haarcascade/haarcascade_frontalface_alt2.xml")  # 级联分类器
    # gray表示传入的灰度图(快速查询) 1.1表示每次搜索窗口依次扩大10% 5表示构成检测目标的相邻矩形的最小个数(默认为3个) (100,100)表示最小人脸大小 (300,300)表示最大人脸大小
    face = face_detect.detectMultiScale(gray, 1.1, 5, cv.CASCADE_SCALE_IMAGE, (30, 30), (200, 200))
    # 遍历所有人脸的位置信息,包括人脸位置及大小
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=1)  # 画出识别出来的人脸框
    cv.imshow("result", img)


# 读取图片
img = cv.imread("p4.jpg")
# 检测图片
face_detect_demo()

while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()
