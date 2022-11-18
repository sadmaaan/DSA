class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            c = ord('A') + (columnNumber - 1) % 26
            res = chr(c) + res
            columnNumber = (columnNumber) // 26
        
        return res

sol = Solution()
print(sol.convertToTitle(28))