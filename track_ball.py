import cv2
import numpy as np
import imutils

background = np.ones((600, 300, 3), np.uint8) * 255

update = np.copy(background)
ball_p = []
def ball(event, x, y, flags, param):
    global update, ball_p
    if event == cv2.EVENT_MOUSEMOVE:
        update = np.copy(background)
        # ball_p = [x, y]
        # cv2.rectangle(update, points[0], (x, y), (0, 255, 0), 2)
        cv2.circle(update, (x, y), 10, (60, 180, 255), -1)
cv2.circle(update, (150, 300), 10, (60, 180, 255), -1) #起始出現在中間
while True:
    key = cv2.waitKey(5) & 0XFF
    cv2.setMouseCallback("demo_airhockey", ball)
    #cv2.circle(update, (150, 300), 10, (60, 180, 255), -1)
    mask = cv2.inRange(update, (60, 180, 255), (70, 190, 255))
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    tracker = np.copy(update)
    cv2.imshow("demo_airhockey", update)
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius >= 10:
            cv2.circle(tracker, center, 15, (0, 255, 0), 3)
            cv2.imshow("demo_test", tracker)
            #print(center)

    if key == 27:
        break