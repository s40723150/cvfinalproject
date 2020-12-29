import cv2
import numpy as np

background = np.ones((600, 300, 3), np.uint8) * 255

# background = cv2.cvtColor(background,cv2.COLOR_GRAY2RGB)
clone = np.copy(background)


def ball(event, x, y, flags, param):
    global clone
    if event == cv2.EVENT_MOUSEMOVE:
        clone = np.copy(background)
        # cv2.rectangle(clone, points[0], (x, y), (0, 255, 0), 2)
        cv2.circle(clone, (x, y), 10, (60, 180, 255), -1)
        # print(x, y)


cv2.circle(clone, (150, 300), 10, (60, 180, 255), -1)

while True:
    key = cv2.waitKey(5) & 0XFF
    cv2.setMouseCallback("airhockey", ball)

    cv2.imshow("airhockey", clone)
    if key == 27:
        break