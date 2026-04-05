class Solution:
    def maximalSquare(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]
        max_side = 0

        for r in range(rows):
            for c in range(cols):

                if matrix[r][c] == "1":

                    # first row or column
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(
                            dp[r-1][c],     # up
                            dp[r][c-1],     # left
                            dp[r-1][c-1]    # diagonal
                        )

                    max_side = max(max_side, dp[r][c])

        return max_side * max_side