def rotated_bs(nums, target, start, end):    
    if start > end:
            return -1
        
    mid = start + (end - start) // 2
    if nums[mid] == target:
        return mid
    
    if nums[start] <= nums[mid]:
        if target >= nums[start] and target <= nums[mid]:
            return rotated_bs(nums, target, start, mid-1)
        else:
            return rotated_bs(nums, target, mid+1, end)
            
    if target >= nums[mid] and target <= nums[end]:
        return rotated_bs(nums, target, mid+1, end)
    else:
        return rotated_bs(nums, target, start, mid-1)

arr = [4,5,7,8,9,70,1,2,3]
print(rotated_bs(arr, 1, 0, len(arr) - 1))