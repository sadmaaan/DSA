#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')

        i, j = 0, 1
        while i < len(prices) - 1 and j < len(prices):
            if prices[i] > prices[j]:
                i += 1
                j += 1
            else:
                profit = prices[j] - prices[i]
                j += 1
            
                max_profit = max(max_profit, profit)

        return max_profit if max_profit > 0 else 0

sol = Solution()
print(sol.maxProfit([2,1,2,1,0,1,2]))
# @lc code=end

