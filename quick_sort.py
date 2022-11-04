def quick_sort(arr, low, high):
    if low >= high:
        return

    start = low
    end = high
    mid = low + (end - low) // 2
    pivot = arr[mid]

    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        
        if start <= end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1

    quick_sort(arr, low, end)
    quick_sort(arr, start, high)

    return arr


a = [-1, -2, 98, 0, 1, 2, 69, 4, 567, 1000, 98, 69]
print(quick_sort(a, 0, len(a) - 1))