import cv2 as cv
import os


def face_detect_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier(
        "haarcascade/haarcascade_frontalface_default.xml")  # 级联分类器
    # gray表示传入的灰度图(快速查询) 1.1表示每次搜索窗口依次扩大10% 5表示构成检测目标的相邻矩形的最小个数(默认为3个) (100,100)表示最小人脸大小 (300,300)表示最大人脸大小
    face = face_detector.detectMultiScale(gray, 1.1, 5, cv.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=1)
        ids, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        if confidence > 80:#差别较大,当做不认识
            cv.putText(img, "unknow" + str(confidence), (x + 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            cv.putText(img, str(names[ids - 1]) + str(confidence), (x + 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.75,
                       (0, 255, 0), 1)
    cv.imshow("result", img)


def getName():
    path = 'data/face/'
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        name = str(os.path.split(imagePath)[1].split('-', 2)[1])
        names.append(name)


names = []

getName()
recognizer = cv.face.LBPHFaceRecognizer_create()

recognizer.read('trainer/trainer.yml')#加载人脸特征值,之前训练出来的

warningtime = 0

img = cv.imread("p6.jpg")#识别图片
face_detect_demo(img)
cv.waitKey(0)

cap = cv.VideoCapture("2.mp4")
while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)#视频每一帧识别

    cv.waitKey(1)
