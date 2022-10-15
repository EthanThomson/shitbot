# Python code for Multiple Color Detection

import numpy as np
import cv2
import imutils
import math
import time

def process(cas):
    frame = cv2.imread('all_colours_0.png')
    frame = frame[40:900, 45: 1250]
    blue_coords = []
    black_coords = []
    red_coords = []
    yellow_coords = []

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
            # cv2.circle(imageFrame, (int(black_mx), int(black_my)), 1, (255, 255, 255), 3)
            # cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)

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
            yellow_list = (yellow_mx, yellow_my)
            yellow_coords.append(yellow_list)
            # cv2.circle(imageFrame, (int(yellow_mx), int(yellow_my)), 1, (255, 255, 255), 3)
            # cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)

    # Red
    r_lower = np.array([0, 5, 0], np.uint8)
    r_upper = np.array([20, 200, 255], np.uint8)
    r_mask = cv2.inRange(HSV, r_lower, r_upper)
    cnts3 = cv2.findContours(r_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)
    for contour in cnts3:
        area = cv2.contourArea(contour)
        if (area < 200):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
            cv2.putText(imageFrame, "Red", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
            red_mx = x + w / 2
            red_my = y + h / 2
            red_list = (red_mx, red_my)
            red_coords.append(red_list)
            # cv2.circle(imageFrame, (int(red_mx), int(red_my)), 1, (255, 255, 255), 3)
            # cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)

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
            blue_list = (blue_mx, blue_my)
            blue_coords.append(blue_list)
            # cv2.circle(imageFrame, (int(blue_mx), int(blue_my)), 1, (255, 255, 255), 3)
            # cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)

    return (yellow_coords, blue_coords, red_coords, black_coords)

# class Node():
#     """A node class for A* Pathfinding"""
#
#     def __init__(self, parent=None, position=None):
#         self.parent = parent
#         self.position = position
#
#         self.g = 0
#         self.h = 0
#         self.f = 0
#
#     def __eq__(self, other):
#         return self.position == other.position
#
# def astar(maze, start, end):
#     """Returns a list of tuples as a path from the given start to the given end in the given maze"""
#
#     # Create start and end node
#     start_node = Node(None, start)
#     start_node.g = start_node.h = start_node.f = 0
#     end_node = Node(None, end)
#     end_node.g = end_node.h = end_node.f = 0
#
#     # Initialize both open and closed list
#     open_list = []
#     closed_list = []
#
#     # Add the start node
#     open_list.append(start_node)
#
#     # Loop until you find the end
#     while len(open_list) > 0:
#
#         # Get the current node
#         current_node = open_list[0]
#
#         current_index = 0
#         for index, item in enumerate(open_list):
#             if item.f < current_node.f:
#                 current_node = item
#                 current_index = index
#
#         # Pop current off open list, add to closed list
#         open_list.pop(current_index)
#         closed_list.append(current_node)
#
#         # Found the goal
#         if current_node == end_node:
#             path = []
#             current = current_node
#             while current is not None:
#                 path.append(current.position)
#                 current = current.parent
#
#             return path[::-1] # Return reversed path
#
#         # Generate children
#         children = []
#         for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
#
#             # Get node position
#             node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
#
#             # Make sure within range
#             if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
#                 continue
#
#             # Make sure walkable terrain
#             if maze[node_position[0]][node_position[1]] != 0:
#                 continue
#
#             # Create new node
#             new_node = Node(current_node, node_position)
#
#             # Append
#             children.append(new_node)
#
#         # Loop through children
#         for child in children:
#
#             # Child is on the closed list
#             # Child is on the closed list
#             is_closed = False
#             for closed_child in closed_list:
#                 if child == closed_child:
#                     is_closed = True
#             if is_closed: continue
#
#             # Create the f, g, and h values
#             child.g = current_node.g + 1
#             child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
#             child.f = child.g + child.h
#
#             # Child is already in the open list
#             for open_node in open_list:
#                 if child == open_node and child.g > open_node.g:
#                     continue
#
#             # Add the child to the open list
#             open_list.append(child)

def obs(yela, blu, re, blak, all, maze, start):
    returns = []
    dist = []
    coord = []
    # if(yela == 1):
    #     obst(all[0], maze)
    # if(blu == 1):
    #     obst(all[1], maze)
    # if(re == 1):
    #     obst(all[2], maze)
    # if(blak == 1):
    #     obst(all[3], maze)
    if (yela == 0):
        returns.append(goalfinder(all[0], maze))
        dist.append(distance(all[0], start))
        coord.append(coords(all[0]))
    if (blu == 0):
        returns.append(goalfinder(all[1], maze))
        dist.append(distance(all[1], start))
        coord.append(coords(all[1]))
    if (re == 0):
        returns.append(goalfinder(all[2], maze))
        dist.append(distance(all[2], start))
        coord.append(coords(all[2]))
    if (blak == 0):
        returns.append(goalfinder(all[3], maze))
        dist.append(distance(all[3], start))
        coord.append(coords(all[3]))

    dist = np.array(dist, dtype=object)
    print(dist)
    print(len(dist))
    print(len(dist[0]))
    coord = np.array(coord, dtype=object)
    print(len(coord))
    point = closest(dist, coord)
    return (maze)


def closest(dist, coord):
    position = []
    mind = []
    k = []
    for x in range(len(dist)):
        mindist = min(dist[x])
        for y in range(len(dist[x])):
            print(dist[x][y])
            check = (mindist == dist[x][y])
            if check == 1:
                position.append(y)
                mind.append(mindist)
                break
    k.append(coord[0][position[0]])
    k.append(coord[1][position[1]])
    for x in range(len(mind))
        fmind = min(mindist)

    print(mind)
    return

# def obst(input, maze):
#     for x in range(len(input)):
#         xin = input[x][0]
#         yin = input[x][1]
#         xout = int(xin/10)
#         yout = int(yin/10)
#         maze[xout-3:xout+3, yout-3:yout+3] = 1
#     return maze

def goalfinder(input, maze):
    goal = []
    for x in range(len(input)):
        xin = input[x][0]
        yin = input[x][1]
        xout = int(xin / 10) #translate coords to
        yout = int(yin / 10)
        goalhoe = (xout, yout)
        goal.append(goalhoe)
        maze[xout - 3:xout + 3, yout - 3:yout + 3] = 0
    return goal

def distance(input, start):
    dist = []
    for x in range(len(input)):
        xin = input[x][0]
        yin = input[x][1]
        coords = (xin, yin)
        distance = math.dist(start, coords)
        dist.append(distance)
    return dist

def coords(input):
    coord = []
    for x in range(len(input)):
        xin = input[x][0]
        yin = input[x][1]
        coords = (xin, yin)
        coord.append(coords)
    return coord


# def angle(xy, ):
#     turns = [0]
#     target = None
#     current = None
#     i = 0
#     z = 0
#     r = 0
#     g = 0
#     # previous = []
#     for x in range(len(input)):
#         if(z + i >= len(input)):
#             r = r + 1
#         delx = input[x][0] - input[(z + i) - r][0]
#         dely = input[x][1] - input[(z + i) - r][1]
#         # previous = current
#         if((delx == 0) & (dely < 0)):
#             current = 180
#         elif (delx == 0):
#             current = 0
#         elif ((dely == 0) & (delx < 0)):
#             current = -90
#         elif (dely == 0):
#             current = 90
#         else:
#             current = math.degrees(math.atan(dely / delx))
#             if ((delx < 0) & (dely < 0)):
#                 current = current * -1 - 90
#             elif((dely < 0) & (delx > 0)):
#                 current = current * -1 + 90
#         if (x == 0):
#             target = current
#         elif(current == target):
#             i = i + 1
#         else:
#             #turns.append(input[z:i])
#             # soap = (current, distance)
#             turns.append(current)
#             i = 0
#             z = int(i) + int(x)
#             target = current
#     return turns

# def distrav(path, start)
#     previous = start
#     current - []
#     for x in range(len(input)):
#         current = path[x]
#         distance = math.dist()
#         previous = current - previous
# def mindist(dist, coord):

def main():
    stime = time.perf_counter()
    start = (0, 0)
    all = process(0)
    maze = np.zeros((80, 121))
    # dist = distance(0,0,1,0,all, start)
    calc = obs(0,1,1,0,all,maze, start) #yellow, blue, red, black, 1 = obstacle, 0 = goal
    # distrav = distrav(path, start)
    # maze = calc[0]
    # beechz = calc[1]



    # yellows = all[0]
    # blues = all[1]
    # reds = all[2]
    # blacks = all[3]
    # print("yellows:  ", yellows)
    # print("blues:  ", blues)
    # print("reds:  ", reds)
    # print("blacks:  ", blacks)

    # end = (5, 40)
    # # path = astar(maze1, start, end)
    # print("path")
    # # print(path)
    # print("goals")
    # # print(beechz)
    # print("angles")
    # # print(angle(path))
    # print("distance")
    # print(distance)
    # print("coordinates")
    # print(check)
    etime =  time.perf_counter()
    print(etime-stime)
main()