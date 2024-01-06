# https://leetcode.com/problems/minimum-path-sum/discuss/3345844/Python-3-oror-7-lines-prefix-array-wexplanation-oror-TM%3A-95-81

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        
        for i in range(1, rows): grid[i][0] += grid[i-1][0]
        for j in range(1, cols): grid[0][j] += grid[0][j-1]
            
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[rows-1][cols-1]