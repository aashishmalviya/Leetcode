class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            mid = (top + bottom)//2
            mid_row = matrix[mid]

            if target < mid_row[0]:
                bottom = mid - 1 
            elif target > mid_row[-1]:
                top = mid + 1
            else:

                low = 0
                high = cols - 1

                while (low <= high):                
                    mid_index = (low + high)//2

                    if mid_row[mid_index] == target:
                        return True
                    elif mid_row[mid_index] > target:
                        high = mid_index - 1
                    else:
                        low = mid_index + 1
                return False