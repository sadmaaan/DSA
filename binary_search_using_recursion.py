def search(nums, target, start, end):    
    while start <= end:
        if start > end:
            return -1
        
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        
        if target < nums[mid]:
            return search(nums, target, start, mid-1)
        return search(nums, target, mid+1, end)

arr = [1,2,3,4,5,7,8,9,70]
print(search(arr, 70, 0, len(arr) - 1))