# https://leetcode.com/problems/valid-sudoku/discuss/3277043/Beats-96.78-oror-Short-7-line-Python-solution-(with-detailed-explanation)
# res += [(i, element), (element, j), (i // 3, j // 3, element)]
# Pay attention to types (int, str), (str, int), (int, int, str) and what occurences they describe.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = []
        
        for current_row in range(9):
            for current_col in range(9):
                current_element = board[current_row][current_col]
                if current_element != '.':
                    result += [(current_row, current_element), (current_element, current_col), (current_row//3, current_col//3, current_element)]
                    
        #print(result)
        return len(result) == len(set(result))