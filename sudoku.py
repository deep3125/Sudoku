class sudoku_solver():
    '''
    This class can solve sudoku of 9X9.
    '''

    # loops through all colums in a row to
    #  check for similwr value
    def check_row(self, board, i, j):
        for ind in range(0, len(board[j])): 
            if ind!=j and board[i][ind]==board[i][j]:
                return False
        return True

    # Checks if there is any value similar
    #  to value at index i, j in an entire
    #  column
    def check_column(self, board, i, j):
        for ind in range(0, len(board)): 
            if ind!=i and board[ind][j]==board[i][j]:
                return False
        return True

    def check_box(self, board, i, j):
        div_i = i//3
        div_j = j//3
        # finding boundaries of imaginary box in which the index
        # i, j exists 
        min_r, max_r = div_i*3, (div_i+1)*3-1
        min_c, max_c = div_j*3, (div_j+1)*3-1

        for r in range(min_r, max_r+1):
            for c in range(min_c, max_c+1):
                if (r!=i and c!=j) and board[i][j]==board[r][c]:
                    return False      
        return True


    def solve(self, board):
        # stores indexs of board with 0 value
        fillable_indexes = []  
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j]==0:
                    fillable_indexes.append((i, j))
        
        ind = 0
        # looping through the fillable indexes
        while ind<len(fillable_indexes):
            i, j = fillable_indexes[ind]

            # if value at current fillable index 
            # is greater than or equal to 9 then
            # set it to 0 and backtrack it to
            # previous fillable value
            while board[i][j]>=9:  
                board[i][j]=0
                ind-=1
                i, j = fillable_indexes[ind]
            
            # if current value is not acceptable 
            # according to checks mentioned in while
            # loop than increment the value at current
            # fillable position.
            board[i][j]+=1
            while not (self.check_box(board, i, j) and self.check_row(board, i, j) and self.check_column(board, i, j)):
                board[i][j]+=1
            
            # Increment ind at value less than equal to
            # 9. Note 9 is also an acceptable value.
            if board[i][j]<=9:
                ind+=1
        return board
    
