def findErrorNums(nums):
    i = 0
    
    while i < len(nums):
        correct_index = nums[i] - 1
        
        if nums[i] != nums[correct_index]:
            temp = nums[i]
            nums[i] = nums[correct_index]
            nums[correct_index] = temp
        else:
            i += 1
            
    arr = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            arr.append(nums[i])
            arr.append(i+1)
            
    return arr

print(findErrorNums([2, 3, 2]))