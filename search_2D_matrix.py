class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        if cols == 0:
            return [-1, -1]
        if rows == 1:
            self.binary_search(matrix, 0, 0, cols-1, target)
        
        row_start = 0
        row_end = rows - 1
        col_mid = cols // 2
        
        # run till 2 loops remaining
        while row_start < row_end-1:
            mid = row_start + (row_end - row_start) // 2
            
            if matrix[mid][col_mid] == target:
                return [mid][col_mid]
            elif matrix[mid][col_mid] < target:
                row_start = mid
            else:
                row_end = mid
                
        # now 2 rows remaining
        if matrix[row_start][col_mid] == target:
            return [row_start][col_mid]
        elif matrix[row_start+1][col_mid] == target:
            return [row_start+1][col_mid]
        
        # search in first half
        if target <= matrix[row_start][col_mid-1]:
            self.binary_search(matrix, row_start, 0, col_mid, target)
        # search in second half
        if target <= matrix[row_start][col_mid+1] and target <= matrix[row_start][cols-1]:
            self.binary_search(matrix, row_start, col_mid+1, cols-1, target)
        # search in third half
        if target <= matrix[row_start+1][col_mid-1]:
            self.binary_search(matrix, row_start+1, 0, col_mid, target)
        # search in fourth half
        else:
            self.binary_search(matrix, row_start+1, col_mid+1, cols-1, target)
            
        
    def binary_search(self, matrix, row, col_start, col_end, target):    
        while col_start <= col_end:
            mid = col_start + (col_end - col_start) // 2

            if matrix[row][mid] == target:
                return [row][mid]
            elif matrix[row][mid] < target:
                col_start = mid + 1
            else:
                col_end = mid - 1
    
        return [-1, -1]