def all_path(r, c, p, maze, path, step):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        path[r][c] = step
        for i in path:
            # print('\t'.join(map(str, i)))
            print(i)
        print(p)
        print("\n")
        return
    
    if not maze[r][c]:
        return
    
    maze[r][c] = False # backtracking -> making false during recursive call
    path[r][c] = step

    if r < len(maze) - 1 and c < len(maze) - 1:
        all_path(r + 1, c + 1, p + 'd', maze, path, step + 1)
    if r < len(maze) - 1:
        all_path(r + 1, c, p + 'D', maze, path, step + 1)
    if c < len(maze[0]) - 1:
        all_path(r, c + 1, p + 'R', maze, path, step + 1)
    if r > 0:
        all_path(r - 1, c, p + 'U', maze, path, step + 1)
    if c > 0:
        all_path(r, c - 1, p + 'L', maze, path, step + 1)

    maze[r][c] = True # backtracking -> making true when returning
    path[r][c] = 0
        

# main
maze = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]

w, h = len(maze), len(maze[0])
path = [[0 for x in range(w)] for y in range(h)] 
all_path(0, 0, "", maze, path, 1)