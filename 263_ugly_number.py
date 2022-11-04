def isUgly(n):
    if n <= 0:
            return False
    if n == 1:
        return True
    i = 2  
    while i * i <= n:  
        if n % i:  
            i += 1  
        else:  
            n //= i  
            
    return n <= 5

print(isUgly(500))