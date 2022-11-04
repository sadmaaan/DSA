def selfDividingNumbers(left, right):
    l = []
    for i in range(left, right + 1):
        val = i
        c = 0
        while i > 0:
            rem = i % 10
            if rem != 0 and val % rem == 0:
                c += 1
            i //= 10

        if c == len(str(val)):
            l.append(val)

    return l

print(selfDividingNumbers(12, 22))