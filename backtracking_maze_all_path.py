def all_path(r, c, p, mage):
    if r == len(mage) - 1 and c == len(mage[0]) - 1:
        print(p)
        return
    
    if not mage[r][c]:
        return
    
    mage[r][c] = False # backtracking -> making false during recursive call

    # if r < len(mage) - 1 and c < len(mage) - 1:
    #     all_path(r + 1, c + 1, p + 'd', mage)
    if r < len(mage) - 1:
        all_path(r + 1, c, p + 'D', mage)
    if c < len(mage[0]) - 1:
        all_path(r, c + 1, p + 'R', mage)
    if r > 0:
        all_path(r - 1, c, p + 'U', mage)
    if c > 0:
        all_path(r, c - 1, p + 'L', mage)

    mage[r][c] = True # backtracking -> making true when returning
        


mage = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]
all_path(0, 0, "", mage)