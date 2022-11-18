#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=star
from typing import List
import math

# class Solution:
#     def smallestDivisor(self, nums: List[int], threshold: int) -> int:
#         nums = sorted(nums)
#         low = 0
#         high = len(nums)

#         while low < high:
#             mid = low + (high - low) // 2
#             temp = self.helper(nums, nums[mid])
#             if temp == threshold:
#                 return nums[mid]
#             elif temp < threshold:
#                 high = mid - 1
#             else:
#                 low = mid + 1
        
#         return nums[low]
        
    
#     def helper(self, nums, val):
#         res = 0

#         for num in nums:
#             res += math.ceil(num / val)
        
#         return res

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums = sorted(nums)
        low = len(nums)
        high = nums[-1] + 1

        while low < high:
            mid = low + (high - low) // 2

            if self.helper(nums, mid) > threshold:
                low = mid + 1
            else:
                high = mid
        
        return low
        
    
    def helper(self, nums, val):
        res = 0

        for num in nums:
            res += math.ceil(num / val)
        
        return res


sol =Solution()
print(sol.smallestDivisor([21212,10101,12121], 1000000))
# @lc code=end
