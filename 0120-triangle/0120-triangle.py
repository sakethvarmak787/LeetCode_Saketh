class Solution:
    def minimumTotal(self, triangle):

        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(triangle) - 1:
                return triangle[i][j]

            down = dfs(i + 1, j)
            diag = dfs(i + 1, j + 1)

            memo[(i, j)] = triangle[i][j] + min(down, diag)
            return memo[(i, j)]

        return dfs(0, 0)