def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right, arr.copy())

def merge(left, right, merged_arr):
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr[k] = left[i]
            i += 1
        else:
            merged_arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged_arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged_arr[k] = right[j]
        j += 1
        k += 1
    
    return merged_arr



print(merge_sort([3,4,5,7,1,2,0,9,7]))