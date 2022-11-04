def nthUglyNumber(n):
    l = [1]
    i = 2
    while len(l) <= n:
        if isUgly(i):
            l.append(i)
        i += 1
    
    return l[-1]
    
def isUgly(n):
    for p in [2, 3, 5]:
        while n % p == 0:
            n = n // p
        
    return n == 1

print(nthUglyNumber(10))