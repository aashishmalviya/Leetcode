class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ans = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(i, j):
            
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j] != '1':
                return
        
            grid[i][j] = '#'
            
            for dirX, dirY in (0, 1), (0, -1), (1, 0), (-1, 0):
                newX = dirX + i
                newY = dirY + j
                
                dfs(newX, newY)
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        
        return ans