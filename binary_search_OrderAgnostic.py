def order_agnostic_binary_search(nums, target):
    start = 0
    end = len(nums) - 1
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

# print(search([1,2,3,4,5,7,8,9,70], 9))
print(order_agnostic_binary_search([9,8,7,6,5,4,3,2,1], 9))