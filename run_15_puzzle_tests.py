import random
import numpy as np
import time
import math
from search_algorithms import *
from n_puzzle import n_puzzle

PDB_3_1 = np.load('saved_PDBs/PDB_3_1.npy')
PDB_4_1 = np.load('saved_PDBs/PDB_4_1.npy')
PDB_4_2 = np.load('saved_PDBs/PDB_4_2.npy')
PDB_4_3 = np.load('saved_PDBs/PDB_4_3.npy')
PDB_5_1 = np.load('saved_PDBs/PDB_5_1.npy')
PDB_5_2 = np.load('saved_PDBs/PDB_5_2.npy')
PDB_5_3 = np.load('saved_PDBs/PDB_5_3.npy')
PDB_5_4 = np.load('saved_PDBs/PDB_5_4.npy')
PDB_5_5 = np.load('saved_PDBs/PDB_5_5.npy')
PDB_6_1 = np.load('saved_PDBs/PDB_6_1.npy')
PDB_6_2 = np.load('saved_PDBs/PDB_6_2.npy')
PDB_6_3 = np.load('saved_PDBs/PDB_6_3.npy')

def Tiles_Out_Of_Place(state):
    n = state.n
    puzzle = state.puzzle
    compare = 1
    oop = 0
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] != 0 and puzzle[i][j]%16 != compare%16:
                oop +=1
            compare+=1
    return oop

#Build correct indices for Manhanttan_Distance
def build_MDI():
    mdi = []
    mdi.append(None)
    #For 1
    mdi.append((0,0))
    #For 2
    mdi.append((0,1))
    #For 3
    mdi.append((0,2))
    #For 4
    mdi.append((0,3))
    #For 5
    mdi.append((1,0))
    #For 6
    mdi.append((1,1))
    #For 7
    mdi.append((1,2))
    #For 8
    mdi.append((1,3))
    #For 9
    mdi.append((2,0))
    #For 10
    mdi.append((2,1))
    #For 11
    mdi.append((2,2))
    # For 12
    mdi.append((2,3))
    # For 13
    mdi.append((3,0))
    # For 14
    mdi.append((3,1))
    # For 15
    mdi.append((3,2))
    return mdi
mdi = build_MDI()

def Manhanttan_Distance(state):
    n = state.n
    goal_puzzle = n_puzzle(4)
    puzzle = state.puzzle
    compare = 1
    oop = 0
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] != 0 and puzzle[i][j] != compare:
                xCor,yCor = mdi[puzzle[i][j]]
                xDisp = abs(xCor - i)
                yDisp = abs(yCor - j)
                oop+=(xDisp + yDisp)
            compare += 1
    return oop

# 6-6-3
def PDB_663_Heuristic(state):
    puzzle = state.puzzle

    # FIRST PDB ----------------------------------------------------------
    non_blank = [2, 3, 4]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value1 = PDB_3_1[indices[0]][indices[1]][indices[2]]

    # SECOND PDB ----------------------------------------------------------
    non_blank = [1, 5, 6, 9, 10, 13]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value2 = PDB_6_2[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]][indices[5]]

    # THIRD PDB ----------------------------------------------------------
    non_blank = [7, 8, 11, 12, 14, 15]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value3 = PDB_6_1[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]][indices[5]]

    return value1 + value2 + value3


# 4-5-6
def PDB_456_Heuristic(state):
    puzzle = state.puzzle

    # FIRST PDB ----------------------------------------------------------
    non_blank = [8, 11, 12, 14, 15]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value1 = PDB_5_1[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]]

    # SECOND PDB ----------------------------------------------------------
    non_blank = [1, 5, 6, 9, 10, 13]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value2 = PDB_6_2[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]][indices[5]]

    # THIRD PDB ----------------------------------------------------------
    non_blank = [2, 3, 4, 7]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value3 = PDB_4_1[indices[0]][indices[1]][indices[2]][indices[3]]

    return value1 + value2 + value3

