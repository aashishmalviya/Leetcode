# Ref 1: https://leetcode.com/problems/n-queens-ii/discuss/2111513/Python-Solution-with-Explanation

# Ref 2: https://leetcode.com/problems/n-queens-ii/discuss/1237811/Short-and-Easy-w-Explanation-and-Visualization-or-Backtracking-Explained!

class Solution:
    def totalNQueens(self, n: int) -> int:
        # state = [["."] * n for _ in range(n)]
        # res  = []

        cols_covered = set()
        diag_covered = set()
        anti_diag_covered = set()

        def nQueen_valid_solutions_counter(current_row) -> int:
            if current_row == n:
                #valid_states_count += 1
                return 1

            valid_states_count = 0

            for current_col in range(n):
                cord_diff = current_row - current_col
                cord_sum = current_row + current_col

                if (current_col not in cols_covered and cord_diff not in diag_covered and cord_sum not in anti_diag_covered):
                    cols_covered.add(current_col)
                    diag_covered.add(cord_diff)
                    anti_diag_covered.add(cord_sum)

                    valid_states_count += nQueen_valid_solutions_counter(current_row + 1)

                    cols_covered.remove(current_col)
                    diag_covered.remove(cord_diff)
                    anti_diag_covered.remove(cord_sum)
            
            return valid_states_count

        return nQueen_valid_solutions_counter(current_row = 0)