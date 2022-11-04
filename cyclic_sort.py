# *****when given 1 to N range(no gap in between) then apply cyclic sort
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        correct_index = arr[i] - 1

        if arr[i] != arr[correct_index]:
            temp = arr[i]
            arr[i] = arr[correct_index]
            arr[correct_index] = temp
        else:
            i += 1
    return arr

print(cyclic_sort([5, 3, 4, 1, 2]))