import math

def solve(board):
    row = -1
    col = -1

    space_left = True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                row = i
                col = j
                space_left = False
                break
        if not space_left:
            break

    if space_left:
        return True
    
    for number in range(1, 10):
        if is_safe(board, row, col, number):
            board[row][col] = number
            if solve(board):
                return True # found ans
            else:
                board[row][col] = 0
    
    return False



def is_safe(board, row, col, number):
    # checking rows
    for row_value in board[row]:
        if row_value == number:
            return False
    
    # checking colums
    for each_row in board:
        if each_row[col] == number:
            return False
    
    # checking 3*3 grid
    inc = int(math.sqrt(len(board)))
    row_start = row - row % inc
    col_start = col - col % inc
    for i in range(row_start, row_start + inc):
        for j in range(col_start, col_start + inc):
            if board[i][j] == number:
                return False
    
    return True

def display(board):
    for i in board:
        for num in i:
            print(num, end=" ")
        print('\n')



# main
sudoku = [  [8,6,0,0,2,0,0,0,0],
			[0,0,0,7,0,0,0,5,9],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,6,0,8,0,0],
			[0,4,0,0,0,0,0,0,0],
			[0,0,5,3,0,0,0,0,7],
			[0,0,0,0,0,0,0,0,0],
			[0,2,0,0,0,0,6,0,0],
			[0,0,7,5,0,9,0,0,0] ]
			
if solve(sudoku):
    display(sudoku)
else:
    print("not solved!!!")