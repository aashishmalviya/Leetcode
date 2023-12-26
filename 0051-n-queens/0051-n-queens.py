class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        state = [["."] * n for i in range(n)]
        result = []

        cols_covered = set()
        diag_covered = set()
        anti_diag_covered = set()


        def queen_placer(current_row):
            if current_row == n:
                result.append(["".join(row) for row in state])
                return

            for current_col in range(n):
                cord_diff = current_row - current_col
                cord_sum = current_row + current_col

                if not (current_col in cols_covered or cord_diff in diag_covered or cord_sum in anti_diag_covered):
                    cols_covered.add(current_col)
                    diag_covered.add(cord_diff)
                    anti_diag_covered.add(cord_sum)

                    state[current_row][current_col] = 'Q'
                    queen_placer(current_row + 1)

                    #backtrack - reset to original
                    cols_covered.remove(current_col)
                    diag_covered.remove(cord_diff)
                    anti_diag_covered.remove(cord_sum)
                    state[current_row][current_col] = '.'

        queen_placer(current_row = 0)
        return result


