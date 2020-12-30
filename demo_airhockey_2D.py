import cv2
import numpy as np

background = np.ones((600, 300, 3), np.uint8) * 255

# background = cv2.cvtColor(background,cv2.COLOR_GRAY2RGB)
update = np.copy(background)
def read(self, image=update):
    pass

def ball(event, x, y, flags, param):
    global update
    if event == cv2.EVENT_MOUSEMOVE:
        update = np.copy(background)
        # cv2.rectangle(update, points[0], (x, y), (0, 255, 0), 2)
        cv2.circle(update, (x, y), 10, (60, 180, 255), -1)
        # print(x, y)


cv2.circle(update, (150, 300), 10, (60, 180, 255), -1)
while True:
    key = cv2.waitKey(5) & 0XFF
    cv2.setMouseCallback("demo_airhockey", ball)

    cv2.imshow("demo_airhockey", update)
    if key == 27:
        break