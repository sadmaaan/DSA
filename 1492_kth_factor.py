def kthFactor(n, k):
    if k < 0:
        return 0
    
    l = []     
    for i in range(1, n+1):
        if n % i == 0:
            l.append(i)
    
    return l[k-1]

print(kthFactor(4, 4))