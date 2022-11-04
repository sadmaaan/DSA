def sub_set(arr):
    outer = []
    outer.append([])

    for i in arr:
        size = len(outer)
        for j in range(size):
            inner = outer[j].copy()
            inner.append(i)
            outer.append(inner)
    
    return outer

arr = [1, 2, 3, 4, 5]
print(sub_set(arr))