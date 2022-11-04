class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        pivot = self.find_pivot(nums)
        
        if pivot == -1:
            return nums[0]
        else:
            return nums[pivot+1]
        
    def find_pivot(self, arr):
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if mid < end and arr[mid] > arr[mid+1]:
                return mid
            elif mid > start and arr[mid] < arr[mid-1]:
                return mid-1
            elif arr[mid] > arr[start]:
                start = mid + 1
            else:
                end = mid - 1
                
        return -1