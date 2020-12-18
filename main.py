import cv2
import numpy as np
cap = cv2.VideoCapture(0)
esc = 27
C = ord("c")
Q = ord("q")
R = ord("r")
show, frame = cap.read()

clone = frame.copy()
points = []
cropping = False
def Area(event,x,y,flags,param):
    global points, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        points = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))
        cropping = False
        cv2.rectangle(frame, points[0], points[1], (0, 255, 0), 2)
while show:
    key = cv2.waitKey(5) & 0XFF
    cv2.setMouseCallback("Video",Area)
    cv2.imshow("Video", frame)
    if key == R:
        points = []
        frame = clone.copy()
        cv2.imshow("Video", frame)
        cv2.destroyWindow("ROI")
        print("pressed R")
    elif key == C:
        print("pressed C")
        if len(points) == 2:
            roi = clone[points[0][1]:points[1][1], points[0][0]:points[1][0]]
            print(roi.shape)
            cv2.imshow("ROI", roi)
    elif key == esc:
        break
