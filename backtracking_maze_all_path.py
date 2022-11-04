def all_path(r, c, p, maze):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        print(p)
        return
    
    if not maze[r][c]:
        return
    
    maze[r][c] = False # backtracking -> making false during recursive call

    # if r < len(mage) - 1 and c < len(mage) - 1:
    #     all_path(r + 1, c + 1, p + 'd', mage)
    if r < len(maze) - 1:
        all_path(r + 1, c, p + 'D', maze)
    if c < len(maze[0]) - 1:
        all_path(r, c + 1, p + 'R', maze)
    if r > 0:
        all_path(r - 1, c, p + 'U', maze)
    if c > 0:
        all_path(r, c - 1, p + 'L', maze)

    maze[r][c] = True # backtracking -> making true when returning
        


mage = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]
all_path(0, 0, "", mage)