def n_Knights(board, row, col, knights):
    if knights == 0:
        display(board)
        print('\n')
        return
    
    if row == len(board) - 1 and col == len(board):
        return

    if col == len(board):
        n_Knights(board, row + 1, 0, knights)
        return
    
    if is_safe(board, row, col):
        board[row][col] = True
        n_Knights(board, row, col + 1, knights - 1)
        board[row][col] = False  
    
    n_Knights(board, row, col + 1, knights)

def is_safe(board, row, col):
    if is_valid(board, row - 2, col - 1):
        if board[row - 2][col - 1]:
            return False

    if is_valid(board, row - 2, col + 1):
        if board[row - 2][col + 1]:
            return False

    if is_valid(board, row - 1, col - 2):
        if board[row - 1][col - 2]:
            return False

    if is_valid(board, row - 1, col + 2):
        if board[row - 1][col + 2]:
            return False
            
    return True

def is_valid(board, row, col):
    if row >= 0 and row < len(board) and col >= 0 and col < len(board):
        return True

    return False


def display(base):
    for i in base:
        for j in i:
            if j == True:
                print('K', end=" ")
            else:
                print('X', end=" ")
        print('\n')


n = 4
board = [[False for x in range(n)] for y in range(n)] 
print(n_Knights(board, 0, 0, n))