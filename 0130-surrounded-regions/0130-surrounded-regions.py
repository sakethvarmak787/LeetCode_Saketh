class Solution:
    def solve(self, board):
        if not board:
            return
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            
            board[r][c] = "T"  # mark safe
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # STEP 1: mark boundary-connected O's
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)

        # STEP 2: flip remaining
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"