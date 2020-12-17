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
show,frame = cap.read()
# cv2.imshow("frame", frame)

print("succseful")
cv2.waitKey(1)
bbox = cv2.selectROI("img",frame, False, True)
x1 = bbox[0]
x2 = bbox[2]
y1 = bbox[1]
y2 = bbox[3]
print(x1, y1, "\n", x2, y2)
imgCropped = frame[y1:y2, x1:x2]
cv2.imshow("imgC", imgCropped)
cv2.imwrite("./001.png", imgCropped, [cv2.IMWRITE_PNG_COMPRESSION, 0])
cv2.waitKey(0)
vidclose(show, Q)
print("will show video")
while show:
    show, frame = cap.read()
    cv2.imshow("Video", frame)
    if key() == esc:
        break
#　vidshow(show, esc)