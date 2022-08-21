*** FOR "run_8_puzzle.py" USAGE ***

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


*** FOR "run_15_puzzle_tests.py" USAGE ***

Here, simply running "python3 run_15_puzzle_tests.py" will automatically begin outputting
results and solutions for our preprogrammed test cases. There is no feature to implement
your own instances. It must be done manually within the code. Note, some instances take
a very long time to solve (over an hour). If the results are to be duplicated consider
lowering the repeatNum variable to 1, and commenting out test instances 2,3,4,5,6.
More concise output is saved to "output.txt". I apologize for the terminal output being
verbose.  


*** FOR "PDB_Builder.py" USAGE ***
Here, simply running "python3 PDB_Builder.py" will automatically construct whichever PDB
is uncommented in the code. Constructing a new PDB requires changing the code. PDBs are
saved to the current directory, to avoid accidentally overwriting an existing PDB.