# 4-5-6-2
def PDB_456_2_Heuristic(state):
    puzzle = state.puzzle

    # FIRST PDB ----------------------------------------------------------
    non_blank = [10, 11, 13, 14, 15]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value1 = PDB_5_4[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]]

    # SECOND PDB ----------------------------------------------------------
    non_blank = [1, 2, 3, 4, 8, 12]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value2 = PDB_6_3[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]][indices[5]]

    # THIRD PDB ----------------------------------------------------------
    non_blank = [5, 6, 7, 9]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value3 = PDB_4_2[indices[0]][indices[1]][indices[2]][indices[3]]

    return value1 + value2 + value3

# 4-5-6-2
def PDB_456_3_Heuristic(state):
    puzzle = state.puzzle

    # FIRST PDB ----------------------------------------------------------
    non_blank = [5, 9, 13, 14, 15]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value1 = PDB_5_5[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]]

    # SECOND PDB ----------------------------------------------------------
    non_blank = [1, 2, 3, 4, 8, 12]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value2 = PDB_6_3[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]][indices[5]]

    # THIRD PDB ----------------------------------------------------------
    non_blank = [6, 7, 10, 11]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value3 = PDB_4_3[indices[0]][indices[1]][indices[2]][indices[3]]

    return value1 + value2 + value3


# 5-5-5
def PDB_555_Heuristic(state):
    puzzle = state.puzzle

    # FIRST PDB ----------------------------------------------------------
    non_blank = [8, 11, 12, 14, 15]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value1 = PDB_5_1[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]]

    # SECOND PDB ----------------------------------------------------------
    non_blank = [5, 6, 9, 10, 13]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value2 = PDB_5_2[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]]

    # THIRD PDB ----------------------------------------------------------
    non_blank = [1, 2, 3, 4, 7]
    indices = []

    for index in non_blank:
        count = 0
        for i in puzzle:
            for j in i:
                if j == index:
                    indices.append(count)
                count += 1
    value3 = PDB_5_3[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]]

    # [2][3][6][7]
    return value1 + value2 + value3

test_instances = []
for i in range(10):
    test_instances.append(n_puzzle(4))

test_instances[0].set_puzzle([8,0,11,4 ,1,10,7,3, 6,5,2,14, 13,12,9,15])
test_instances[1].set_puzzle([6,4,7,8 ,0,12,10,15, 13,2,9,5, 14,11,3,1])
test_instances[2].set_puzzle([15,3,9,13 ,12,11,5,10, 1,14,8,0, 2,7,6,4])
test_instances[3].set_puzzle([0,14,11,6, 8,15,2,7, 10,9,13,3, 4,12,1,5])
test_instances[4].set_puzzle([9,14,15,12, 13,7,0,6, 5,3,4,10, 1,2,8,11])
test_instances[5].set_puzzle([10,14,2,8, 13,15,12,9, 4,3,11,1, 6,5,0,7])
test_instances[6].set_puzzle([6,5,0,4, 1,10,12,13, 11,8,15,14, 2,9,7,3])
test_instances[7].set_puzzle([12,14,4,6, 2,11,7,15, 3,1,10,0, 8,9,13,5])
test_instances[8].set_puzzle([4,3,0,15, 7,14,1,6, 11,13,5,10, 8,2,9,12])
test_instances[9].set_puzzle([15,7,5,10, 4,0,12,6, 2,11,1,14, 9,13,8,3])

#ida_star_path_dd(test_instances[1], PDB_555_Heuristic)


