from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import dlib
import cv2


def eye_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)  # 人眼纵横比(eye aspect ratio)
    return ear


def eye_detection(threshold, sustain):
    # 人眼纵横比参数
    EAR_THRESHOLD = threshold  # 阈值
    SUSTAIN_FREAMS = sustain  # 当检测到人眼超过50帧还在闭眼状态，说明人正在瞌睡

    # 检测帧次数
    COUNTER = 0

    # 加载人脸68点数据模型
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('../shape_predictor_68_face_landmarks.dat')

    # 获取人眼的坐标
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

    # 从摄像头中来获取人脸
    vs = VideoStream(src=0).start()
    time.sleep(1.0)

    # 从视频中获取视频帧来进行检测
    while True:

        # 从视频中获取图片来检测
        frame = vs.read()
        frame = imutils.resize(frame, width=700)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        for rect in rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # 提取人眼坐标，来计算人眼纵横比
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_ratio(leftEye)
            rightEAR = eye_ratio(rightEye)

            # 平均左右眼的纵横比
            ear = (leftEAR + rightEAR) / 2.0

            # 显示左右眼
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            # 计算ear是否小于阈值
            if ear < EAR_THRESHOLD:
                COUNTER += 1
                if COUNTER >= SUSTAIN_FREAMS:
                    # 人瞌睡是要处理的函数
                    cv2.putText(frame, "You Died", (230, 250),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 7)

                # 闭眼时，提醒
                cv2.putText(frame, "WARNING", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            else:
                COUNTER = 0  # 当检测不到闭眼
                cv2.putText(frame, 'EAR: {:.2f}'.format(ear), (580, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
    vs.stop()


if __name__ == '__main__':
    eye_detection(0.3, 50)








