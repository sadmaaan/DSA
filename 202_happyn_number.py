class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.digitSquare(slow)
            fast = self.digitSquare(self.digitSquare(fast))

            if slow == fast:
                break
        
        return slow == 1
        
    def digitSquare(self, n):
        sum = 0
        while n:
            last_digit = n % 10
            sum += last_digit * last_digit
            n = n // 10
        
        return sum
            

sol = Solution()
print(sol.isHappy(12))