import copy
import numpy as np
import time
from queue import PriorityQueue
from n_puzzle import n_puzzle

# This is the node class used specifically for constructing PDB tables
class node:
    # State is represented as an instance of n_puzzle
    def __init__(self, state, parent, cost=1):
        self.state = state
        # self.h_val=0
        self.g_val = 0
        # self.parent=parent
        if parent != None:
            self.g_val = parent.g_val + cost
        return

    def __gt__(self, other):
        return self.g_val > other.g_val

    # Returns indices of values in puzzle
    # in increasing order i.e., [2,3,6,7]
    def get_indices(self):
        non_blank = self.state.non_blank
        indices = []
        puzzle = self.state.puzzle
        for index in non_blank:
            count = 0
            for i in puzzle:
                for j in i:
                    if j == index:
                        indices.append(count)
                    count += 1
        return indices

    def get_blank_index(self):
        count = 0
        puzzle = self.state.puzzle
        for i in puzzle:
            for j in i:
                if j == 0:
                    return count
                count += 1
        return count

    def evaluate_cost(self, other_state):
        this_puzzle = self.state.puzzle
        other_puzzle = other_state.puzzle

        for i in range(len(this_puzzle)):
            for j in range(len(this_puzzle[i])):
                if this_puzzle[i][j] != other_puzzle[i][j]:
                    if this_puzzle[i][j] > 0 or other_puzzle[i][j] > 0:
                        return 1
        return 0

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
        children = []
        for i in self.state.get_actions():
            child_state = copy.deepcopy(self.state)
            child_state.perform_action(i)
            children.append(node(child_state, self, self.evaluate_cost(child_state)))
        return children


def PDB_UCS_3(root):
    open_list = PriorityQueue()
    open_list.put(root)

    # Method for three indices*
    PDB = np.zeros(4096) - 1
    PDB = np.reshape(PDB, (16, 16, 16))

    closed_list = np.zeros(65536)
    closed_list = np.reshape(closed_list, (16, 16, 16, 16))

    currentIteration = 0
    PDBs_set = 0
    while open_list.empty() == False:
        current = open_list.get()

        i = current.get_indices()
        b = current.get_blank_index()

        # Again, just assume that our pdb has four indices
        if PDB[i[0]][i[1]][i[2]] == -1:
            PDBs_set += 1
            PDB[i[0]][i[1]][i[2]] = current.g_val
        else:
            PDB[i[0]][i[1]][i[2]] = min(PDB[i[0]][i[1]][i[2]], current.g_val)

        if closed_list[i[0]][i[1]][i[2]][b] == 0:
            closed_list[i[0]][i[1]][i[2]][b] = 1
        else:
            continue

        for child in current.generate_children():
            open_list.put(child)

        if (currentIteration % 1000) == 0:
            print('Current Iteration:', currentIteration)
            print('Cost', current.g_val)
            print('PDBs_set:', PDBs_set)
            print('Indices', i)
            current.state.display()
        currentIteration += 1
    return PDB


def PDB_UCS(root):
    open_list = PriorityQueue()
    open_list.put(root)
    # For now, just assume that our pdb has four indices*
    PDB = np.zeros(65536) - 1
    PDB = np.reshape(PDB, (16, 16, 16, 16))

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
                        arr5 = 0
                        arr4.append(arr5)
                    arr3.append(arr4)
                arr2.append(arr3)
            arr1.append(arr2)
        closed_list.append(arr1)

    currentIteration = 0
    PDBs_set = 0
    while open_list.empty() == False:
        current = open_list.get()

        i = current.get_indices()
        b = current.get_blank_index()

        # Again, just assume that our pdb has four indices
        if PDB[i[0]][i[1]][i[2]][i[3]] == -1:
            PDBs_set += 1
            PDB[i[0]][i[1]][i[2]][i[3]] = current.g_val
        else:
            PDB[i[0]][i[1]][i[2]][i[3]] = min(PDB[i[0]][i[1]][i[2]][i[3]], current.g_val)

        if closed_list[i[0]][i[1]][i[2]][i[3]][b] == 0:
            closed_list[i[0]][i[1]][i[2]][i[3]][b] = 1
        else:
            continue

        for child in current.generate_children():
            open_list.put(child)

        if (currentIteration % 1000) == 0:
            print('Current Iteration:', currentIteration)
            print('Cost', current.g_val)
            print('PDBs_set:', PDBs_set)
            print('Indices', i)
            current.state.display()
        currentIteration += 1
    return PDB


