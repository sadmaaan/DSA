# gives XOR from 0 to n
# this works better
# using lopp will give timelimitexceed for large number
def xor(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    else:
        return 0

# xor between 3 to 9
a = 3
b = 9
print(xor(a-1) ^ xor(b))
