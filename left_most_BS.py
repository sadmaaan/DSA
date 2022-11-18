def left_most_bs(arr, target):
    left = 0
    right =len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
             right = mid
        
    return left


print(left_most_bs([1,2,3,4,5,6,7,9], 8))