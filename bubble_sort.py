import array as arr

def bubble_sort(arr): # best case: O(n), worst case: O(n^2)
    swapped = False
    for i in range(len(arr) - 1):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                swapped = True
        if not swapped:
            break

    return arr

# a = arr.array('i', [-1, -2, 98, 0, 1, 2, 69])
a = [-1, -2, 98, 0, 1, 2, 69]
print(bubble_sort(a))