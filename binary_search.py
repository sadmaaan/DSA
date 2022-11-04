def search(nums, target):
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            return mid
    
    return -1

print(search([1,2,3,4,5,7,8,9,70], 7))
 