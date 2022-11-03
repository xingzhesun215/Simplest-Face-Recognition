import cv2 as cv


# 检测函数 检索
def face_detect_demo():
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 转为灰度图片
    face_detect = cv.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")  # 级联分类器
    face = face_detect.detectMultiScale(gray, minSize=(30, 30))  # 检索人脸
    # 遍历所有人脸的位置信息,包括人脸位置及大小
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=1)  # 画出识别出来的人脸框
    cv.imshow("result", img)


# 读取图片
img = cv.imread("p3.jpg")
# 检测图片
face_detect_demo()

while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()
