def dice(string, target, l):
    if target == 0:
        l.append(string)
        return

    for i in range(1, 7, 1):
        if i <= target:
            dice(string + str(i), target - i, l)

    return l

print(dice("", 6, []))