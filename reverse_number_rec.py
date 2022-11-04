import math
def rev(n):
    digits = int(math.log10(n)) + 1
    return helper(n, digits)

def helper(n, dig):
    if n % 10 == n:
        return n
    
    return n % 10 * 10**(dig-1) + helper(n // 10, dig - 1)


print(rev(12345))