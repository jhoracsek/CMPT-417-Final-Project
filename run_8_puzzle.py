import random
import copy
import numpy as np
import time
import math
from queue import PriorityQueue

'''
Puzzle(N) creates a NxN puzzle and asks the user for the initial state and the goal state. 
In the case of an 8-puzzle, we have N=3 and use the solved 8-puzzle as the goal state.

Input Example:

Initial state
1 5 2
4 8 3
_ 7 6

Goal state
1 2 3
4 5 6
7 8 _

There are two algorithms to solve the puzzle, A*(astar method) and IDA*(id_astar method). 
In both of these algorithms, we can use the tiles-out-of-order or the Manhattan distance as the heuristic. 

When the user inputs the initial state, the program checks whether it is solvable or not. 
If it is, it finds a solution and prints all the expanded nodes in the order of expansion. 
'''

import math
import time

class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        # Find the blank tile and generate child nodes by moving it in the four directions {up,down,left,right}
        x, y = self.find(self.data, '_')
        actions = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]

        children = []
        for i in actions:
            child = self.move(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def move(self, puzzle, x1, y1, x2, y2):
        # Move the blank space and check if it is still inside the map
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puzzle = self.copy(puzzle)
            temp = temp_puzzle[x2][y2]
            temp_puzzle[x2][y2] = temp_puzzle[x1][y1]
            temp_puzzle[x1][y1] = temp
            return temp_puzzle
        else:
            return None

    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puzzle, x):
        # Find the position of the blank space
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puzzle[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        # Initialize an n_puzzle in standard configuration
        self.n = size
        self.open = []
        self.closed = []

    def count_inversions(self, puzzle):
        obj = RepeatedCode(self.n)
        return obj.count_inversions(puzzle)

    def check_solvability(self, puzzle):
        obj = RepeatedCode(self.n)
        return obj.check_solvability(puzzle)

    def get_puzzle(self):
        # Get user input for the puzzle
        puzzle = []
        while True:
            for i in range(0, self.n):
                temp = input().split(" ")
                puzzle.append(temp)
            if self.check_solvability(puzzle):
                return puzzle
            else:
                print("Not solvable")
                print("Enter the start state matrix \n")

    def f(self, start, goal, manhattan):
        # Returns the f-value
        if manhattan:
            return self.manhattan_heuristic(start.data, goal) + start.level
        else:
            return self.tiles_heuristic(start.data, goal) + start.level

    def tiles_heuristic(self, start, goal):
        # Heuristic function - Tiles out of order
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def manhattan_heuristic(self, start, goal):
        # Heuristic function - Manhattan Distance
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != '_':
                    for k in range(0, self.n):
                        for l in range(0, self.n):
                            if start[i][j] == goal[k][l] and (i != k or j != l):
                                temp = temp + abs(k - i) + abs(l - j)
        return temp

    def astar(self, manhattan):
        num_gen = 0
        num_opn = 0
        print("Enter the start state matrix \n")
        start = self.get_puzzle()
        print("Enter the goal state matrix \n")
        goal = self.get_puzzle()

        start = Node(start, 0, 0)
        start.fval = self.f(start, goal, manhattan)
        bound = start.fval

        self.open.append(start)

        print("\n\n")

        while True:
            num_opn += 1
            cur = self.open[0]
            print("\n")

            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")

            if self.tiles_heuristic(cur.data, goal) == 0:
                print("\n")
                print("number of nodes generated ", num_gen)
                print("number of nodes opened ", num_opn)
                break

            for i in cur.generate_child():

                # Check if it is a duplicate
                if i.data not in self.closed:
                    num_gen += 1
                    i.fval = self.f(i, goal, manhattan)
                    self.open.append(i)

            self.closed.append(cur.data)
            del self.open[0]

            # Sort the open list based on f value
            self.open.sort(key=lambda x: x.fval, reverse=False)

    def id_astar(self, manhattan):
        num_gen = 0
        num_opn = 0
        print("Enter the start state matrix \n")
        start = self.get_puzzle()
        print("Enter the goal state matrix \n")
        goal = self.get_puzzle()

        start = Node(start, 0, 0)
        start.fval = self.f(start, goal, manhattan)
        bound = start.fval

        self.open.append(start)

        print("\n\n")

        while True:
            self.open.append(start)
            self.closed = []
            mincost = math.inf
            while self.open:
                num_opn += 1
                cur = self.open[0]
                if cur.fval > bound:
                    mincost = min(mincost, cur.fval)
                    del self.open[0]
                    continue

                print("\n")

                for i in cur.data:
                    for j in i:
                        print(j, end=" ")
                    print("")

                if self.tiles_heuristic(cur.data, goal) == 0:
                    print("\n")
                    print("number of nodes generated ", num_gen)
                    print("number of nodes expanded ", num_opn)
                    break

                for i in cur.generate_child():
                    # Check if it is a duplicate
                    if i.data not in self.closed:
                        num_gen += 1
                        i.fval = self.f(i, goal, manhattan)
                        self.open.append(i)

                self.closed.append(cur.data)
                del self.open[0]

                # Sort the open list based on f value
                self.open.sort(key=lambda x: x.fval, reverse=False)
            if mincost == math.inf:
                break
            bound = mincost


if __name__ == '__main__':
    puz = Puzzle(3)
    manhattan = False
    start = time.process_time()
    puz.astar(manhattan)
    print(time.process_time() - start)
