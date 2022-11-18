class Solution:
    def romanToInt(self, s: str) -> int:
        h_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        l = len(s)
        res = 0
        i = 0
        while i < l:
            if i + 1 < l and s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                temp = h_map.get(s[i+1]) - h_map.get(s[i])
                res += temp
                i += 2
            elif i + 1 < l and s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                temp = h_map.get(s[i+1]) - h_map.get(s[i])
                res += temp
                i += 2
            elif i + 1 < l and s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                temp = h_map.get(s[i+1]) - h_map.get(s[i]) 
                res += temp
                i += 2
            else:
                res += h_map.get(s[i])
                i += 1
        
        return res


s = Solution()
print(s.romanToInt("MCMXCIV"))