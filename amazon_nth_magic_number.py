def nth_magic_number(n):
    ans = 0
    base = 5

    while n > 0:
        last = n&1
        n = n >> 1
        ans += last * base
        base *= 5
    
    return ans


print(nth_magic_number(6))