f = open("output.txt","w")
repeatNum = 5
for num, test_instance in enumerate(test_instances):
    f.write("Test instance:")
    f.write(str(num))
    f.write('\n')
    time_sum=0
    for i in range(repeatNum):
        info = a_star_dd_extra_mem(test_instance, PDB_663_Heuristic)
        #info = ida_star_path_dd(test_instance, PDB_663_Heuristic)
        time_sum+=info[0]
    time_elapsed=time_sum/repeatNum
    f.write("PDB_663")
    f.write('\n')
    f.write("Time Elapsed:")
    f.write(str(time_elapsed))
    f.write('\n')
    f.write("Nodes Generated:")
    f.write(str(info[1]))
    f.write('\n')
    f.write("Nodes Expanded:")
    f.write(str(info[2]))
    f.write('\n')
    f.write("Cost:")
    f.write(str(info[3]))
    f.write('\n\n')

    time_sum = 0
    for i in range(repeatNum):
        info = a_star_dd_extra_mem(test_instance, PDB_456_Heuristic)
        #info = ida_star_path_dd(test_instance, PDB_456_Heuristic)
        time_sum += info[0]
    time_elapsed = time_sum / repeatNum
    f.write("PDB_456")
    f.write('\n')
    f.write("Time Elapsed:")
    f.write(str(time_elapsed))
    f.write('\n')
    f.write("Nodes Generated:")
    f.write(str(info[1]))
    f.write('\n')
    f.write("Nodes Expanded:")
    f.write(str(info[2]))
    f.write('\n')
    f.write("Cost:")
    f.write(str(info[3]))
    f.write('\n\n')

    time_sum = 0
    for i in range(repeatNum):
        info = a_star_dd_extra_mem(test_instance, PDB_456_2_Heuristic)
        #info = ida_star_path_dd(test_instance, PDB_456_2_Heuristic)
        time_sum += info[0]
    time_elapsed = time_sum / repeatNum
    f.write("PDB_456-2")
    f.write('\n')
    f.write("Time Elapsed:")
    f.write(str(time_elapsed))
    f.write('\n')
    f.write("Nodes Generated:")
    f.write(str(info[1]))
    f.write('\n')
    f.write("Nodes Expanded:")
    f.write(str(info[2]))
    f.write('\n')
    f.write("Cost:")
    f.write(str(info[3]))
    f.write('\n\n')

    time_sum = 0
    for i in range(repeatNum):
        info = a_star_dd_extra_mem(test_instance, PDB_456_3_Heuristic)
        #info = ida_star_path_dd(test_instance, PDB_456_3_Heuristic)
        time_sum += info[0]
    time_elapsed = time_sum / repeatNum
    f.write("PDB_456-3")
    f.write('\n')
    f.write("Time Elapsed:")
    f.write(str(time_elapsed))
    f.write('\n')
    f.write("Nodes Generated:")
    f.write(str(info[1]))
    f.write('\n')
    f.write("Nodes Expanded:")
    f.write(str(info[2]))
    f.write('\n')
    f.write("Cost:")
    f.write(str(info[3]))
    f.write('\n\n')

    time_sum = 0
    for i in range(repeatNum):
        info = a_star_dd_extra_mem(test_instance, PDB_555_Heuristic)
        #info = ida_star_path_dd(test_instance, PDB_555_Heuristic)
        time_sum += info[0]
    time_elapsed = time_sum / repeatNum
    f.write("PDB_555")
    f.write('\n')
    f.write("Time Elapsed:")
    f.write(str(time_elapsed))
    f.write('\n')
    f.write("Nodes Generated:")
    f.write(str(info[1]))
    f.write('\n')
    f.write("Nodes Expanded:")
    f.write(str(info[2]))
    f.write('\n')
    f.write("Cost:")
    f.write(str(info[3]))
    f.write('\n\n')
    f.write('\n\n')



f.close()


#a_star_dd_extra_mem(test_instances[0],PDB_663_Heuristic)
#a_star_dd_extra_mem(test_instances[0],PDB_456_Heuristic)
#a_star_dd_extra_mem(test_instances[0],Manhanttan_Distance)
#a_star_dd_extra_mem(test_instances[0],Tiles_Out_Of_Place)
