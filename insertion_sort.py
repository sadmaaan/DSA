def selection_sort(arr): # best case: O(n), worst case: O(n^2) *** works well in small data
    # *** used in hybrid sorting algorithm!!!
    for i in range(len(arr) - 1):
        j = i + 1
        while j > 0:
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            else:
                break   
            j -= 1
    return arr
        

a = [-1, -2, 98, 0, 1, 2, 69]
print(selection_sort(a))