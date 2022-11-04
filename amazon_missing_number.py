def MissingNumber(arr):
    # code here
    i = 0
    while i < len(arr):
        correct_index = arr[i] - 1
        
        if arr[i] < len(arr) and arr[i] != arr[correct_index]:
            temp = arr[i]
            arr[i] = arr[correct_index]
            arr[correct_index] = temp
        else:
            i += 1
        
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1
    
    return len(arr) + 1

print(MissingNumber([1,2,3,5,7,4,6]))