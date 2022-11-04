def ss_rec(arr, row, col, max):
    if row == 0:
        return
    
    if col < row:
        if arr[col] > arr[max]:
            ss_rec(arr, row, col+1, col)
        else:
            ss_rec(arr, row, col+1, max)
        
    else:
        temp = arr[max]
        arr[max] = arr[row-1]
        arr[row-1] = temp

        ss_rec(arr, row-1, 0, 0)
        
    return arr


print(ss_rec([4,3,2,1,5,56,78], 7, 0, 0))