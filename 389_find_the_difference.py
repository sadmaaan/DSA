def findTheDifference(s, t):
        extra_char = 0
        
        for ch in s:
            extra_char ^= ord(ch)
            
        for ch in t:
            extra_char ^= ord(ch)
            
        return chr(extra_char)

print(findTheDifference("abc", ("caxb")))