from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        # Convert square number → (row, col)
        def get_position(num):
            row = n - 1 - (num - 1) // n
            col = (num - 1) % n

            # reverse column for zig-zag rows
            if ((n - 1 - row) % 2 == 1):
                col = n - 1 - col #flippinfg the col for 12<----7 case

            return row, col

        queue = deque()
        queue.append((1, 0))  # (current_square, moves)
        visited = set([1])

        while queue:
            curr, moves = queue.popleft()

            # reached last cell
            if curr == n * n:
                return moves

            # try all dice rolls
            for dice in range(1, 7):
                next_square = curr + dice

                if next_square > n * n:
                    continue

                r, c = get_position(next_square)

                # if snake or ladder
                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1