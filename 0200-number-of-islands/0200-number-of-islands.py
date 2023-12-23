class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        island_count = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        def helper(i, j):
            
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j] != '1':
                return
            
            grid[i][j] = '#'
            
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            
            for x,y in directions:
                helper(i+x, j+y)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    helper(i, j)
                    island_count += 1
        
        return island_count