def three_sum(nums, target): # 0 <= i < j < k < target < n, Time: O(n^3)
    n = len(nums)
    count = 0
    for i in range(0, n - 2, 1):
        for j in range(i + 1, n - 1, 1):
            for k in range(j + 1, n, 1):
                if nums[i] + nums[j] + nums[k] < target:
                    count += 1
    
    return count

def threeSumSmaller(nums, target): # Time: O(n^2)
    ans = 0
    nums.sort()
    for i in range(0, len(nums) - 2):
      start, end = i + 1, len(nums) - 1
      while start < end:
        if nums[i] + nums[start] + nums[end] < target:
          ans += end - start
          start += 1
        else:
          end -= 1

    return ans



# print(three_sum([-2, 0, 1, 3], 2))
# print(threeSumSmaller([-2, 0, 1, 3], 2))
print(threeSumSmaller([5, 1, 3, 4, 7], 12))
