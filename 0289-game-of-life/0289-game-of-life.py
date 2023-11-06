class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        
        directions = [(1,0), (1,-1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        
        for current_row in range(rows):
            for current_col in range(cols):
                
                alive_neighbours_count = 0
                
                for x, y in directions:
                    next_row = current_row + x
                    next_col = current_col + y
                    
                    if next_row < rows and next_row >= 0 and next_col < cols and next_col >= 0 and abs(board[next_row][next_col]) == 1:
                        alive_neighbours_count += 1
                
                if board[current_row][current_col] == 1 and (alive_neighbours_count < 2 or alive_neighbours_count > 3):
                    board[current_row][current_col] = -1
                    
                elif board[current_row][current_col] == 0 and alive_neighbours_count == 3:
                    board[current_row][current_col] = 2
                    
        
        for current_row in range(rows):
            for current_col in range(cols):
                
                board[current_row][current_col] = 1 if board[current_row][current_col]>0 else 0
                
                
        return board
        