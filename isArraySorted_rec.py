def isSorted(arr, index):
    if index == len(arr) - 1:
        return True
    
    return arr[index] < arr[index + 1] and isSorted(arr, index + 1)


print(isSorted([1,2,3,4,5,6,7], 0))