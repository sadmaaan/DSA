from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        if (n) % 2 != 0:
            return
        
        while n:
            maxi, mini, maximum, minimum = self.m(nums) 
            if maxi > mini:
                del nums[maxi]
                del nums[mini]
            else:
                del nums[mini]
                del nums[maxi]
            
            avg = (maximum + minimum) / 2
            
            if avg not in s:
                s.add(avg)
            
            n -= 2
        
        return len(s)
    
    def m(self, arr):
        maxi = float('-inf')
        mini = float('inf')
        x, y = -1, -1
        for i in range(len(arr)):
            if arr[i] > maxi:
                maxi = arr[i]
                x = i
            if arr[i] <= mini:
                mini = arr[i]
                y = i
                
        return x, y, maxi, mini
            


sol = Solution()
print(sol.distinctAverages([4,1,4,0,3,5,4,6,8,9,9,22,34,5]))