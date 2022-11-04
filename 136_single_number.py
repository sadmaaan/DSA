from cmath import sin


def singleNumber(nums):
    single_num = 0
    for i in nums:
        single_num ^= i
        
    return single_num

print(singleNumber([1,2,3,4,2,1,3]))