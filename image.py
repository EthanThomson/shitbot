# Python code for Multiple Color Detection

import cv2
import imutils
import numpy as np
import time

start = time.perf_counter()
frame = cv2.imread('r1.jpg')
clear = cv2.imread('r2.jpg')
frame = frame[18:1118,28:828]
clear = frame[21:1121, 16:816]
image3 = cv2.absdiff(clear, frame)
cv2.imwrite(r"C:\Users\elet1\PycharmProjects\Shitbot\b.png", image3)
# frame = frame[40:900, 45: 1250]

# 1118 x 828 r2
# 1121 x 816 r1

black_coords = []
yellow_coords = []
blue_coords = []
red_coords = []
for x in range(1):
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # translate image to high saturated volume
    black = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # change colour to grey scale

    # black
    black = 255 - black  # invert so black = white and vice versa
    ret, thresh = cv2.threshold(black, 255 - 40, 255, cv2.THRESH_BINARY_INV)
    cnts1 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)
    for contour in cnts1:
        area = cv2.contourArea(contour)
        if 20 < area < 200:
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
            cv2.putText(imageFrame, "Black", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
            black_mx = x + w / 2
            black_my = y + h / 2
            black_list = (black_mx, black_my)
            black_coords.append(black_list)

    # Yellow
    y_lower = np.array([21, 50, 120], np.uint8)
    y_upper = np.array([40, 255, 255], np.uint8)
    y_mask = cv2.inRange(HSV, y_lower, y_upper)
    cnts2 = cv2.findContours(y_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)
    for contour in cnts2:
        area = cv2.contourArea(contour)
        if (25 < area < 200):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
            cv2.putText(imageFrame, "Yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
            yellow_mx = x + w / 2
            yellow_my = y + h / 2
            yellow_list = (yellow_mx, yellow_my)
            yellow_coords.append(yellow_list)

    # Red
    r_lower = np.array([0, 30, 0], np.uint8)
    r_upper = np.array([20, 200, 255], np.uint8)
    r_mask = cv2.inRange(HSV, r_lower, r_upper)
    cnts3 = cv2.findContours(r_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)
    for contour in cnts3:
        area = cv2.contourArea(contour)
        if 20 < area < 200:
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
            cv2.putText(imageFrame, "red", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
            red_mx = x + w / 2
            red_my = y + h / 2
            red_list = (red_mx, red_my)
            red_coords.append(red_list)


    # Blue
    bu_lower = np.array([90, 60, 50], np.uint8)
    bu_upper = np.array([125, 255, 255], np.uint8)
    bu_mask = cv2.inRange(HSV, bu_lower, bu_upper)
    cnts4 = cv2.findContours(bu_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts4 = imutils.grab_contours(cnts4)
    for contour in cnts4:
        area = cv2.contourArea(contour)
        if 20 < area < 200:
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
            cv2.putText(imageFrame, "Blue", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
            blue_mx = x + w / 2
            blue_my = y + h / 2
            blue_list = (blue_mx, blue_my)
            blue_coords.append(blue_list)
cv2.imwrite(r"C:\Users\elet1\PycharmProjects\Shitbot\a.png", imageFrame)
print(blue_coords)
print(black_coords)
print(red_coords)
print(yellow_coords)

end = time.perf_counter()
print(end - start)