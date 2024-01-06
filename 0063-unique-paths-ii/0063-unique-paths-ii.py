# https://leetcode.com/problems/unique-paths-ii/discuss/3896905/100-Dynamic-Programming-VIDEO-Optimal-Solution

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        previous_row = [0] * cols
        current_row = [0] * cols
        
        previous_row[0] = 1
        
        for i in range(rows):
            current_row[0] = 0 if grid[i][0] == 1 else previous_row[0]
            for j in range(1, cols):
                current_row[j] = 0 if grid[i][j] == 1 else current_row[j-1] + previous_row[j]
            previous_row[:] = current_row
            
        return previous_row[-1]