from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)

        def block_to_position(current_block):
            r, c = divmod(current_block-1, n)
            if r%2 == 0:
                return n-1-r, c
            else:
                return n-1-r, n-1-c

        visited = set()
        q = deque()
        q.append((1,0))

        while q:
            current_block, total_steps_till_now = q.popleft()
            r, c = block_to_position(current_block)

            if board[r][c] != -1:
                current_block = board[r][c]

            if current_block == n*n:
                return total_steps_till_now

            for step_size in range(1, 7):
                new_block = current_block + step_size

                if new_block <= n*n and new_block not in visited:
                    visited.add(new_block)
                    q.append((new_block, total_steps_till_now + 1))

        return -1