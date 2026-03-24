class Solution:
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        # Step 1: mark transitions
        for r in range(rows):
            for c in range(cols):

                live_neighbors = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if abs(board[nr][nc]) == 1:
                            live_neighbors += 1

                # apply rules
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1   # live → dead

                else:
                    if live_neighbors == 3:
                        board[r][c] = 2    # dead → live

        # Step 2: finalize values
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0