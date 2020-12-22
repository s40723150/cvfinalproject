import cv2
import numpy as np
cap = cv2.VideoCapture(0)
esc, C ,Q , R, S = 27, ord("c"), ord("q"), ord("r"), ord("s")
show, frame = cap.read()
TARGET = "TARGET"
p_c = False
clone = np.copy(frame)
clone_frame = np.copy(frame)
points = []
mouse_pressed = False
def Area(event,x,y,flags,param):
    global points, mouse_pressed, clone
    if event == cv2.EVENT_LBUTTONDOWN:
        clone = np.copy(frame)
        mouse_pressed = True
        points = [(x, y)]
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            clone = np.copy(frame)
            cv2.rectangle(clone, points[0], (x, y), (0, 255, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        points.append((x, y))
        cv2.rectangle(clone, points[0], points[1], (0, 255, 0), 2)
def rank_dot(points):
    global x0, y0, x1, y1
    x0, y0 = points[0][0], points[0][1]
    x1, y1 = points[1][0], points[1][1]
    if x0 >= x1:
        x0, x1 = points[1][0], points[0][0]
        if y0 >= y1:
            y0, y1 = points[1][1], points[0][1]
    elif y0 >= y1:
        y0, y1 = points[1][1], points[0][1]

while show:
    key = cv2.waitKey(5) & 0XFF
    cv2.setMouseCallback("Video",Area)
    cv2.imshow("Video", clone)
    if key == R:
        points = []
        clone = np.copy(frame)
        cv2.imshow("Video", clone)
        cv2.destroyWindow(TARGET)
        p_c = False
        print("pressed R")
    elif key == C:
        p_c = True
        if len(points) == 2:
            rank_dot(points)
            target = clone_frame[y0:y1, x0:x1]
            print(target.shape)
            cv2.imshow(TARGET, target)
        else:
            print("Pleace select target.")
    elif key == S:
        if p_c is False:
            print("Pleace select target.")
        else:
            cv2.destroyWindow(TARGET)
            cv2.imshow("target",target)
            cv2.imwrite("target.png", target, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            print("Save the target as image is successful")
    elif key == esc:
        break

