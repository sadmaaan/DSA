def nextPermutation(nums):
    temp = True
    if len(nums) <=2:
        nums[::] = nums[::-1]
        temp = False
        
    pointer = len(nums) - 2
    while pointer >= 0 and nums[pointer] >= nums[pointer+1]:
        pointer -= 1
    
    if pointer == -1:
        nums[::] = nums[::-1]
        temp = False
    
    for i in range(len(nums)-1, pointer, -1):
        if nums[pointer] < nums[i]:
            nums[pointer], nums[i] = nums[i], nums[pointer]
            break
    
    if temp:
        nums[pointer+1:] = nums[pointer+1:][::-1]

    return nums

# nums = [1,2,3,6,5,4]
nums = [3,2]
print(nextPermutation(nums))