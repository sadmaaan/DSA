def permutations(arr, new_arr, l):
    if len(arr) == 0:
        l.append(new_arr)
        return

    ch = arr[0]
    for i in range(len(new_arr) + 1):
        start = new_arr[0:i]
        end = new_arr[i:len(new_arr)]
        permutations(arr[1:], start + ch + end, l)

    return l

s = "abc"
print(permutations(s, "", []))