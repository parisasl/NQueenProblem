class NQueens:
    # Initializing size of the (chess)board
    def __init__(self, size):
       
        self.size = size
        self.solutions = 0
        self.solve()
 
    def solve(self):
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print(self.solutions, " solution(s) have been found!")
 
    def put_queen(self, positions, target_row):
        if target_row == self.size:
            '''if we check all the rows and find a place for queens in each column, it means we have found
            solution and now, we need to show it.'''
            self.show_full_board(positions)
            self.solutions += 1
        else:
            
            for column in range(self.size):
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    # backtracking algorithm
                    self.put_queen(positions, target_row + 1)
                    
    # check the possible places for queens according to the previous assignments.
    def check_place(self, positions, ocuppied_rows, column):
        # no queens attack each other by being in the same row, column or diagonal.
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:
                    return False
        return True
    
    def show_full_board(self, positions):
        # The position of the queens have been determined and now we should demonstrate it. 
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += " O "
                else:
                     line += ". "
            print(line)
        print("\n")
         
NQueens(4)
