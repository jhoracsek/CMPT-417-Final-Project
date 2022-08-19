from queue import PriorityQueue
import copy
import math
from time import perf_counter

class node_astar:
    # State is represented as an instance of n_puzzle
    def __init__(self, state, parent, h_func, cost=1):
        self.state = state
        self.h_func = h_func
        self.h_val = h_func(state)
        self.g_val = 0
        self.parent = parent
        if parent != None:
            self.g_val = parent.g_val + cost
        self.f_val = self.g_val + self.h_val
        return

    def __gt__(self, other):
        # This is where you tiebreak by larger g val
        if self.f_val == other.f_val:
            return self.g_val < other.g_val
        return self.f_val > other.f_val

    def __eq__(self, other):
        if other == None:
            return False
        this_puzzle = self.state.puzzle
        other_puzzle = other.state.puzzle
        for i in range(len(this_puzzle)):
            for j in range(len(this_puzzle[i])):
                if this_puzzle[i][j] != other_puzzle[i][j]:
                    return False
        return True

    def is_goal(self):
        this_puzzle = self.state.puzzle
        n = self.state.n
        for i in range(len(this_puzzle)):
            for j in range(len(this_puzzle[i])):
                if this_puzzle[i][j] != 0 and this_puzzle[i][j] != (i * n + (j + 1)):
                    return False
        return True

    def is_equal(self, other_node):
        this_puzzle = self.state.puzzle
        other_puzzle = other_node.state.puzzle
        for i in range(len(this_puzzle)):
            for j in range(len(this_puzzle[i])):
                if this_puzzle[i][j] != other_puzzle[i][j]:
                    return False
        return True

    # Returns a list of children
    # i.e., expands the node
    def generate_children(self):
        # children=[]
        children = PriorityQueue()
        for i in self.state.get_actions():
            child_state = copy.deepcopy(self.state)
            child_state.perform_action(i)
            # children.append(node_astar(child_state, self, self.h_func, 1))
            child_node = node_astar(child_state, self, self.h_func, 1)
            children.put(child_node)

        return children

    def generate_children_arr(self):
        children = []
        for i in self.state.get_actions():
            child_state = copy.deepcopy(self.state)
            child_state.perform_action(i)
            children.append(node_astar(child_state, self, self.h_func, 1))

        return children


def a_star(start_state, h_func):
    root = node_astar(start_state, None, h_func, 0)
    open_list = PriorityQueue()
    open_list.put(root)

    # To print every 500th node
    count = 0

    while open_list.empty() == False:

        current = open_list.get()

        if current.is_goal():
            print("Found Solution")
            print('Node num:', count)
            print('Node f_val:', current.f_val)
            print('Node g_val:', current.g_val)
            print('Node h_val:', current.h_val)
            cur = current
            while cur.parent != None:
                cur.state.display()
                cur = cur.parent
                print()
            cur.state.display()
            return True

        if count % 500 == 0:
            print('Node num:', count)
            print('Node f_val:', current.f_val)
            print('Node g_val:', current.g_val)
            print('Node h_val:', current.h_val)
            print()

        for child in current.generate_children_arr():
            open_list.put(child)

        count += 1


def a_star_dd(start_state, h_func):
    root = node_astar(start_state, None, h_func, 0)
    open_list = PriorityQueue()
    open_list.put(root)

    closed_list = []
    for x in range(16):
        arr1 = []
        for y in range(16):
            arr2 = []
            for z in range(16):
                arr3 = []
                for w in range(16):
                    arr4 = []
                    for a in range(16):
                        arr5 = []
                        arr4.append(arr5)
                    arr3.append(arr4)
                arr2.append(arr3)
            arr1.append(arr2)
        closed_list.append(arr1)
    # To print every 500th node
    count = 0

    while open_list.empty() == False:

        current = open_list.get()

        puzzle = current.state.puzzle

        if current in closed_list[puzzle[0][0] - 1][puzzle[0][3] - 1][puzzle[1][1] - 1][puzzle[2][2] - 1][
            puzzle[3][3] - 1]:
            continue

        if current.is_goal():
            print("Found Solution")
            print('Node num:', count)
            print('Node f_val:', current.f_val)
            print('Node g_val:', current.g_val)
            print('Node h_val:', current.h_val)
            cur = current
            while cur.parent != None:
                cur.state.display()
                cur = cur.parent
                print()
            cur.state.display()
            return True

        if count % 500 == 0:
            print('Node num:', count)
            print('Node f_val:', current.f_val)
            print('Node g_val:', current.g_val)
            print('Node h_val:', current.h_val)
            print()

        for child in current.generate_children_arr():
            open_list.put(child)

        closed_list[puzzle[0][0] - 1][puzzle[0][3] - 1][puzzle[1][1] - 1][puzzle[2][2] - 1][puzzle[3][3] - 1].append(
            current)
        count += 1


