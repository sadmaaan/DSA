def twoSum(nums, target):
    hashMap = {}
    
    for i, num in enumerate(nums):
        diff = target - num
        
        if diff in hashMap:
            return [hashMap[diff], i]
        
        hashMap[num] = i

print(twoSum([1,2,3,5,7,9], 8))