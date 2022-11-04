from re import A


def gcd_loop(a, b):
    if a > b:
        small = b
    else:
        small = a

    for i in range(1, small + 1):
        if (a % i == 0) and (b % i == 0):
            gcd  = i
    return gcd

def gcd_recursion(a, b):
    if a == 0:
        return b
    return gcd_recursion(b % a, a)

def lcm(a, b):
    return (a * b) // gcd_recursion(a, b)

print(gcd_recursion(30, 68))
print(lcm(30, 68))