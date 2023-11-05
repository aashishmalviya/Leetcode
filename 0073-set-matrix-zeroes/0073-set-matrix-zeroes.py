class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_first_col, rows, cols = False, len(matrix), len(matrix[0])
        
        for current_row in range(rows):
            
            if matrix[current_row][0] == 0:
                zero_first_col = True
            
            for current_col in range(1, cols):
                if matrix[current_row][current_col] == 0:
                    matrix[current_row][0] = matrix[0][current_col] = 0
                    
        
        for current_row in range(rows-1, -1, -1):
            for current_col in range(cols-1, 0, -1):
                if matrix[current_row][0] == 0 or matrix[0][current_col] == 0:
                    matrix[current_row][current_col] = 0
            if zero_first_col == True:
                matrix[current_row][0] = 0
            
        