def search(nums, target, start, end):    
    while start <= end:
        mid = start + (end - start) // 2
        
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            return mid
    
    return -1

if __name__ == '__main__':
    nums = [1,2,3,5,7,8,9,10,11,15,17,19,22,24,27,33,35,39,44,444,445, 446, 447,448,449,450,1000,10009, 10009, 10009, 10009, 10009, 10009] 
    target = 444
    start = 0
    end = 1

    
    while start <= end:
        if target >= nums[start] and target <= nums[end]:
            i = start
            j = end
            break
        else:
            new_start = end + 1
            end = end + (end - start + 1) * 2
            start = new_start
        
    
    
    print(search(nums, target, i, j))