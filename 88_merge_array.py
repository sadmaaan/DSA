from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
            
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] != 0 and nums1[i] <= nums2[j]:
                i += 1
            else:
                temp = nums1[:i]
                temp.append(nums2[j])
                nums1 = temp + nums1[i:]
                j += 1
                i += 1

        # nums1 = nums1[:m-1]
    
        print(nums1[-3])


sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3, 
nums2 = [2,5,6]
n = 3
sol.merge(nums1, m, nums2, n)
# print(nums1)