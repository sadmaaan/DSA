#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
from typing import List
# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        local_sum = 0

        for i in range(k):
            local_sum += nums[i]
        
        max_sum = local_sum

        for j in range(len(nums) - k):
            local_sum = max_sum - nums[j] + nums[j + k]

            max_sum = max(max_sum, local_sum)


        return max_sum / k
                

sol = Solution()
print(sol.findMaxAverage([0,4,0,3,2], 1))
# @lc code=end

