def flipAndInvertImage(image):
    for row in image:
        l = len(row) - 1
        for col in range(len(row) // 2):
            temp = row[col]
            row[col] = row[l]
            row[l] = temp
            l -= 1
    
    for row in image:
        for col in range(len(row)):
            row[col] = row[col] ^ 1
    
    return image

print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))