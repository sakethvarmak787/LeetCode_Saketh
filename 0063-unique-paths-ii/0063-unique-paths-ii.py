class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # dp[r][c] = number of ways to reach (r, c)
        dp = [[0] * cols for _ in range(rows)]

        # start position
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1

        for r in range(rows):
            for c in range(cols):

                # if obstacle → no paths
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    # from top
                    if r > 0:
                        dp[r][c] += dp[r - 1][c]

                    # from left
                    if c > 0:
                        dp[r][c] += dp[r][c - 1]

        return dp[rows - 1][cols - 1]