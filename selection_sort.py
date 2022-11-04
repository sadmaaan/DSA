def selection_sort(arr): # best case: O(n^2), worst case: O(n^2) *** works well in lower size array
    for i in range(len(arr)):
        last_index = len(arr) - i - 1
        max_index = get_max_index(arr, 0, last_index)

        temp = arr[max_index]
        arr[max_index] = arr[last_index]
        arr[last_index] = temp
    
    return arr

def get_max_index(arr, first_index, last_index):
    max = arr[first_index]
    max_index = first_index

    for i in range(last_index + 1):
        if arr[i] > max:
            max = arr[i]
            max_index = i
            
    return max_index
        

a = [-1, -2, 98, 0, 1, 2, 69]
print(selection_sort(a))