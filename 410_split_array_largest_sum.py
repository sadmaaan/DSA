def splitArray(nums, k):
    start = 0
    end = 0

    for i in range(len(nums) - 1):
        start = max(nums)
        end = end + nums[i]
    
    # Binary search to find the potential max sum which also splits in k sub-array
    while start < end:
        subArray_count = 1 #initial
        sum = 0
        mid = start + (end - start) // 2

        for num in nums:
            if sum + num > mid: # if first sub-array exceed mid value
                sum = num
                subArray_count += 1
            else:
                sum += num # first sub-array/piece
        
        if subArray_count <= k: # sub-array count < m means try to reduce the potential ans to get more sub-array/pieces 
            end = mid
        else:
            start = mid + 1

    return end    



nums = [7,2,5,10,8]
k = 2
print(splitArray(nums, k))
        