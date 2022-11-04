def firstMissingPositive(nums):
    i = 0
        
    while i < len(nums):                
        correct_index = nums[i] - 1
        
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct_index]:
            temp = nums[i]
            nums[i] = nums[correct_index]
            nums[correct_index] = temp
        else:
            i += 1
            
    val = 0
    for i in range(len(nums)):
        if nums[i] != i + 1:
            val = i + 1
            return val
    
    return len(nums) + 1

print(firstMissingPositive([3,4,-1,1]))