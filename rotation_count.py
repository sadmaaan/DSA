def find_pivot(arr):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if mid < end and arr[mid] > arr[mid+1]:
            return mid
        elif mid > start and arr[mid] < arr[mid-1]:
            return mid-1
        elif arr[mid] > arr[start]:
            start = mid + 1
        else:
            end = mid - 1
            
    return -1

def find_pivot_duplicate(arr):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if mid < end and arr[mid] > arr[mid+1]:
            return mid
        elif mid > start and arr[mid] < arr[mid-1]:
            return mid-1
        elif arr[mid] == arr[start] and arr[mid] == arr[end]:
            if arr[start] > arr[start+1]:
                return start
            start += 1

            # if arr[end] < arr[end-1]: #kunal
            #     return end - 1
            if arr[end] > arr[end-1]: #sadman
                return end
            end -+ 1
        elif arr[start] < arr[mid] or arr[start] == arr[mid] and arr[end] > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

pivot = find_pivot([3,4,5,6,2])

if pivot == -1:
    print("0")
else:
    rotation_count = pivot + 1
    print(rotation_count)
# print(find_pivot_duplicate([2,2,2,2,5,2,2]) + 1)