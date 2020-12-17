import cv2
import numpy as np


def key():
    key = cv2.waitKey(10) & 0XFF
    return key


def vidshow(show, keys):
    while show:
        show, frame = cap.read()
        cv2.imshow("Video", frame)
        if key() == keys:
            break


def vidclose(show, keys):
    while show:
        if key() == keys:
            cv2.destroyAllWindows()
            break


cap = cv2.VideoCapture(0)
esc = 27
Q = ord("q")
show, frame = cap.read()
'''
f2 = np.array(frame)

cv2.imshow("hight", f2)

clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))
claheImg = clahe.apply(frame)
Cimg = cv2.cvtColor(claheImg,cv2.COLOR_GRAY2RGB)
'''
# cv2.imshow("Cimg", Cimg)
# cv2.waitKey(0)
bbox = cv2.selectROI("img", frame, False, True)
print(bbox)
vidclose(show, Q)
vidshow(show, esc)