def PDB_UCS_5(root):
    open_list = PriorityQueue()
    open_list.put(root)

    # Method for five indices*
    PDB = np.zeros(1048576) - 1
    PDB = np.reshape(PDB, (16, 16, 16, 16, 16))

    closed_list = np.zeros(16777216)
    closed_list = np.reshape(closed_list, (16, 16, 16, 16, 16, 16))

    currentIteration = 0
    PDBs_set = 0
    while open_list.empty() == False:
        current = open_list.get()

        i = current.get_indices()
        b = current.get_blank_index()

        if PDB[i[0]][i[1]][i[2]][i[3]][i[4]] == -1:
            PDBs_set += 1
            PDB[i[0]][i[1]][i[2]][i[3]][i[4]] = current.g_val
        else:
            PDB[i[0]][i[1]][i[2]][i[3]][i[4]] = min(PDB[i[0]][i[1]][i[2]][i[3]][i[4]], current.g_val)

        if closed_list[i[0]][i[1]][i[2]][i[3]][i[4]][b] == 0:
            closed_list[i[0]][i[1]][i[2]][i[3]][i[4]][b] = 1
        else:
            continue

        for child in current.generate_children():
            open_list.put(child)

        if (currentIteration % 1000) == 0:
            print('Current Iteration:', currentIteration)
            print('Cost', current.g_val)
            print('PDBs_set:', PDBs_set)
            print('Indices', i)
            current.state.display()
        currentIteration += 1
    return PDB


def PDB_UCS_6(root):
    open_list = PriorityQueue()
    open_list.put(root)

    # Method for 6 indices*
    PDB = np.zeros(16777216, dtype=np.int32) - 1
    PDB = np.reshape(PDB, (16, 16, 16, 16, 16, 16))

    closed_list = np.full((16, 16, 16, 16, 16, 16, 16), False)

    currentIteration = 0
    PDBs_set = 0
    while open_list.empty() == False:
        current = open_list.get()

        i = current.get_indices()
        b = current.get_blank_index()

        if PDB[i[0]][i[1]][i[2]][i[3]][i[4]][i[5]] == -1:
            PDBs_set += 1
            PDB[i[0]][i[1]][i[2]][i[3]][i[4]][i[5]] = current.g_val
        else:
            PDB[i[0]][i[1]][i[2]][i[3]][i[4]][i[5]] = min(PDB[i[0]][i[1]][i[2]][i[3]][i[4]][i[5]], current.g_val)

        if closed_list[i[0]][i[1]][i[2]][i[3]][i[4]][i[5]][b] == False:
            closed_list[i[0]][i[1]][i[2]][i[3]][i[4]][i[5]][b] = True
        else:
            del current
            continue

        for child in current.generate_children():
            open_list.put(child)

        if (currentIteration % 1000) == 0:
            print('Current Iteration:', currentIteration)
            print('Cost', current.g_val)
            print('PDBs_set:', PDBs_set)
            print('Indices', i)
            current.state.display()
        currentIteration += 1
        del current
    return PDB

#PDB Construction
#start = time.time()
#test_state = n_puzzle(4,[2,3,4])
#test_node = node(test_state, None, 1)
#PDB_3_1 = PDB_UCS_3(test_node)
#end = time.time()
#print(end-start)
#np.save('PDB_3_1.npy', PDB_3_1)

#PDB Construction
#start = time.time()
#test_state = n_puzzle(4,[2,3,4,7])
#test_node = node(test_state, None, 1)
#PDB_4_1 = PDB_UCS(test_node)
#end = time.time()
#print(end-start)
#np.save('PDB_4_1.npy', PDB_4_1)

#PDB Construction
start = time.time()
test_state = n_puzzle(4,[5,6,7,8])
test_node = node(test_state, None, 1)
PDB_4_2 = PDB_UCS(test_node)
end = time.time()
print(end-start)
np.save('PDB_4_2.npy', PDB_4_2)

#PDB Construction
#start = time.time()
#test_state = n_puzzle(4,[8,11,12,14,15])
#test_node = node(test_state, None, 1)
#PDB_5_1 = PDB_UCS_5(test_node)
#end = time.time()
#print(end-start)
#np.save('PDB_5_1.npy', PDB_5_1)

#PDB Construction
#start = time.time()
#test_state = n_puzzle(4,[5,6,9,10,13])
#test_node = node(test_state, None, 1)
#PDB_5_2 = PDB_UCS_5(test_node)
#end = time.time()
#print(end-start)
#np.save('PDB_5_2.npy', PDB_5_2)

#PDB Construction
start = time.time()
test_state = n_puzzle(4,[10,11,13,14,15])
test_node = node(test_state, None, 1)
PDB_5_4 = PDB_UCS_5(test_node)
end = time.time()
print(end-start)
np.save('PDB_5_4.npy', PDB_5_4)

#PDB Construction
#start = time.time()
#test_state = n_puzzle(4,[1,5,6,9,10,13])
#test_node = node(test_state, None, 1)
#PDB_6_2 = PDB_UCS_6(test_node)
#end = time.time()
#print(end-start)
#np.save('PDB_6_2.npy', PDB_6_2)