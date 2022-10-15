
import numpy as np
import time
import math


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

# ([983.5, 338.0, 712.0, 515.0], [504.0, 500.5, 307.0, 259.0])
# ([626.0, 550.0, 1056.5, 271.0], [652.0, 572.0, 290.0, 171.0])
# ([558.0, 664.5, 351.0, 355.5, 934.5], [446.0, 412.0, 394.0, 392.5, 315.5])
# ([264.0, 254.0, 581.5, 411.5], [634.0, 597.0, 517.5, 395.5])

def populategrid(y, x, maze):
    x = int(x/10)
    y = int(y/10)
    maze[x, y] = 1
    return maze




def main():
    blues = ([983.5, 504], [338, 500.5], [712, 307], [515, 259])



    maze1 = np.zeros((80, 121))
    x = 0
    for x in range(len(blues)):
        xin = blues[x][0]
        yin = blues[x][1]
        maze1 = populategrid(xin, yin, maze1)


    start = (0, 0)
    end = (79, 0)


    k = time.perf_counter()
    path = astar(maze1, start, end)
    kk = time.perf_counter()
    print(kk - k)
    print(path)

    print(gil(path))

def gil(inp):
    delx = inp[-1][0] - inp[0][0]
    dely = inp[-1][1] - inp[0][1]
    if(delx == 0):
        return 0
    if(dely == 0):
        return 90

    return(math.degrees(math.atan(dely/delx)))

main()