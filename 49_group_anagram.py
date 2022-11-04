from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)
    count = [0] * 26
    
    for s in strs:
        for c in s:
            count[ord(c) - ord("a")] += 1
        
        res[tuple(count)].append(s)
        count.clear()
            
    
    return res.values()
    
    
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))