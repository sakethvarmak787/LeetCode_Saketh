class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        dp = [[0]*n for _ in range(m)]

        dp[m-1][n-1] = grid[m-1][n-1]

        # last row
        for j in range(n-2, -1, -1):
            dp[m-1][j] = grid[m-1][j] + dp[m-1][j+1]

        # last column
        for i in range(m-2, -1, -1):
            dp[i][n-1] = grid[i][n-1] + dp[i+1][n-1]

        # rest
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]