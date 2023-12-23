class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        rows = len(board)
        cols = len(board[0])
        
        q = deque()
        
        for i in range(rows):
            for j in range(cols):
                if (i==0 or i==rows-1 or j==0 or j==cols-1) and board[i][j] == 'O':
                    board[i][j] = '#'
                    q.append((i,j))
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        while q:
            i, j = q.popleft()
            for X, Y in directions:
                nX = i + X
                nY = j + Y
                if nX >= 0 and nX < rows and nY >=0 and nY < cols and board[nX][nY] == 'O':
                    board[nX][nY] = '#'
                    q.append((nX, nY))
                    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
            