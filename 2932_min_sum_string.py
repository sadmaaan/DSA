class Solution:
    def minimumSum(self, num: int) -> int:
        # as numbers are fixed size (length = 4)
        # we always get the minimum ans by 2 / 2
        s = ""
        while num:
            rem = num % 10
            s += (f'{rem}')
            num //= 10
        
        x = "".join(sorted(s))

        s1, s2 = x[0] + x[2], x[1] + x[3]

        return int(s1) + int(s2)


sol = Solution()
print(sol.minimumSum(2932))