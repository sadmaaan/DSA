def search(nums, target):  
    start = 0
    end = len(nums) - 1
    pivot = find_pivot(nums)
    
    if pivot == -1:
        return binary_search(nums, target, start, end)
    else:
        if nums[pivot] == target:
            return pivot
        elif target >= nums[0]:   
            return binary_search(nums, target, start, pivot-1)

    return binary_search(nums, target, pivot+1, end)
            
            
def find_pivot(arr):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if mid < end and arr[mid] > arr[mid+1]:
            return mid
        elif mid > start and arr[mid] < arr[mid-1]:
            return mid-1
        elif arr[mid] > arr[start]:
            start = mid + 1
        else:
            end = mid - 1
            
    return -1
     
def binary_search(nums, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            return mid

    return -1
    
print(search([7,8,1,2,3,4,5,6], 2))