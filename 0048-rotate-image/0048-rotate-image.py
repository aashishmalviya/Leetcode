class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix_size = len(matrix)
        
        matrix.reverse()
        
        for current_row in range(matrix_size):
            for current_col in range(current_row + 1, matrix_size):
                
                matrix[current_row][current_col], matrix[current_col][current_row] = matrix[current_col][current_row], matrix[current_row][current_col]
                
        return matrix