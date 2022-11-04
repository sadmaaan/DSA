def isSubsequence(s, t):
    startS = 0
    startT = 0
    count = 0

    while startS < len(s):
        if startT == len(t):
            break

        if s[startS] == t[startT]:
            startS += 1
            startT += 1
            count += 1
        else:
            startT += 1
        
    
    if count == len(s):
        return True
    else:
        return False

print(isSubsequence("abc", "ahbgdc"))