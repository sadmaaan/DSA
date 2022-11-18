#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#

# @lc code=start
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        h = {}
        rank = [] # [5,3,4,2,8,6,7,1,3]
        i = 0
        j = 0
        while j < len(sorted_arr):
            if sorted_arr[j] not in h:
                h[sorted_arr[j]] = i + 1
                i += 1
            j += 1


        for num in arr:
            if num in h:
                rank.append(h.get(num))

        return rank


sol = Solution()
print(sol.arrayRankTransform([37,12,28,9,100,56,80,5,12]))

# @lc code=end

