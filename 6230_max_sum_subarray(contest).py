def maximumSubarraySum(nums, k):
    res = -1
    count = 0
    for i in range(len(nums) - (k - 1)):
        s = 0
        is_distinct = False
        j = i
        while j < i + k:
            if j+k <= len(nums):
                if count == 0:
                    if helper(j, k, nums):
                        is_distinct = True
                        count += 1
                    else:
                        break

            if is_distinct:
                s += nums[j]

            j += 1

        if s > res:
            res = s
        count = 0

    if res != -1:
        return res
    else:
        return 0

def helper(j, k, nums):
    h = {}
    for i in range(j, j + k):
        if nums[i] in h:
            return False
        h[nums[i]] = i
    
    return True

print(maximumSubarraySum([1,5,4,2,9,9,9], 3))