def a_star_dd_extra_mem(start_state, h_func):
    root = node_astar(start_state, None, h_func, 0)
    open_list = PriorityQueue()
    open_list.put(root)

    closed_list = []
    for x in range(16):
        arr1 = []
        for y in range(16):
            arr2 = []
            for z in range(16):
                arr3 = []
                for w in range(16):
                    arr4 = []
                    for a in range(16):
                        arr5 = []
                        for b in range(16):
                            arr6 = []
                            arr5.append(arr6)
                        arr4.append(arr5)
                    arr3.append(arr4)
                arr2.append(arr3)
            arr1.append(arr2)
        closed_list.append(arr1)
    # To print every 500th node
    count = 0
    generated = 1

    start_time = perf_counter()
    while open_list.empty() == False:

        current = open_list.get()

        puzzle = current.state.puzzle

        if current in closed_list[puzzle[0][0] - 1][puzzle[0][3] - 1][puzzle[1][1] - 1][puzzle[2][2] - 1][puzzle[3][0] - 1][puzzle[3][3] - 1]:
            continue

        if current.is_goal():
            end_time = perf_counter()
            print("Found Solution")
            print('Nodes Generated:', generated)
            print('Nodes Expanded', count)
            print('Node f_val:', current.f_val)
            print('Node g_val:', current.g_val)
            print('Node h_val:', current.h_val)
            print('Elapsed time:', end_time - start_time)
            cur = current
            if False:
                while cur.parent != None:
                    cur.state.display()
                    cur = cur.parent
                    print()
                cur.state.display()
            return (end_time - start_time, generated, count, current.f_val)

        if count % 5000 == 0:
            print('Nodes Generated:', generated)
            print('Nodes Expanded', count)
            print('Node f_val:', current.f_val)
            print('Node g_val:', current.g_val)
            print('Node h_val:', current.h_val)
            print()

        for child in current.generate_children_arr():
            open_list.put(child)
            generated +=1
        closed_list[puzzle[0][0] - 1][puzzle[0][3] - 1][puzzle[1][1] - 1][puzzle[2][2] - 1][puzzle[3][0] - 1][puzzle[3][3] - 1].append(current)
        count += 1


def ida_star(start_state, h_func):
    root = node_astar(start_state, None, h_func, 0)
    # Cost threshold
    l = root.f_val

    # To print every 500th node
    count = 0
    while True:

        stack = []
        stack.append(root)
        minCost = math.inf
        while len(stack) > 0:

            current = stack.pop()

            if current.is_goal():
                print("Found Solution")
                print('Node num:', count)
                print('Node f_val:', current.f_val)
                print('Node g_val:', current.g_val)
                print('Node h_val:', current.h_val)
                print()

                cur = current

                while cur.parent != None:
                    cur.state.display()
                    cur = cur.parent
                    print()
                cur.state.display()
                return True

            # This is where we prune nodes greater than the cost threshold
            # so we also keep track of the minimum cost of all prined nodes
            if current.f_val > l:
                minCost = min(minCost, current.f_val)
                continue

            if count % 500 == 0:
                print('Node num:', count)
                print('Node f_val:', current.f_val)
                print('Node g_val:', current.g_val)
                print('Node h_val:', current.h_val)
                print()

            children = current.generate_children()
            while children.empty() == False:
                child = children.get()
                stack.append(child)
            # For old implementation of generate_children()
            # for child in current.generate_children():
            #    stack.append(child)

            count += 1
        # Update cost threshold
        print('Updated cost threshold', l)
        l = minCost

