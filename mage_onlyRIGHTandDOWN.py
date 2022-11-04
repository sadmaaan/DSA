def count(r, c):
    if r == 1 or c == 1:
        return 1
    
    left = count(r - 1, c)
    right = count(r, c - 1)
    
    return left + right

def path(r, c, p):
    if r == 1 and c == 1:
        print(p)
        return
    
    if r > 1:
        path(r - 1, c, p + 'D')
    if c > 1:
        path(r, c - 1, p + 'R')

def path_inc_diagonal(r, c, p):
    if r == 1 and c == 1:
        print(p)
        return
    
    if r > 1 and c > 1:
        path_inc_diagonal(r - 1, c - 1, p + 'd')
    if r > 1:
        path_inc_diagonal(r - 1, c, p + 'D')
    if c > 1:
        path_inc_diagonal(r, c - 1, p + 'R')

def start_from_zerozero(r, c, p, mage):
    if r == len(mage) - 1 and c == len(mage[0]) - 1:
        print(p)
        return
    
    if mage[r][c] == False:
        return
    if r < len(mage) - 1 and c < len(mage) - 1:
        start_from_zerozero(r + 1, c + 1, p + 'd', mage)
    if r < len(mage) - 1:
        start_from_zerozero(r + 1, c, p + 'D', mage)
    if c < len(mage) - 1:
        start_from_zerozero(r, c + 1, p + 'R', mage)

# print(count(3, 3))
# path(3, 3, "")
# path_inc_diagonal(3, 3, "")
mage = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]
start_from_zerozero(0, 0, "", mage)