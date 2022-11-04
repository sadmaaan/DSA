def order_agnostic_binary_search(nums, target, start, end):
    is_asc = nums[start] < nums[end]
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if target == nums[mid]:
            return mid
        
        if is_asc:
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1 
    
    return -1

def findPeakElement(nums):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = start + (end - start) // 2

        if nums[mid] < nums[mid+1]:
            start = mid + 1
        else:
            end = mid

    return start

if __name__ == '__main__':
    arr = [1,2,3,4,5,3,1]
    target = 3
    i = []

    start = 0
    end = len(arr) - 1

    peak = findPeakElement(arr)

    i1 = order_agnostic_binary_search(arr, target, start, peak-1)
    i.append(i1)

    i2 = order_agnostic_binary_search(arr, target, peak+1, end)
    i.append(i2)

print(i)