 # Python code for Multiple Color Detection

import cv2
import imutils
import numpy as np

frame = cv2.imread('all_colours_0.png')
HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # translate image to high saturated volume
black = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # change colour to grey scale
frame = frame[40:900, 45: 1250]

# g_lower = np.array([60, 40, 0], np.uint8)
# g_upper = np.array([89, 255, 255], np.uint8)
# g_mask = cv2.inRange(HSV, g_lower, g_upper)
# cv2.imshow("green", g_mask)
# cnts5 = cv2.findContours(g_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnts5 = imutils.grab_contours(cnts5)
# for contour in cnts5:
#     area = cv2.contourArea(contour)
#     if (10000 < area):
#         x, y, w, h = cv2.boundingRect(contour)
#
#         cv2.circle(frame, (int(x+w), int(h)), 1, (255, 255, 255), 10)
#         cv2.circle(frame, (int(w+10), int(y)), 1, (255, 255, 255), 10)
#         cv2.circle(frame, (int(x), int(y+10)), 1, (255, 255, 255), 10)
#         cv2.circle(frame, (int(x), int(y+h)), 1, (255, 255, 255), 10)
#         cv2.imshow("Multiple Color Detection in Real-TIme", frame)
black_yl = []
black_xl = []
yellow_yl = []
yellow_xl = []
blue_yl = []
blue_xl = []
red_xl = []
red_yl = []

while (1):
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

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
            black_yl.append(black_my)
            black_xl.append(black_mx)
            black_xl = list(dict.fromkeys(black_xl))
            black_yl = list(dict.fromkeys(black_yl))
            black_coords = (black_xl, black_yl)
            cv2.circle(imageFrame, (int(black_mx), int(black_my)), 1, (255, 255, 255), 3)
            cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)

    # Yellow
    y_lower = np.array([21, 100, 120], np.uint8)
    y_upper = np.array([40, 255, 255], np.uint8)
    y_mask = cv2.inRange(HSV, y_lower, y_upper)
    cnts2 = cv2.findContours(y_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)
    for contour in cnts2:
        area = cv2.contourArea(contour)
        if (20 < area < 200):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
            cv2.putText(imageFrame, "Yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
            yellow_mx = x + w / 2
            yellow_my = y + h / 2
            yellow_yl.append(yellow_my)
            yellow_xl.append(yellow_mx)
            yellow_xl = list(dict.fromkeys(yellow_xl))
            yellow_yl = list(dict.fromkeys(yellow_yl))
            yellow_coords = (yellow_xl, yellow_yl)
            cv2.circle(imageFrame, (int(yellow_mx), int(yellow_my)), 1, (255, 255, 255), 3)
            cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)

    # Red
    r_lower = np.array([0, 5, 0], np.uint8)
    r_upper = np.array([20, 200, 255], np.uint8)
    r_mask = cv2.inRange(HSV, r_lower, r_upper)
    cnts3 = cv2.findContours(r_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)
    for contour in cnts3:
        area = cv2.contourArea(contour)
        if (25 < area < 200):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
            cv2.putText(imageFrame, "Red", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
            red_mx = x + w / 2
            red_my = y + h / 2
            red_yl.append(red_my)
            red_xl.append(red_mx)
            red_xl = list(dict.fromkeys(red_xl))
            red_yl = list(dict.fromkeys(red_yl))
            red_coords = (red_xl, red_yl)
            cv2.circle(imageFrame, (int(red_mx), int(red_my)), 1, (255, 255, 255), 3)
            cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)

    # Blue
    bu_lower = np.array([90, 60, 0], np.uint8)
    bu_upper = np.array([125, 255, 255], np.uint8)
    bu_mask = cv2.inRange(HSV, bu_lower, bu_upper)
    cnts4 = cv2.findContours(bu_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts4 = imutils.grab_contours(cnts4)
    for contour in cnts4:
        area = cv2.contourArea(contour)
        if (20 < area < 200):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
            cv2.putText(imageFrame, "Blue", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
            blue_mx = x + w / 2
            blue_my = y + h / 2
            blue_yl.append(blue_my)
            blue_xl.append(blue_mx)
            blue_xl = list(dict.fromkeys(blue_xl))
            blue_yl = list(dict.fromkeys(blue_yl))
            blue_coords = (blue_xl, blue_yl)
            cv2.circle(imageFrame, (int(blue_mx), int(blue_my)), 1, (255, 255, 255), 3)
            cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)