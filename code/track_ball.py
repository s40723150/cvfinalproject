import cv2, imutils, time
import numpy as np
from collections import deque

distance = deque(maxlen=2)
def bg():
    background = np.ones((600, 300, 3), np.uint8) * 255
    background = cv2.rectangle(background, (0, 0), (299, 300), (0, 0, 0), 3)
    background = cv2.rectangle(background, (0, 300), (299, 599), (0, 0, 0), 3)
    background = cv2.rectangle(background, (100, 0), (200, 40), (0, 0, 0), 5)
    background = cv2.rectangle(background, (100, 560), (200, 600), (0, 0, 0), 5)
    background = cv2.circle(background, (150, 300), 50, (0, 0, 0), 3)
    return background
def ball(event, x, y, flags, param):
    global update, ball_p
    if event == cv2.EVENT_MOUSEMOVE:
        update = np.copy(background)
        cv2.circle(update, (x, y), 10, (60, 180, 255), -1)
def Velocity(center , distance = distance ):
    end_t = time.time()
    dt = end_t - start_t
    distance.append(center)
    x0, y0 = distance[0][0]/2, distance[0][1]/2
    x1, y1 = distance[-1][0]/2, distance[-1][1]/2
    dx, dy= abs(x0 - x1), abs(y0 - y1)
    ds = (dx ** 2 + dy ** 2) ** 0.5
    velocity = ds / dt
    v_str = str(format(velocity, '.1f') + "cm/sec")

    cv2.putText(info, "velocity", (10, 23), cv2.FONT_HERSHEY_SIMPLEX,  0.6, (0,255,0), 1)
    cv2.putText(info, v_str, (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0,255,0), 1)
def position(center):
    color = (205, 205, 80)
    cv2.putText(info, "position", (120, 23), cv2.FONT_HERSHEY_SIMPLEX,  0.6, color, 1)
    cv2.putText(info, "(cm)", (195, 23), cv2.FONT_HERSHEY_SIMPLEX,  0.4, color, 1)
    px_str = "x:"+ str(int(center[0]/2))
    py_str = "y:"+ str(int(center[1]/2))
    cv2.putText(info, px_str, (120, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1)
    cv2.putText(info, py_str, (180, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1)
if __name__ == "__main__":
    background = bg()
    information = np.ones((60, 240, 3), np.uint8) * 255
    information = cv2.rectangle(information, (0, 0), (240, 59), (0, 0, 0), 3)
    update = np.copy(background)
    ball_p = []
    cv2.circle(update, (150, 300), 10, (60, 180, 255), -1) #起始出現在中間
    while True:
        start_t = time.time()
        key = cv2.waitKey(5) & 0XFF
        cv2.setMouseCallback("demo_airhockey", ball)
        mask = cv2.inRange(update, (60, 180, 255), (70, 190, 255))
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        tracker = np.copy(update)
        info = np.copy(information)
        cv2.imshow("demo_airhockey", tracker)
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            center2 = (float(M["m10"] / M["m00"]), float(M["m01"] / M["m00"]))
            if radius >= 10:
                cv2.circle(tracker, center, 15, (0, 255, 0), 3)
                cv2.putText(tracker, "ball", ((center[0]-15),(center[1]-20)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        Velocity(center2)
        position(center)
        tracker = cv2.resize(tracker, (240, 480))
        demo = np.vstack([info, tracker])
        cv2.imshow("track_ball", demo)

        if key == 27:
            cv2.destroyAllWindows()
            break