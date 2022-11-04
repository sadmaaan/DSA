def nextGreatestLetter(letters, target):
    low = 0
    high = len(letters) - 1
    
    while low <= high:            
        mid = low + (high - low) // 2
        
        if ord(letters[mid]) <= ord(target):
            low = mid + 1
        else:
            high = mid - 1
    
    return letters[low % len(letters)]


print(nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], "e"))