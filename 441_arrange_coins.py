def arrangeCoins(n):
    l = 0
    h = n
    
    while l < h:
        mid  = l + (h - l) // 2
        temp = (mid * (mid + 1))
        
        if temp == n:
            return mid
        elif temp < n:
            l = mid + 1
        else:
            h = mid - 1

print(arrangeCoins(5))