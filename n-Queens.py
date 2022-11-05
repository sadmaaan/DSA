def n_Queens(board, r):
    if r == len(board):
        display(board)
        print('\n')
        return 1
    
    count = 0
    for c in range(len(board)):
        if is_safe(board, r, c):
            board[r][c] = True
            count += n_Queens(board, r + 1)
            board[r][c] = False

    return count
            

def is_safe(base, r, c):
    for i in range(r):
        if base[i][c]:
            return False
    
    diag_left = min(r, c)
    for j in range(1, diag_left + 1):
        if base[r-j][c-j]:
            return False

    diag_right = len(base) - c - 1
    for k in range(1, diag_right + 1):
        if base[r-k][c+k]:
            return False

    return True


def display(base):
    for i in base:
        for j in i:
            if j == True:
                print('Q', end=" ")
            else:
                print('X', end=" ")
        print('\n')


n = 4
w, h = n, n
board = [[False for x in range(w)] for y in range(h)] 
print(n_Queens(board, 0))