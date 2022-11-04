def bs_rec(arr, row, col):
    if row == 0:
        return
    
    if col < row-1:
        if arr[col] > arr[col+1]:
            temp = arr[col]
            arr[col] = arr[col+1]
            arr[col+1] = temp

        bs_rec(arr, row, col+1)
        
    else:
        bs_rec(arr, row-1, 0)
        
    return arr


print(bs_rec([4,3,2,1,5], 5, 0))