def firstUniqChar(s):
    h = {}
        
    for i in range(len(s)):
        if s[i] not in h:
            h[s[i]] = 1
        else:
            h[s[i]] += 1

    for j in range(len(s)):
        if h[s[j]] == 1:
            return j

    return -1

print(firstUniqChar("ababababckbcytmnjm"))