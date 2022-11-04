def ls_rec(arr, target, index):
    if index == len(arr):
        return False
    
    return arr[index] == target or ls_rec(arr, target, index + 1)

def ls_rec2(arr, target, index):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    else:
        return ls_rec2(arr, target, index + 1)

print(ls_rec([1,2,5,4,98,66], 98, 0))
print(ls_rec2([1,2,5,4,98,66], 98, 0))