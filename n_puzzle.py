import random
class n_puzzle:
    def __init__(self, n, non_blank=None):
        self.n = n
        self.puzzle = []
        self.non_blank = non_blank
        for i in range(n):
            rowI = []
            for j in range(n):
                if non_blank == None:
                    rowI.append((i * n) + (j + 1))
                else:
                    num = (i * n) + (j + 1)
                    if num in non_blank:
                        rowI.append(num)
                    else:
                        rowI.append(-1)
            self.puzzle.append(rowI)
        self.puzzle[-1][-1] = 0
        return

    # https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
    def count_inversions(self):
        flattenedArray = []
        for row in self.puzzle:
            for tile in row:
                if (tile != 0):
                    flattenedArray.append(tile)
        inversions = 0
        N = len(flattenedArray)
        for i in range(N):
            for j in range(i + 1, N):
                if (flattenedArray[i] > flattenedArray[j]):
                    inversions += 1
        return inversions

    # Used for testing
    def set_puzzle(self, neworder):
        for i in range(self.n):
            for j in range(self.n):
                self.puzzle[i][j] = neworder[(i * self.n) + (j)]
        return

    def check_solvability(self):
        # If n is odd, we know that the instance is solvable
        # if and only if the number of inversions is even.
        inversions = self.count_inversions()
        if (self.n % 2) == 1:
            if (inversions % 2) == 0:
                return True
            else:
                return False

        # In the case where n is even, we must consider two subcases:
        # If the blank is on an even row then,
        #     The instance is solvable if and only if,
        #     the number of inversions is odd.
        # If the blank is on an odd row then,
        #     The instance is solvable if and only if,
        #     the number of inversions is even.
        else:
            # Start by finding row of 0
            row_of_zero = -1
            for row in range(self.n):
                for col in range(self.n):
                    if self.puzzle[row][col] == 0:
                        row_of_zero = row
            # If the blank is on an even row
            if (row_of_zero % 2) == 0:
                if (inversions % 2) == 1:
                    return True
            else:
                if (inversions % 2) == 0:
                    return True
        return False

    def scramble(self):
        while True:
            # Creates a random tile puzzle
            candidates = []
            neworder = []
            for i in range(self.n * self.n):
                candidates.append(i)
            for i in range(self.n * self.n):
                m = len(candidates)
                tileNo = random.randint(0, m - 1)
                neworder.append(candidates[tileNo])
                candidates.pop(tileNo)
            for i in range(self.n):
                for j in range(self.n):
                    self.puzzle[i][j] = neworder[(i * self.n) + (j)]

            # Checks if the tile puzzle is solvable.
            if self.check_solvability() == True:
                return
        return

    def display(self):
        for row in self.puzzle:
            for tile in row:
                if tile == 0:
                    print('_', end='   ')
                elif tile < 10:
                    print(tile, end='   ')
                else:
                    print(tile, end='  ')
            print('\n')
        return

    # For get_actions(), all possible actions
    # are returned for the given instance of the
    # board where,
    #
    # 0 = Moving blank up
    # 1 = Moving blank to the right
    # 2 = Moving blank to the left
    # 3 = Moving blank down
    #
    def get_actions(self):
        actions = []
        row_of_zero = -1
        col_of_zero = -1
        # Note: Optimize this by saving position as an attribute of
        # the class and update it on performing an action.
        for row in range(self.n):
            for col in range(self.n):
                if self.puzzle[row][col] == 0:
                    row_of_zero = row
                    col_of_zero = col

        if row_of_zero != 0:
            actions.append(0)
        if row_of_zero != (self.n - 1):
            actions.append(3)
        if col_of_zero != 0:
            actions.append(2)
        if col_of_zero != (self.n - 1):
            actions.append(1)
        return actions

    # Here we perform the action given as
    # either 0,1,2, or 4 (as defined above).
    # To save time, there's no check to make
    # sure the action is valid, so use only
    # actions returned from get_actions()
    def perform_action(self, action):
        # Note: Optimize this by saving position as an attribute of
        # the class and update it on performing an action.
        for row in range(self.n):
            for col in range(self.n):
                if self.puzzle[row][col] == 0:
                    row_of_zero = row
                    col_of_zero = col

        # Up
        if action == 0:
            self.puzzle[row_of_zero][col_of_zero] = self.puzzle[row_of_zero - 1][col_of_zero]
            self.puzzle[row_of_zero - 1][col_of_zero] = 0
            return

        # Right
        if action == 1:
            self.puzzle[row_of_zero][col_of_zero] = self.puzzle[row_of_zero][col_of_zero + 1]
            self.puzzle[row_of_zero][col_of_zero + 1] = 0
            return

        # Left
        if action == 2:
            self.puzzle[row_of_zero][col_of_zero] = self.puzzle[row_of_zero][col_of_zero - 1]
            self.puzzle[row_of_zero][col_of_zero - 1] = 0
            return

        # Down
        if action == 3:
            self.puzzle[row_of_zero][col_of_zero] = self.puzzle[row_of_zero + 1][col_of_zero]
            self.puzzle[row_of_zero + 1][col_of_zero] = 0
            return

    # Used for testing
    def display_actions(self):
        print('Actions:', end=' ')
        for action in self.get_actions():
            # Up
            if action == 0:
                print('Up', end=' ')
            # Right
            if action == 1:
                print('Right', end=' ')
            # Left
            if action == 2:
                print('Left', end=' ')
            # Down
            if action == 3:
                print('Down', end=' ')
        print('')
        pass

    # Used for testing
    def get_action_text(self, action):
        # Up
        if action == 0:
            return 'Up'
        # Right
        if action == 1:
            return 'Right'
        # Left
        if action == 2:
            return 'Left'
        # Down
        if action == 3:
            return 'Down'
